import os
from cs50 import SQL
from flask import Flask, render_template, request, redirect, url_for, session


app = Flask(__name__)
app.config["SECRET_KEY"] = "sy77yvkNmvhGD4"

# Connect to the database
db = SQL("sqlite:///fiftyville.db")

# Define the correct answers
correct_answers = {
    "thief": "bruce",
    "city": ["new york", "new york city"],
    "accomplice": "robin"
}


@app.route("/atm_transactions", methods=["GET", "POST"])
def atm_transactions():
    """ Display and filter atm_transactions table """
    if request.method == "POST":
        month = int(request.form.get("month"))
        day = int(request.form.get("day"))
        atm_location = request.form.get("atm_location")
        session["atm_month"] = month
        session["atm_day"] = day
        session["atm_location"] = atm_location

    else:
        month = session.get("atm_month")
        day = session.get("atm_day")
        atm_location = session.get("atm_location")

    atm_transaction = db.execute("SELECT account_number, atm_location, transaction_type, amount FROM atm_transactions WHERE month = ? AND day = ? AND atm_location = ?", month, day, atm_location)
    location = db.execute("SELECT DISTINCT atm_location FROM atm_transactions ORDER BY atm_location;")
    return render_template("atm_transactions.html", atm_transaction=atm_transaction, month=month, day=day, atm_location=atm_location, location=location)


@app.route("/bakery_security_logs", methods=["GET", "POST"])
def bakery_security_logs():
    """ Display and filter bakery_security_logs table """
    if request.method == "POST":
        month = int(request.form.get("month"))
        day = int(request.form.get("day"))
        hour = int(request.form.get("hour"))
        session["bsl_month"] = month
        session["bsl_day"] = day
        session["bsl_hour"] = hour

    else:
        month = session.get("bsl_month")
        day = session.get("bsl_day")
        hour = session.get("bsl_hour")

    bakery_security_log = db.execute("SELECT hour, minute, license_plate, activity FROM bakery_security_logs WHERE month = ? AND day = ? AND hour = ?", month, day, hour)
    return render_template("bakery_security_logs.html", bakery_security_log=bakery_security_log, month=month, day=day, hour=hour)



@app.route("/crime_scene_reports", methods=["GET", "POST"])
def crime_scene_reports():
    """ Display and filter crime_scene_reports table """
    if request.method == "POST":
        month = int(request.form.get("month"))
        day = int(request.form.get("day"))
        session["csr_month"] = month
        session["csr_day"] = day

    else:
        month = session.get("csr_month")
        day = session.get("csr_day")

    # Query the database for filtered results
    crime_scene_report = db.execute("SELECT street, description FROM crime_scene_reports WHERE month = ? AND day = ?;", month, day)
    return render_template("crime_scene_reports.html", crime_scene_report=crime_scene_report, month=month, day=day)


@app.route("/flights", methods=["GET", "POST"])
def flights():
    """ Display and filter flights table joined with airports table """
    if request.method == "POST":
        month = int(request.form.get("month"))
        day = int(request.form.get("day"))
        session["f_month"] = month
        session["f_day"] = day

    else:
        month = session.get("f_month")
        day = session.get("f_day")

    # Query the database for filtered results
    flight = db.execute("""
                        SELECT flights.id AS id, hour, minute, origin.full_name AS origin_airport, destination.full_name AS destination_airport, origin.city AS origin_city, destination.city AS destination_city
                        FROM flights
                        JOIN airports AS origin
                        ON flights.origin_airport_id = origin.id
                        JOIN airports AS destination
                        ON flights.destination_airport_id = destination.id
                        WHERE month = ? AND day = ?
                        ORDER BY hour, minute;
    """, month, day)
    return render_template("flights.html", flight=flight, month=month, day=day)


@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        # Get user's answers from the form
        user_thief = request.form.get("thief").strip().lower()
        user_city = request.form.get("city").strip().lower()
        user_accomplice = request.form.get("accomplice").strip().lower()

        # Check if the user's answers are correct
        if (
            user_thief.lower() == correct_answers["thief"]
            and any(city in user_city for city in correct_answers["city"])
            and user_accomplice.lower() == correct_answers["accomplice"]
        ):
            # Correct answers - Redirect to a success page
            return redirect("/success")
        else:
            # Incorrect answers - Display an error message
            error_message = "Sorry, your answers are incorrect. Please try again."
            return render_template("index.html", error_message=error_message)

    return render_template("index.html")


@app.route("/interviews", methods=["GET", "POST"])
def interviews():
    """ Display and filter interviews table """
    if request.method == "POST":
        month = int(request.form.get("month"))
        day = int(request.form.get("day"))
        session["i_month"] = month
        session["i_day"] = day

    else:
        month = session.get("i_month")
        day = session.get("i_day")

    # Query the database for filtered results
    interview = db.execute("SELECT name, transcript FROM interviews WHERE month = ? AND day = ?;", month, day)
    return render_template("interviews.html", interview=interview, month=month, day=day)


@app.route("/passengers", methods=["GET", "POST"])
def passengers():
    """ Display and filter interviews table """
    if request.method == "POST":
        flight_id = int(request.form.get("flight_id"))
        session["flight_id"] = flight_id

    else:
        flight_id = session.get("flight_id")

    # Query the database for filtered results
    passenger = db.execute("SELECT passport_number, seat FROM passengers WHERE flight_id = ?;", flight_id)
    return render_template("passengers.html", passenger=passenger, flight_id=flight_id)


@app.route("/people", methods=["GET", "POST"])
def people():
    # Check if it's a POST request (form submitted)
    try:
        if request.method == "POST":
            search = request.form.get("search")
            value = request.form.get("value")
            session["search"] = search
            session["value"] = value

            if search in ["passport_number", "account_number"]:
                value = int(value)

            # Store search criteria and value in the session
            people = db.execute(f"""
                                SELECT name, phone_number, passport_number, license_plate, account_number AS bank_account
                                FROM people
                                JOIN bank_accounts
                                ON people.id = person_id
                                WHERE {search} = ?;""", value)
        else:
            people = []
            search = session.get("search")
            value = session.get("value")

        # Render the template with the query results and filter values
        return render_template("people.html", people=people, search=search, value=value)
    except ValueError:
        error_message = "Sorry, search field and search value do not match. Please try again."
        return render_template("people.html", error_message=error_message)



@app.route("/phone_calls", methods=["GET", "POST"])
def phone_calls():
    """ Display and filter interviews table """
    if request.method == "POST":
        month = int(request.form.get("month"))
        day = int(request.form.get("day"))
        session["pc_month"] = month
        session["pc_day"] = day

    else:
        month = session.get("pc_month")
        day = session.get("pc_day")

    phone_call = db.execute("SELECT caller, receiver, duration FROM phone_calls WHERE month = ? AND day = ? ORDER BY duration;", month, day)
    return render_template("phone_calls.html", phone_call=phone_call, month=month, day=day)


@app.route("/success")
def success():
    """ Display a success message when the answers are correct """
    success_message = "Congratulations! You've solved the mystery!"
    return render_template("success.html", success_message=success_message)


if __name__ == "__main__":
    app.run(debug=True)
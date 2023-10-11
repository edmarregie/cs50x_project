# Fiftyville Mystery Web App

Welcome to the Fiftyville Mystery web application! This app is designed to help you solve the mystery of the stolen CS50 Duck in the town of Fiftyville. Authorities believe that the thief stole the duck and then, shortly afterwards, took a flight out of town with the help of an accomplice. All you know is that the theft took place on July 28, 2021, and it happened on Humphrey Street.

#### Video Demo: [Fiftyville Mystery Web App](https://youtu.be/D0R2Z-X8SZM)

## Prerequisites

Before embarking on your journey to solve the Fiftyville Mystery, ensure that you have the essential prerequisites in place:

- Python 3.x
- Flask
- cs50 (a vital library for seamless interaction with the SQL database)

If you don't have Flask and cs50 installed, you can acquire them through the following pip commands:

```bash
pip install Flask
pip install cs50
```

## Features

### Navigation

**Step 1:** Explore the vast troves of data in the Fiftyville Mystery database using the intuitive navigation system. You can access an array of tables to gather clues, including:

- **ATM Transactions:** Delve into financial transactions associated with ATMs.

  **Step 1.1:** Click on "ATM Transactions" in the navigation bar to access the ATM Transactions tab.

  **Step 1.2:** Filter ATM transactions by specifying the month, day, and ATM location.

  **Step 1.3:** View the filtered ATM transactions, complete with account numbers, ATM locations, transaction types, and amounts.

- **Bakery Security Logs:** Scrutinize security logs from the local bakery.

  **Step 1.1:** Click on "Bakery Security Logs" in the navigation bar to access the Bakery Security Logs tab.

  **Step 1.2:** Filter bakery security logs by specifying the month, day, and hour.

  **Step 1.3:** Explore the filtered bakery security logs, including hour, minute, license plate, and activity.

- **Crime Scene Reports:** Investigate incidents and their details.

  **Step 1.1:** Click on "Crime Scene Reports" in the navigation bar to access the Crime Scene Reports tab.

  **Step 1.2:** Filter crime scene reports by specifying the month and day.

  **Step 1.3:** Review the filtered crime scene reports, revealing street names and descriptions.

- **Flights:** Trace flight records for potential escape routes.

  **Step 1.1:** Click on "Flights" in the navigation bar to access the Flights tab.

  **Step 1.2:** Filter flight records by specifying the month and day.

  **Step 1.3:** Examine the filtered flight records, detailing flight IDs, hours, minutes, origin airports, destination airports, and cities.

- **Interviews:** Read through interviews conducted during the investigation.

  **Step 1.1:** Click on "Interviews" in the navigation bar to access the Interviews tab.

  **Step 1.2:** Filter interviews by specifying the month and day.

  **Step 1.3:** Peruse the filtered interviews, including interviewee names and transcripts.

- **Passengers:** Examine the list of passengers on various flights.

  **Step 1.1:** Click on "Passengers" in the navigation bar to access the Passengers tab.

  **Step 1.2:** Filter passengers by specifying the flight ID.

  **Step 1.3:** Investigate the filtered passenger list, complete with passport numbers and seat information.

- **Phone Calls:** Unearth conversations to uncover more evidence.

  **Step 1.1:** Click on "Phone Calls" in the navigation bar to access the Phone Calls tab.

  **Step 1.2:** Filter phone calls by specifying the month and day.

  **Step 1.3:** Review the filtered phone call records, including caller, receiver, and call duration.

### People Search

**Step 2:** Embark on the quest to locate individuals within the database using a diverse set of search criteria. You can search based on passport numbers, account numbers, and more, making it an invaluable tool for your investigation.

- Use the "People" tab in the navigation bar to perform these searches.

### Crack the Case

**Step 3:** Your primary mission is to decipher the riddle by deducing three key pieces of information:

1. **The Thief's Identity**: Deduce the name of the thief who stole the CS50 Duck.

   **Step 3.1:** On the home page, enter the name of the thief in the input field labeled "Who is the thief?".

2. **Destination City**: Uncover the city where the thief made their escape.

   **Step 3.2:** In the home page, provide the city where the thief escaped to in the input field labeled "What city did the thief escape to?".

3. **Accomplice's Name**: Reveal the identity of the thief's partner in crime.

   **Step 3.3:** Still on the home page, enter the name of the thief's accomplice in the input field labeled "Who is the thief's accomplice?".

- When you submit your answers, the application will scrutinize your responses. If they align with the truth, you will be gracefully redirected to a success page. In case your answers fall short, an error message will guide you to make another attempt.

## Acknowledgments

This web app is a final project for the CS50x course offered by Harvard University.

## Author

- **Edmar Regie Rodriguez**
- **Location:** Manila, Philippines

## Inspiration

This project was inspired by [CS50x Problem Set](https://cs50.harvard.edu/x/2023/psets/7/fiftyville/#fiftyville).

Enjoy your journey into the heart of Fiftyville as you explore the database and work tirelessly to solve the enigmatic case of the stolen CS50 Duck!

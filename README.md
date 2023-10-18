# CSV Data Flask API

A simple Flask application that provides an API for working with CSV data. You can list all data, get data by ID, and filter data by column and value.

## Table of Contents

- [Getting Started](#getting-started)
- [Endpoints](#endpoints)
  - [List All Data](#list-all-data)
  - [Get Data by ID](#get-data-by-id)
  - [Filter Data](#filter-data)

## Getting Started

To run the CSV Data API, follow these steps:

1. Make sure you have Python and Flask installed.

2. Clone this repository or download the source code.

3. Install the required packages
   ```bash
   pip install -r requirements.txt
   ```

4. Open a terminal, navigate to the project directory, and run the Flask app:

   ```bash
   python app.py
   ```
6. The app will be accessible at http://127.0.0.1:5001/

## Endpoints

- ### List All Data
- Endpoint: /data
- Method: GET
- Description: Returns a JSON array containing all data from the CSV file.

- ### Get Data by ID
- Endpoint: /data/<id>
- Method: GET
- Description: Returns a JSON object containing data with the specified ID if it exists, or a 404 error if not found.


- ### Filter Data
- Endpoint: /filter
- Method: GET
- Query Parameters:
1. column (string): The name of the column to filter by.
2. value (string): The value to filter for.
3. Description: Returns a JSON array containing data filtered by the specified column and value. If no data matches the filter, it returns an empty array.

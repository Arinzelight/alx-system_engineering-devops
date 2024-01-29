# 0x15. API

This project involved working with APIs, specifically the [JSONPlaceholder REST API](https://jsonplaceholder.typicode.com/). The main objectives were to gather data from the API and learn how to export it to CSV or JSON format.

## Tasks :page_with_curl:

### 0. Gather data from an API
- **File:** [0-gather_data_from_an_API.py](./0-gather_data_from_an_API.py)
- **Description:** Python script that retrieves information about the to-do list progress of a given employee ID.
- **Usage:** `python3 0-gather_data_from_an_API.py <employee ID>`
- **Output:** `Employee <employee name> is done with tasks(<# completed tasks>/<total # tasks>):`

### 1. Export to CSV
- **File:** [1-export_to_CSV.py](./1-export_to_CSV.py)
- **Description:** Python script that exports to-do list information of a given employee ID to CSV format.
- **Usage:** `python3 1-export_to_CSV.py <employee ID>`
- **File name:** `<user id>.csv`
- **Format:** `"<user id>","<username>","<task completed status>","<task title>"`

### 2. Export to JSON
- **File:** [2-export_to_JSON.py](./2-export_to_JSON.py)
- **Description:** Python script that exports to-do list information of a given employee ID to JSON format.
- **Usage:** `python3 2-export_to_JSON.py <employee ID>`
- **File name:** `<user id>.json`
- **Format:** `{ "<user id>": [ {"task": "<task title>", "completed": <task completed status>, "username": "<username>"}}, ... ]}`

### 3. Dictionary of list of dictionaries
- **File:** [3-dictionary_of_list_of_dictionaries.py](./3-dictionary_of_list_of_dictionaries.py)
- **Description:** Python script that exports to-do list information for all employees to JSON format.
- **Usage:** `python3 3-dictionary_of_list_of_dictionaries.py`
- **File name:** `todo_all_employees.json`
- **Format:** `{ "<user id>": [ {"username": "<username>", "task": "<task title>", "completed": <task completed status>}, {"username": "<username>", "task": "<task title>", "completed": <task completed status>}, ... ], "<user id>": [ {"username": "<username>", "task": "<task title>", "completed": <task completed status>}, {"username": "<username>", "task": "<task title>", "completed": <task completed status>}, ... ]}`


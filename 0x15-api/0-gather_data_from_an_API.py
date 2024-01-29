#!/usr/bin/python3
"""Returns to-do list information for a given employee ID."""
import requests
import sys

if __name__ == "__main__":
    # Check if the correct number of arguments is provided
    if len(sys.argv) != 2:
        print("Usage: {} <employee_id>".format(sys.argv[0]))
        sys.exit(1)

    # Ensure the provided employee ID is an integer
    try:
        employee_id = int(sys.argv[1])
    except ValueError:
        print("Error: Employee ID must be an integer.")
        sys.exit(1)

    url = "https://jsonplaceholder.typicode.com/"
    
    # Make request to get user data
    user_response = requests.get(url + "users/{}".format(employee_id))
    if user_response.status_code != 200:
        print("Error: Unable to fetch user data.")
        sys.exit(1)
    user = user_response.json()

    # Make request to get todo list data
    todos_response = requests.get(url + "todos", params={"userId": employee_id})
    if todos_response.status_code != 200:
        print("Error: Unable to fetch todo list data.")
        sys.exit(1)
    todos = todos_response.json()

    # Filter completed tasks
    completed = [t.get("title") for t in todos if t.get("completed")]

    # Print employee todo list progress
    print("Employee {} is done with tasks({}/{}):".format(
        user.get("name"), len(completed), len(todos)))
    for c in completed:
        print("\t{}".format(c))


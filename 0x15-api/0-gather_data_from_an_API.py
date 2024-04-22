import requests

def get_employee_todo_progress(employee_id):
    """Retrieves and displays an employee's TODO list progress.

    Args:
        employee_id (int): The ID of the employee.
    """

    base_url = "https://jsonplaceholder.typicode.com/"  # Replace with the actual API base URL
    user_url = f"{base_url}users/{employee_id}"
    todos_url = f"{base_url}todos"

    # Fetch user information
    user_response = requests.get(user_url)
    if user_response.status_code != 200:
        print(f"Error fetching user data: {user_response.status_code}")
        return

    user_data = user_response.json()
    employee_name = user_data["name"]

    # Fetch all TODOs and filter by employee ID
    todos_response = requests.get(todos_url)
    if todos_response.status_code != 200:
        print(f"Error fetching TODO data: {todos_response.status_code}")
        return

    todos_data = todos_response.json()
    employee_todos = [todo for todo in todos_data if todo["userId"] == employee_id]

    completed_tasks = [todo for todo in employee_todos if todo["completed"]]
    num_completed = len(completed_tasks)
    total_tasks = len(employee_todos)

    # Display results
    print(f"Employee {employee_name} is done with tasks({num_completed}/{total_tasks}):")
    for task in completed_tasks:
        print(f"\t {task['title']}")

if __name__ == "__main__":
    employee_id = int(input("Enter employee ID: "))
    get_employee_todo_progress(employee_id)

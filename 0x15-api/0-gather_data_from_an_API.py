import requests

def print_employee_todo_list_progress(employee_id):
    # Fetch the employee data
    employee_response = requests.get(f'https://jsonplaceholder.typicode.com/users/{employee_id}')
    employee = employee_response.json()

    # Fetch the TODOs for the employee
    todos_response = requests.get(f'https://jsonplaceholder.typicode.com/users/{employee_id}/todos')
    todos = todos_response.json()

    # Calculate the progress
    total_tasks = len(todos)
    done_tasks = len([todo for todo in todos if todo['completed']])
    
    # Print the first line
    print(f'Employee {employee["name"]} is done with tasks({done_tasks}/{total_tasks}):')

    # Print the completed tasks
    for todo in todos:
        if todo['completed']:
            print(f'\t {todo["title"]}')

# Test the function with an example employee ID
print_employee_todo_list_progress(1)

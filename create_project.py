import os
import sys


def create_project_structure(name):
    # Create directory with the given name
    os.makedirs(name, exist_ok=True)

    # Define file names
    py_file_name = f"{name}.py"
    test_file_name = f"test_{name}.py"

    # Create the .py file
    with open(os.path.join(name, py_file_name), "w") as py_file:
        py_file.write(f"# {name} module\n\n")
        py_file.write(f"def {name}():\n")  # Function named after the snake_case name
        py_file.write("    pass  # TODO: Implement main functionality\n\n")
        py_file.write(f"if __name__ == '__main__':\n")
        py_file.write(f"    {name}()\n")  # Call the function by its name

    # Create the test file
    with open(os.path.join(name, test_file_name), "w") as test_file:
        test_file.write(f"# Tests for {name} module\n\n")
        test_file.write(
            f"from {name} import {name}\n\n"
        )  # Import the function by its name
        test_file.write("def test_placeholder():\n")
        test_file.write("    assert True  # TODO: Implement tests\n")

    print(f"Created folder '{name}' with files '{py_file_name}' and '{test_file_name}'")


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python create_project.py <snake_case_name>")
        sys.exit(1)

    snake_case_name = sys.argv[1]
    create_project_structure(snake_case_name)

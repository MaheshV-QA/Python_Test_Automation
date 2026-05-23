# file_handling_example.py

# Function to write to a file
def write_to_file(filename):
    with open(filename, 'w') as file:
        file.write("Hello, world!\n")
        file.write("This is an example of file handling in Python.\n")
    print(f"Data written to {filename} successfully.")

# Function to read from a file
def read_from_file(filename):
    try:
        with open(filename, 'r') as file:
            content = file.read()
            print("File Content:\n", content)
    except FileNotFoundError:
        print(f"File '{filename}' not found. Please check the file path.")

# Function to append to a file
def append_to_file(filename):
    with open(filename, 'a') as file:
        file.write("Appending a new line to the file.\n")
    print(f"Data appended to {filename} successfully.")

# Function to read line by line
def read_line_by_line(filename):
    try:
        with open(filename, 'r') as file:
            print("Reading line by line:")
            for line in file:
                print(line.strip())  # Use strip() to remove trailing newline characters
    except FileNotFoundError:
        print(f"File '{filename}' not found. Please check the file path.")

# Function to read all lines into a list
def read_lines_to_list(filename):
    try:
        with open(filename, 'r') as file:
            lines = file.readlines()
            print("Lines as a List:", lines)
    except FileNotFoundError:
        print(f"File '{filename}' not found. Please check the file path.")

# Main execution
if __name__ == "__main__":
    filename = 'example.txt'

    # Writing to the file
    write_to_file(filename)

    # Reading the file
    read_from_file(filename)

    # Appending to the file
    append_to_file(filename)

    # Reading line by line
    read_line_by_line(filename)

    # Reading all lines into a list
    read_lines_to_list(filename)

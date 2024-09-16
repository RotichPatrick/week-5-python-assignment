# file_handling_assignment.py

def create_and_write_file():
    try:
        # Create a new file and write initial content
        with open('my_file.txt', 'w') as file:
            file.write('This is the first line of text.\n')
            file.write('Here is a second line with some numbers: 1234.\n')
            file.write('Finally, this is the third line of text.\n')
        print("File created and initial content written successfully.")

    except (PermissionError, IOError) as e:
        print(f"An error occurred while creating/writing the file: {e}")
    finally:
        print("File creation and writing process completed.")

def read_and_display_file():
    try:
        # Read the content of the file
        with open('my_file.txt', 'r') as file:
            content = file.read()
            print("File content:")
            print(content)

    except FileNotFoundError:
        print("The file does not exist.")
    except PermissionError:
        print("You do not have permission to read the file.")
    finally:
        print("File reading process completed.")

def append_to_file():
    try:
        # Append additional lines to the file
        with open('my_file.txt', 'a') as file:
            file.write('Appending a new line of text.\n')
            file.write('Here is another line with more text.\n')
            file.write('This is the third line to append.\n')
        print("Additional lines appended successfully.")

    except (PermissionError, IOError) as e:
        print(f"An error occurred while appending to the file: {e}")
    finally:
        print("File appending process completed.")

if __name__ == '__main__':
    create_and_write_file()
    read_and_display_file()
    append_to_file()
    read_and_display_file()  # Display file contents again to see the appended lines

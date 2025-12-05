class FileHandler:
    def __init__(self, file_path):
        self.file_path = file_path
        self.content = ""

    def read_file(self):
        """Reads the file and stores its content."""
        try:
            with open(self.file_path, "r") as file:
                self.content = file.read()
            print("File read successfully!")
        except FileNotFoundError:
            print("Error: File not found.")
        except Exception as e:
            print(f"Unexpected error: {e}")

    def append_to_file(self, text):
        """Appends text at the end of the file."""
        try:
            with open(self.file_path, "a") as file:
                file.write("\n" + text)
            print("Text appended successfully!")
        except Exception as e:
            print(f"Could not append to file: {e}")

    def print_content(self):
        """Prints the content of the file."""
        print("\n---- FILE CONTENT ----")
        print(self.content)


# -----------------------------
# Example Usage
# -----------------------------
if __name__ == "__main__":
    handler = FileHandler("demo_file.txt")  # Change filename as needed

    handler.read_file()
    handler.print_content()

    handler.append_to_file("This line was appended using Python OOP.")

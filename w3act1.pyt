class FileReader:
    def __init__(self, file_path):
        self.file_path = file_path
        self.content = ""

    def read_file(self):
        """Reads the file and stores the content."""
        try:
            with open(self.file_path, 'r') as file:
                self.content = file.read()
            print("File read successfully!\n")
        except FileNotFoundError:
            print("Error: File not found.")
        except Exception as e:
            print(f"An error occurred: {e}")

    def print_content(self):
        """Prints the content of the file."""
        if self.content:
            print("---- File Content ----")
            print(self.content)
        else:
            print("File is empty or not read yet.")

    def count_stars(self):
        """Counts the number of '*' characters in the file."""
        if not self.content:
            print("No content to analyze.")
            return 0
        star_count = self.content.count('*')
        print(f"\nNumber of '*' characters: {star_count}")
        return star_count


# -------------------------------
# Example usage:
# -------------------------------
if __name__ == "__main__":
    reader = FileReader("demo_file.txt")  # Replace with your file name
    reader.read_file()
    reader.print_content()
    reader.count_stars()

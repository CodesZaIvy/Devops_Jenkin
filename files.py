import os

def check_file_exists(filename):
    """Checks if the given file exists.

    Args:
        filename: The name of the file to check.

    Returns:
        True if the file exists, False otherwise.
    """

    return os.path.isfile(filename)

if __name__ == "__main__":
    # Check if README.md exists.
    readme_exists = check_file_exists("README.md")

    # Check if LICENSE exists.
    license_exists = check_file_exists("LICENSE")

    # Print the results.
    print("README.md exists:", readme_exists)
    print("LICENSE exists:", license_exists)


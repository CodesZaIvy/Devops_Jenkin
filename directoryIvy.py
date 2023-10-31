import os
import subprocess

def create_directory(directory_name):
    """Creates a directory with the given name.

    Args:
        directory_name: The name of the directory to create.
    """

    os.makedirs(directory_name, exist_ok=True)

def create_file(filename, content=None):
    """Creates a file with the given name and content.

    Args:
        filename: The name of the file to create.
        content: The content of the file to create.
    """

    with open(filename, "w") as f:
        if content is not None:
            f.write(content)

def check_current_working_directory():
    """Returns the current working directory."""

    return os.getcwd()

def list_files_and_perms():
    """Lists all the files in the current working directory together with their file permissions.

    Returns:
        A list of tuples, where each tuple contains the filename and the file permissions.
    """

    files = []
    for root, dirs, files in os.walk("."):
        for file in files:
            filepath = os.path.join(root, file)
            file_perms = os.stat(filepath).st_mode
            files.append((file, file_perms))
    return files

def push_to_repo():
    """Pushes the current directory to the remote repository."""

    subprocess.run(["git", "add", "."])
    subprocess.run(["git", "commit", "-m", "Created directory and files"])
    subprocess.run(["git", "push"])

if __name__ == "__main__":
    # Create a directory named "my_directory".
    create_directory("my_directory")

    # Create a .txt file named "my_text_file.txt".
    create_file("my_directory/my_text_file.txt")

    # Create a .py file named "my_python_file.py".
    create_file("my_directory/my_python_file.py")

    # Create a .sh file named "my_shell_file.sh".
    create_file("my_directory/my_shell_file.sh")

    # Create a .java file named "my_java_file.java".
    create_file("my_directory/my_java_file.java")

    # Check the current working directory.
    current_working_directory = check_current_working_directory()

    # Print the current working directory.
    print("Current working directory:", current_working_directory)

    # List all the files in the current working directory together with their file permissions.
    files_and_perms = list_files_and_perms()

    # Print the files and permissions.
    print("Files and permissions:")
    for file, perms in files_and_perms:
        print(f"{file}: {perms}")

    # Push the current directory to the remote repository.
    push_to_repo()



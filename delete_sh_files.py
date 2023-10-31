import os

def delete_sh_files(path):
    """Recursively deletes all .sh files from the given path and its subdirectories."""

    for root, dirs, files in os.walk(path):
        for file in files:
            if file.endswith(".sh"):
                os.remove(os.path.join(root, file))

if __name__ == "__main__":
    # Get the current working directory.
    cwd = os.getcwd()

    # Delete all .sh files from the current working directory and its subdirectories.
    delete_sh_files(cwd)


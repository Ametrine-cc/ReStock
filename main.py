import GitRestocker.project
import GitRestocker.update
import sys
import os


# Check if the script is being run directly
if __name__ == "__main__":
    # Check if the correct number of arguments is provided

    GitRestocker.update.checkupdate()
    if len(sys.argv) != 3:
        print("Usage: python main.py <project name> <programming language>")
        sys.exit(1)

    # Get the project name and language from command line arguments
    projectname = sys.argv[1]
    usrlanguage = sys.argv[2]

    # Initialize the Git repository with the provided project name and language
    GitRestocker.project.git.init(None, projectname, usrlanguage)
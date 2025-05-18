import GitRestocker.gitcheck as gitcheck
import sys
import os

class checkupdate:

    def __init__(self):
        # Check if ReStock.conf exists
        if not os.path.exists("ReStock.conf"):
            print("ReStock.conf not found. Please create it first.")
            return
        
        # Read the current version from ReStock.conf
        current_version = None

        with open("ReStock.conf", "r") as f:
            for line in f:
                if line.startswith("version="):
                    current_version = line.split("=")[1].strip()
                    break
                else:
                    print("Version not found in ReStock.conf")
                    return
            
        # Check if the current version is the latest version
        if current_version is None:
            print("Version not found in ReStock.conf")
            return
        # Simulate checking for the latest version
        
        latest_version = gitcheck.version()
        
        if latest_version == current_version:
            print("You are using the latest version of ReStock.")
        
        else:
            # Version check
            print("A new version of ReStock is available. Please update to the latest version.")
            print("Current version: " + current_version)
            print("Latest version: 0.1.0")
            print("Updating ReStock...")

            gitcheck.update()
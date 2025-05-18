import os
import dropbox
import tempfile
import shutil

def version():
    url = "https://raw.githubusercontent.com/Noticxs/ReStock/refs/heads/main/version.txt?token=GHSAT0AAAAAADDEAXHD32LG33YHNZINHQGG2BJWDDQ"
    latest_version = None

    with tempfile.TemporaryDirectory() as temp_dir:
        version_path = os.path.join(temp_dir, "version.txt")
        try:
            # Change to the temp directory and download the file using curl
            current_dir = os.getcwd()
            os.chdir(temp_dir)
            result = os.system(f'curl -s -O {url}')
            os.chdir(current_dir)

            if result != 0 or not os.path.exists(version_path):
                print("Failed to download version.txt")
                return None

            with open(version_path, "r") as f:
                for line in f:
                    if line.startswith("version="):
                        latest_version = line.split("=", 1)[1].strip()
                        break
                else:
                    print("Version not found in version.txt")
                    return None

            return latest_version

        except Exception as e:
            print(f"Error fetching version: {e}")
            return None

def update():
    pass
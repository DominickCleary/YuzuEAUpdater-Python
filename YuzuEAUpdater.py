import re
import os
import platform
import zipfile
import subprocess
import shutil
from pathlib import Path
import urllib.request
import json
import math
import stat

CURRENT_EXE = 'yuzu.exe'
CURRENT_APPIMAGE = 'yuzu.AppImage'
YUZU_VERSION_FILE = ".yuzuversion"
WINDOWS = "Windows"
LINUX = "Linux"

PLAT = platform.system().lower().capitalize()  # Determine the platform
YUZU_DIR = Path.cwd()  # The current working directory


URL = ""
ASSET_VERSION = 0
CURRENT_VERSION = None


def main():
    if (PLAT == WINDOWS or PLAT == LINUX):
        global URL
        global ASSET_VERSION

        setCurrentVersion()

        # Set up the URL
        github_url = "https://api.github.com/repos/pineappleEA/pineapple-src/releases/latest"
        # Download the JSON from the GitHub API for the latest release
        try:
            with urllib.request.urlopen(github_url) as response:
                data = response.read().decode()
        except Exception as e:
            print(f"Failed to connect to GitHub API: {e}")
            launchYuzu()

        release = json.loads(data)

        # Look for the asset for our platform in the release assets
        for asset in release["assets"]:
            if PLAT in asset["name"]:
                asset_name = asset["name"]
                break
        else:
            print("No compatible release found")
            launchYuzu()

        ASSET_VERSION = re.search(r'EA-(\d+)', asset_name).group(1)
        URL = asset["browser_download_url"]

        if (not CURRENT_VERSION or ASSET_VERSION > CURRENT_VERSION):
            print("New version available, updating...")
            readyFiles(asset_name)

        # Start the Yuzu emulator
        launchYuzu()
    else:
        print(f"{PLAT} is unsupported. Goodbye.")


def launchYuzu():
    try:
        print(f"Launching Yuzu...")
        if PLAT == WINDOWS:
            exe_path = YUZU_DIR / CURRENT_EXE
            if os.path.isfile(exe_path):
                subprocess.Popen([str(exe_path)])
            else:
                print(f"File {exe_path} not found.")
        else:
            appimage_path = YUZU_DIR / CURRENT_APPIMAGE
            if os.path.isfile(appimage_path):
                subprocess.Popen([str(appimage_path)])
            else:
                print(f"File {appimage_path} not found.")
    except FileNotFoundError:
        print("File not found.")
    except PermissionError:
        print("You do not have permission to execute the file.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")


def readyFiles(asset_name):
    download_file(asset_name)

    if PLAT == WINDOWS:
        # Get a list of all files and directories in the current directory
        files = os.listdir(YUZU_DIR)

        # Go through the list and delete each item, except for the script itself
        for item in files:
            if item != os.path.basename(__file__) and item != asset_name:
                item_path = YUZU_DIR / item
                if os.path.isfile(item_path):
                    os.remove(item_path)
                elif os.path.isdir(item_path):
                    shutil.rmtree(item_path)

        unzip(asset_name)
    else:
        st = os.stat(YUZU_DIR / asset_name)
        os.chmod(YUZU_DIR / asset_name, st.st_mode | stat.S_IEXEC)
        write_version(ASSET_VERSION)


def unzip(asset_name):
    zip_path = YUZU_DIR / asset_name
    try:
        with zipfile.ZipFile(zip_path, 'r') as zip_ref:
            print(f"Extracting...")
            files = zip_ref.infolist()
            total_files = len(files)
            for i, member in enumerate(files, start=1):
                # Remove the first directory in the file path
                parts = member.filename.split('/')
                if len(parts) > 1:
                    member.filename = '/'.join(parts[1:])
                    # Extract the file/directory
                    zip_ref.extract(member, YUZU_DIR)
                # Print progress bar
                print('\r[{0}] {1}%'.format(
                    '#'*(i*50//total_files), i*100//total_files), end='')
            print()  # End the line for the progress bar
    except FileNotFoundError:
        print(f"Zip file {asset_name} not found.")
        exit()
    except zipfile.BadZipFile:
        print(
            f"The file at {asset_name} is either not a valid zip file or it is corrupted. Initiating re-download.")
        os.remove(zip_path)
        readyFiles(asset_name)
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        exit()
    else:
        try:
            # Delete the zip file after extraction
            os.remove(zip_path)
        except OSError:
            print(f"Unable to delete zip file {asset_name}.")
        except Exception as e:
            print(f"An unexpected error occurred: {e}")


def setCurrentVersion():
    global CURRENT_VERSION
    if PLAT == WINDOWS and os.path.exists(CURRENT_EXE):
        with open(CURRENT_EXE, 'rb') as f:
            content = f.read().decode(errors='ignore')
        match = re.search(r'yuzu Early Access', content)
        if match:
            start = max(0, match.start() - 20)
            current_version = content[start:match.start()].replace('\0', '')
            if current_version.startswith("0"):
                current_version = current_version[1:]
            print("Yuzu EA version found : EA-" + current_version)
            CURRENT_VERSION = current_version
    elif PLAT == LINUX and os.path.exists(YUZU_VERSION_FILE):
        current_version = read_version()
        print("Yuzu EA version found : EA-" + current_version)
        CURRENT_VERSION = current_version


def write_version(version):
    with open(YUZU_VERSION_FILE, "w") as f:
        f.write(version)


def read_version():
    with open(YUZU_VERSION_FILE, "r") as f:
        return f.read().strip()


def download_file(asset_name):
    file_path = YUZU_DIR / asset_name
    filename = CURRENT_APPIMAGE if PLAT == LINUX else asset_name
    if not os.path.isfile(file_path):
        response = urllib.request.urlopen(URL)

        # Get the total file size
        file_size = int(response.getheader('Content-Length'))

        # Create the file on disk and start writing to it
        with open(YUZU_DIR / filename, 'wb') as f:
            print(f"Downloading {filename}...")
            downloaded = 0
            block_size = 8192  # The size of each block to download
            while True:
                buffer = response.read(block_size)
                if not buffer:  # If there's no more data to read, we're done
                    break
                # Increase the amount of data we've downloaded
                downloaded += len(buffer)
                f.write(buffer)

                # Print the progress bar
                percent_downloaded = downloaded / file_size
                progress_bar_width = 50  # How wide the progress bar will be, in characters
                num_hashes = math.floor(
                    percent_downloaded * progress_bar_width)
                print('\r[{}{}] {:.2f}%'.format('#' * num_hashes, ' ' *
                                                (progress_bar_width - num_hashes), percent_downloaded * 100), end='')

            print()  # Print a newline at the end to clean up the output


if __name__ == "__main__":
    main()

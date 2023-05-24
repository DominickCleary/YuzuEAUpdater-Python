# Yuzu Updater Script

A lightweight, fast, and unobtrusive Python 3 script designed to keep your Yuzu emulator up-to-date on Windows and Linux platforms. Yuzu is a popular open-source emulator for the Nintendo Switch. This script ensures you're always using the latest version with no additional dependencies.

## Features

- **Automatic Version Checking**: Compares your Yuzu version with the latest from the PineappleEA's GitHub repository, initiating an update if needed.
- **Platform Compatibility**: Supports both Windows and Linux.
- **File Cleanup**: Maintains a clean directory by removing outdated files during the update process.
- **Zero Dependencies**: Requires only Python 3 to run, with no additional libraries or modules.
- **Easy Execution**: Simply run the script in your Yuzu directory. The script will handle the rest, launching Yuzu post-update.

## Usage
For Windows users:

- Run the script in your Yuzu directory. On Windows, use a dedicated directory for the script as it clears all other files and directories (except itself) during the update process.

For Linux users:

- Ensure that your Yuzu emulator executable is named 'yuzu.AppImage'.
- The script also requires the presence of a '.yuzuversion' file in the directory with the emulator. This file is used to keep track of the current version.

This script requires Python 3 to run.

Please note that the script does not have a rollback feature. If a new version of the emulator introduces issues, you will have to manually revert to a previous version.

## Steam Deck Compatibility

While the script is expected to function with the Steam Deck's Linux environment, it is yet to be tested. Feedback from Steam Deck users is greatly appreciated!

## Credit

The Yuzu emulator is a product of the [Yuzu team](https://yuzu-emu.org/). The PineappleEA's repository, which this script utilizes, compiles the latest Yuzu builds. All credit for the emulator itself goes to the Yuzu team, and the compiled builds are provided by PineappleEA.

## Disclaimer

This script is provided as-is, and the authors take no responsibility for any issues that may arise from its use. Always back up your files before running scripts like this one. Also, ensure that you have a stable internet connection for the script to run effectively.

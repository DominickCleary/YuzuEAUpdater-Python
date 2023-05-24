# Yuzu Updater Script

A lightweight, fast, and unobtrusive Python 3 script designed to keep your Yuzu emulator up-to-date on Windows and Linux platforms. Yuzu is a popular open-source emulator for the Nintendo Switch. This script ensures you're always using the latest version with no additional dependencies.

## Features

- **Automatic Version Checking**: Compares your Yuzu version with the latest from the PineappleEA's GitHub repository, initiating an update if needed.
- **Platform Compatibility**: Supports both Windows and Linux.
- **File Cleanup**: Maintains a clean directory by removing outdated files during the update process.
- **Zero Dependencies**: Requires only Python 3 to run, with no additional libraries or modules.
- **Easy Execution**: Simply run the script in your Yuzu directory. The script will handle the rest, launching Yuzu post-update.

## Usage

This script requires Python 3 to run. To use it:

1. Ensure that your Yuzu emulator executable is named 'yuzu.AppImage' on Linux platforms.
2. On Linux, the script also requires the presence of a '.yuzuversion' file in the directory with the emulator. This file is used to keep track of the current version.
3. Run the script in the directory where your Yuzu emulator is located. On Windows, make sure that the script is in its own dedicated directory as it will delete all other files and directories (except itself) in its running directory during the update process.
4. The script will check for updates from the [PineappleEA's repository](https://github.com/pineappleEA/pineapple-src). If an update is available, it will be automatically downloaded and installed. Afterward, the Yuzu emulator will be launched.

Please note that the script does not have a rollback feature. If a new version of the emulator introduces issues, you will have to manually revert to a previous version.

## Credit

The Yuzu emulator is a product of the [Yuzu team](https://yuzu-emu.org/). The PineappleEA's repository, which this script utilizes, compiles the latest Yuzu builds. All credit for the emulator itself goes to the Yuzu team, and the compiled builds are provided by PineappleEA.

## Disclaimer

This script is provided as-is, and the authors take no responsibility for any issues that may arise from its use. Always back up your files before running scripts like this one. Also, ensure that you have a stable internet connection for the script to run effectively.



# Yuzu Updater Script

This script is designed to keep your Yuzu emulator up-to-date on Windows and Linux platforms. Yuzu is a popular open-source emulator for the Nintendo Switch, and this script makes it easy to ensure you're always using the latest version.

## Features

- Automatic version checking: The script checks the current version of your Yuzu emulator against the latest release available on the PineappleEA's GitHub repository. If a newer version is available, the script will automatically download it.
- Platform compatibility: The script supports both Windows and Linux platforms, recognizing the appropriate executable for each.
- File cleanup: The script will clean up outdated files, keeping your directory tidy.
- Error handling: The script includes robust error handling, ensuring it doesn't fail silently and provides helpful feedback.
- Progress visualization: The script provides a progress bar for both download and extraction processes, so you can see at a glance how far along the update process is.
- Easy execution: Simply run the script in the directory where your Yuzu emulator is located. If an update is available, it will be automatically downloaded and installed. Afterward, the Yuzu emulator will be launched.

## Usage

This script requires Python 3 to run. To use it:

1. Ensure that your Yuzu emulator executable is named 'yuzu.AppImage' on Linux platforms.
2. On Linux, the script also requires the presence of a '.yuzuversion' file in the directory with the emulator. This file is used to keep track of the current version.
3. Run the script in the directory where your Yuzu emulator is located. On Windows, make sure that the script is in its own dedicated directory as it will delete all other files and directories (except itself) in its running directory during the update process.
4. The script will check for updates from the [PineappleEA's repository](https://github.com/pineappleEA/pineapple-src). If an update is available, it will be automatically downloaded and installed. Afterward, the Yuzu emulator will be launched.

Please note that the script does not have a rollback feature. If a new version of the emulator introduces issues, you will have to manually revert to a previous version.

## Credit

The Yuzu emulator is developed and maintained by the team at [Yuzu](https://yuzu-emu.org/). The PineappleEA's repository compiles the latest builds of the Yuzu emulator. This script uses the latest releases from the PineappleEA's GitHub repository to provide automatic updates. All credit for the emulator itself goes to the authors at Yuzu, and the compiled builds are courtesy of PineappleEA.

## Disclaimer

This script is provided as-is, and the authors take no responsibility for any issues that may arise from its use. Always back up your files before running scripts like this one. Also, ensure that you have a stable internet connection for the script to run effectively.

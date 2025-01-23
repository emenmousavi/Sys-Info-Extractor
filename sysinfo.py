import sys
import subprocess
import os

def print_intro():
    print("="*50)
    print("Welcome to Sys-Info-Extractor!")
    print("Created by: Emen Mousavi")
    print("="*50)
    print("What this tool does:")
    print("  - Shows the programs installed on Windows")
    print("  - Lists the running processes on Linux")
    print("  - Shows the Python packages installed")
    print("="*50)
    print("Let's get started!")
    print("="*50)

def get_installed_programs_windows():
    installed_programs = []
    registry_path = r"SOFTWARE\Microsoft\Windows\CurrentVersion\Uninstall"

    try:
        import winreg
        with winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE, registry_path) as key:
            for i in range(0, winreg.QueryInfoKey(key)[0]):
                subkey_name = winreg.EnumKey(key, i)
                subkey = winreg.OpenKey(key, subkey_name)

                try:
                    program_name = winreg.QueryValueEx(subkey, "DisplayName")[0]
                    installed_programs.append(program_name)
                except FileNotFoundError:
                    continue
        return installed_programs
    except ImportError:
        print("This tool works only on Windows. Make sure the 'winreg' module is available.")
        return []

def get_running_processes_linux():
    try:
        result = subprocess.run(['ps', '-aux'], capture_output=True, text=True)
        processes = result.stdout.splitlines()
        return processes
    except Exception as e:
        print(f"Error while retrieving processes: {e}")
        return []

def get_installed_python_packages():
    try:
        result = subprocess.run(['pip', 'list'], capture_output=True, text=True)
        packages = result.stdout.splitlines()
        return packages
    except Exception as e:
        print(f"Error while retrieving Python packages: {e}")
        return []

def main():
    print_intro()

    current_directory = os.getcwd()
    print(f"Running this tool from: {current_directory}")

    if sys.platform == 'win32':
        print("Checking installed programs on Windows...")
        programs = get_installed_programs_windows()
        if programs:
            print("Here are the installed programs on your system:")
            for program in programs:
                print(program)
        else:
            print("No programs found or could not access the program list.")
    
    elif sys.platform == 'linux' or sys.platform == 'linux2':
        print("Checking running processes on Linux...")
        processes = get_running_processes_linux()
        if processes:
            print("Here are the processes currently running on your system:")
            for process in processes:
                print(process)
        else:
            print("No processes found.")
    
    else:
        print("Sorry, this tool only works on Windows and Linux systems.")

if __name__ == "__main__":
    main()

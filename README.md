
# Sys-Info-Extractor
## Created by: Emen Mousavi

### Description:
Sys-Info-Extractor is a simple tool designed to extract system information. It works on both Windows and Linux systems, including Kali Linux. It retrieves installed programs, running processes, and installed Python packages.

### Features:
- Displays installed programs on Windows.
- Lists running processes on Linux.
- Shows the installed Python packages.

### Prerequisites:
- Python 3.x installed on your system.
- Linux or Windows for full functionality.

### Installation in Linux:
1. Clone the repository or download the Python script:
   ```bash
   git clone https://github.com/yourusername/sys-info-extractor.git
   ```
2. Install any missing dependencies using pip:
   ```bash
   pip install -r requirements.txt
   ```
3. For Windows, ensure `winreg` is available.
4. For Linux, make sure you have `ps` command and Python installed.

### Usage in Linux:
1. Navigate to the directory containing the script.
2. Run the script:
   ```bash
   python sysinfo.py
   ```
3. The tool will automatically check your OS and provide the relevant information.

### Usage in Windows:
1. Run the .exe file.
2. Open the TXT file to read all installed applications

### Output:
- For Windows: Outputs the installed programs inside a TXT file in the same folder you run the .exe file
- For Linux: Shows Running processes.
- Python packages will also be displayed.

### Contributing:
Feel free to fork the project, create a pull request, or open issues for any feature requests or bugs. Contributions are always welcome!

### License:
This project is open-source and free to use. You can modify and distribute it as per your needs.

# numHunter


Installation Guide for Phone Information Tool
This guide will help you download and set up the Phone Information Tool on different operating systems, including Windows, macOS, and Linux.

Prerequisites
Before installing the tool, ensure you have the following:

Python 3.x: Make sure Python 3 is installed on your system. You can download it from the official Python website.
Numverify API Key: Sign up for an account on Numverify to obtain your API key.
Installation Steps
For Windows
Download Python:

Visit the Python download page.
Download the latest version of Python 3.x and run the installer.
During installation, make sure to check the box that says “Add Python to PATH”.
Install Requests Library:

Open Command Prompt (search for "cmd" in the Start menu).
Run the following command to install the Requests library:
bash
Copier le code
pip install requests
Download the Tool:

Create a new directory where you want to store the tool (e.g., C:\PhoneInfoTool).
Open a text editor (like Notepad) and copy the Phone Information Tool code into a new file.
Save the file as phone_info.py in the directory you created.
Configuration:

Open phone_info.py in the text editor.
Replace YOUR_API_KEY with your actual Numverify API key.
Run the Tool:

Open Command Prompt and navigate to the directory where the script is saved:
bash
Copier le code
cd C:\PhoneInfoTool
Run the tool with the following command:
bash
Copier le code
python phone_info.py
For macOS
Download Python:

Visit the Python download page.
Download the latest version of Python 3.x and install it.
Install Requests Library:

Open Terminal (you can find it in Applications > Utilities).
Run the following command to install the Requests library:
bash
Copier le code
pip3 install requests
Download the Tool:

Create a new directory for the tool (e.g., ~/PhoneInfoTool).
Open a text editor (like TextEdit) and copy the Phone Information Tool code into a new file.
Save the file as phone_info.py in the directory you created.
Configuration:

Open phone_info.py in the text editor.
Replace YOUR_API_KEY with your actual Numverify API key.
Run the Tool:

Open Terminal and navigate to the directory where the script is saved:
bash
Copier le code
cd ~/PhoneInfoTool
Run the tool with the following command:
bash
Copier le code
python3 phone_info.py
For Linux
Download Python:

Most Linux distributions come with Python pre-installed. To check if Python 3 is installed, open Terminal and run:
bash
Copier le code
python3 --version
If it's not installed, you can install it using your package manager (e.g., for Ubuntu):
bash
Copier le code
sudo apt update
sudo apt install python3
Install Requests Library:

In Terminal, run the following command to install the Requests library:
bash
Copier le code
pip3 install requests
Download the Tool:

Create a new directory for the tool (e.g., ~/PhoneInfoTool):
bash
Copier le code
mkdir ~/PhoneInfoTool
Navigate to the new directory:
bash
Copier le code
cd ~/PhoneInfoTool
Open a text editor (like nano) and copy the Phone Information Tool code into a new file:
bash
Copier le code
nano phone_info.py
Save the file (in nano, press CTRL + O to save and CTRL + X to exit).
Configuration:

Open phone_info.py in the text editor again and replace YOUR_API_KEY with your actual Numverify API key.
Run the Tool:

In Terminal, run the tool with the following command:
bash
Copier le code
python3 phone_info.py

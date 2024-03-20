# How to set up (Visual Studio Code)

Step 1: Download latest version of Python

Step 2 (Visual Studio Code): Press Ctrl+Shift+P and type Python:Create Environments to select create .venv

Step 3 (Visual Studio Code): Select the Workspace and the latest Python version

Step 4 (Visual Studio Code): Choose the requirements.txt for dependecies to install

Step 5: Run "python ./Launch.py" while in the \app directory

# How to set up (Console)

Step 1: Download latest version of Python

Step 2 (Console): Create a .venv using "python -m venv .venv" command in the command prompt

Step 3 (Console): Type ".venv\Scripts\activate" to activate the environment

Step 4 (Console): Go into the app folder and run "py -m pip install -r requirements.txt" 

Step 5: Add .ignore file to .venv since it doesn't do it automatically

Step 6: Run "python ./Launch.py" while in the \app directory

# Making fakeData for testing

For testing try:

Step 1: Run "python ./Launch_test.py" while in the \app directory to check that everything's working

# Making fakeData for testing

If you want to use your own txt file of URLS drag it into the fakeData folder and rename it or change the file path in Launch.

NOTE: The URLS in the txt file must be separated, one url per line.

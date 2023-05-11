import os
import winreg

# Script Name: setup_maven_env_variables.py
# Description: Sets up the MAVEN_HOME and Path environment variables for a user account in Windows.
# Replace MAVEN_HOME with the path to the Maven directory on your system.

# Set the path to the Maven directory on your system
MAVEN_HOME = r"C:\maven"

# Set the MAVEN_HOME environment variable
os.environ["MAVEN_HOME"] = MAVEN_HOME

# Set the Path environment variable to include the Maven bin directory
path_key = winreg.OpenKey(winreg.HKEY_CURRENT_USER, "Environment", 0, winreg.KEY_ALL_ACCESS)
path_value, _ = winreg.QueryValueEx(path_key, "Path")
winreg.SetValueEx(path_key, "Path", 0, winreg.REG_EXPAND_SZ, f"{path_value};{MAVEN_HOME}\\bin")

# Notify the user that the configuration has been set
print("MAVEN_HOME and Path environment variables have been set.")
print("Please log out and log back in again for the changes to take effect.")

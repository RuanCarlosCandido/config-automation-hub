@echo off
REM Script Name: setup_maven_env_variables.bat
REM Description: Sets up the MAVEN_HOME and Path environment variables for a user account in Windows.
REM Replace MAVEN_HOME with the path to the Maven directory on your system.

REM Set the path to the Maven directory on your system
set "MAVEN_HOME=C:\maven"

REM Set the MAVEN_HOME environment variable
setx MAVEN_HOME "%MAVEN_HOME%" /m

REM Set the Path environment variable to include the Maven bin directory
set "PATH=%PATH%;%MAVEN_HOME%\bin%"
setx PATH "%PATH%" /m

REM Notify the user that the configuration has been set
echo MAVEN_HOME and Path environment variables have been set.
echo Please log out and log back in again for the changes to take effect.

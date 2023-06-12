#!/bin/bash

# Function to get project name from the root directory
get_project_name() {
    # Get current working directory's name
    basename "$(pwd)"
}

# Function to find the .war file
find_war() {
    # Search for .war file under target directory
    find . -path "./target/$(get_project_name)-*.war" -print -quit
}

# Set up WebLogic environment
source /opt/desenv/servers/wls12213/wlserver/server/bin/setWLSEnv.sh

# Define the .war file
war_file=$(find_war)

# Validate if war file is found
if [ -z "$war_file" ]
then
  echo "WAR file not found in the defined directory"
  exit 1
fi

# Start WebLogic Scripting Tool
java weblogic.WLST <<EOF

# Connect to the admin server
connect('weblogic', 'ADD_HERE_YOUR_PASSWORD', 't3://localhost:7001')

# Begin deployment
edit()
startEdit()

# Deploy .war file
cd('/')
appExists=getMBean('/AppDeployments/$(get_project_name)')

# Undeploy the application if it exists
if appExists:
    print 'Undeploying existing application...'
    undeploy('$(get_project_name)', targets='AdminServer')

# Deploy the new application
print 'Deploying new application...'
deploy('$(get_project_name)', '$war_file', targets='AdminServer')

# Save and activate changes
save()
activate(block="true")

# Disconnect from the admin server
disconnect()

# Exit WLST
exit()
EOF

#!/usr/bin/env python3

import fileinput
import sys
import os

# Define the paths to your Java installations
java_versions = {
    '8': '/opt/desenv/libs/jdk1.8.0_281',
    '11': '/usr/lib/jvm/java-11-openjdk-amd64',
    '17': '/usr/lib/jvm/java-17-openjdk-amd64',
    '18': '/usr/lib/jvm/java-18-openjdk-amd64',
}

def main():
    # Prompt the user for the desired Java version
    java_version = input('Enter the Java version you want to switch to (8, 11, 17 or 18): ')

    if java_version not in java_versions:
        print('Invalid Java version. Please enter 8, 11, 17 or 18.')
        sys.exit(1)

    # Edit the .bashrc file in-place
    with fileinput.FileInput(os.path.expanduser('~/.bashrc'), inplace=True) as f:
        for line in f:
            if 'export JAVA_HOME' in line:
                print('export JAVA_HOME={}'.format(java_versions[java_version]))
            else:
                print(line, end='')

if __name__ == '__main__':
    main()


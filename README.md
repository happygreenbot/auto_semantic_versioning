# Automatic semantic version
A simple utiity to automatically update semantic version numbers of your code everytime you make a commit. Uses a combination of git diff and pre-commit hooks.

## Installation instructions

Run the below setup script

`./setup.sh`

Use `git commit --no-verify` if you wish to skip the hook

## Working :

* Runs a git diff to see the changed number of lines.

* Based on the number of lines changed, the version update is either a **patch, minor or major** update, and the version number is updated accordingly.

## Note :

* Creates a directory **config** and writes version numbers to **version_info.py**. This can be changed as per requirement in the **setup.sh** file

## Requirements :
* python3

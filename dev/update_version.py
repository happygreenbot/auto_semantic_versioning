
import sys
import os
import re

def change_version(file_name, code_changes):
	with open(file_name, "r+") as file:
		#read the file contents
		file_contents = file.read()
		#print(file_contents)
		text_pattern = re.compile('version = ".*"', 0)
		previous_version_number = text_pattern.search(file_contents).group().split('"')[1]
		#previous_version_number = "0.0.0"
		major, minor, patch = previous_version_number.split(".")

		matches = 0
		for line in code_changes:
			matches = matches + len(re.findall(r"\+\+\+", line))
		print("Line changes : " + str(matches))

		if matches<2:
			update_type = "patch"
		elif matches<5:
			update_type = "minor"
		else:
			update_type = "major"
		
		if update_type == "patch":
			patch = str(int(patch) + 1)
		elif update_type == "minor":
			patch = "0"
			minor = str(int(minor) + 1)
		elif update_type == "major":
			patch = "0"
			minor = "0"
			major = str(int(major) + 1)
		else:
			print("Unkown update type")
		new_version_number = ".".join([major, minor, patch])
		subs = "version = \"" + new_version_number + "\""
		file_contents = text_pattern.sub(subs, file_contents)
		file.seek(0)
		file.truncate()
		file.write(file_contents)

print("Working dir: " + os.getcwd())
version_file = "config/config.py"

code_changes = sys.stdin.readlines()
print(code_changes)

change_version(version_file, code_changes)

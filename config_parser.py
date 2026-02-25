import json

class config_Parser_Error(Exception):
    pass
# Step 1 – Create a config file
# Create:
# config.txt OR config.json
# Step 2 – Create a main parser function
# It should:
# Accept file path
# Detect file type
# Read file
# Return dictionary
# Step 3 – Create validation function
# This should:
# Accept dictionary
# Validate required fields
# Validate types
# Validate ranges
# Raise errors if invalid
# Step 4 – Add proper exception handling
# Handle:
# FileNotFoundError
# JSONDecodeError (if using json
# ValueError
# Custom errors (optional)
# Step 5 – Clean Output
# If everything is correct:
# Print "Configuration loaded successfully"
# Return usable config dictionary
config = {}
try:
    with open("config.json", "r") as file:
        for line in file:
            if line.startswith("{") or line.endswith("}"):
                continue
            if line.strip():                      #strip() returns the string so if line.strip = "" it will be false
                print(line.strip())
                key, value = line.strip().split(":")
                config[key] = value
            else:
                raise config_Parser_Error("Invalid line format, Moving to next line")
                continue
except FileNotFoundError:
    print("File not found")
except Exception as e:
    print(e)

print(config)
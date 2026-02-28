import json
import os
import pathlib


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

def parser(file_path):
    config = {}
    try:
        checker =str(pathlib.Path(file_path).parent.resolve())
        if(checker in file_path):    # left operand should be string so we converted it to string
            file_name = os.path.basename(file_path)   #gets the file name from the path itself
            # print(file_name)
            with open(file_name, "r") as file:
                for line in file:
                    if line.startswith("{") or line.endswith("}"):
                        continue
                    if line.strip():                      #strip() returns the string so if line.strip = "" it will be false
                        # print(line.replace('"','').replace(",","").replace(" ","").strip())
                        key, value = line.replace('"','').replace(",","").replace(" ","").strip().split(":")
                        config[key] = value
            print(config)
            return config
        else:
            raise config_Parser_Error("Path exist but File doesn't")
    except FileNotFoundError:
        print("File not found")
    except Exception as e:
        print(e)


# Step 3 – Create validation function
# This should:
# Accept dictionary
# Validate required fields
# Validate types
# Validate ranges
# Raise errors if invalid

def validate_config(config):
    required_fields = ["host", "port", "debug", "timeout"]
    
    # Check required fields
    for field in required_fields:
        if field not in config:
            raise ValueError(f"Missing required field: {field}")
    
    # Validate types
    if not isinstance(config["host"], str):
        raise TypeError("host must be a string")
    

    if not isinstance(config["port"], int) or not int(config["port"]) <= 65535:
        print(type(config["port"]))
        raise ValueError("port must be an integer between 1024 and 65535")
    
    if not isinstance(config["debug"], bool):
        raise TypeError("debug must be a boolean")
    
    if not isinstance(config["timeout"], (int, float)) or config["timeout"] <= 0:
        raise ValueError("timeout must be a positive number")
    
    return True



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


config_checker = parser("D:\\Moltbot\\config.json")

print(type(config_checker))
if validate_config(config_checker): 
    print("Configuration loaded successfully")


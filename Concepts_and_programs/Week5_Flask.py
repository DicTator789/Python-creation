#Understanding flask at depth




#python d:/Moltbot/Python-creation/Concepts_and_programs/Week5.py     run like this oior first activate virtual environments .\.venv\Scripts\Activate.ps1
import json
from logging import debug
from flask import Flask,jsonify,send_file
from flask import request



app = Flask(__name__)  #creates an web server or app

@app.route('/')   # route to function when one goes to http://localhost:5000/ 
def home():
    return "server is running and all looks good!"   # response to the client
    # return {"status" : "healthy"}       # returning json


#excercise 1
@app.route('/home')
def real_home():
    return "Hi there You are in Home page"

@app.route('/home/<name>')   # you can give name in the url then it will execute this function like post method
def named_home(name):
    return f"Hi {name}, Welcome"


#handling json   -- exc 2
@app.route('/health')
def health():
    # return {"status": "ok", "port": 80},200
    return jsonify({
        "status": "Healthy",
        "Port" : 80
    })

#handling json files  
@app.route('/config')
def get_config():                                                                       
    # return {"status": "ok", "port": 80},200
    with open('config.json') as f:
        data = json.load(f)
    return data


    #OR


#handing json through file 
@app.route('/config-file')
def get_config_file():                                                               ## dont name the function same  or just change the endpoint in the app.route :: @app.route('/config-file', endpoint='config_file')
    return send_file('d:\\Moltbot\\config.json')
    
@app.route('/config-file2',endpoint='config_file')
def get_config_file():                                                               ## dont name the function same  or just change the endpoint in the app.route :: @app.route('/config-file', endpoint='config_file')
    return send_file('d:\\Moltbot\\config.json')


#handing user input ===== exc 3
@app.route('/greet')                                                 #/greet?name=Rohit
def greet():
    name = request.args.get('name','Guest')
    return f"hello {name}"


#Post request(Important)
@app.route('/add', methods=['POST'])
def add():
    data = request.get_json()
    a = data['a']
    b = data['b']
    return {"result": a + b }

@app.route('/add2', methods=['POST'], endpoint='add_json') # endpoint is different but Flask does NOT use endpoint to match incoming request
def add_json():
    data = request.get_json()
    return {"host": data['host'],
    "port": data['port'],
    "debug": data['debug'],
    "timeout": data['timeout']}

@app.route('/divide', methods=['POST'])
def divide():
    data = request.get_json()
    
    try:
        a = data['a']
        b = data['b']
        result = data['a'] / data['b']
    except ZeroDivisionError:
        return {"error": "Division by zero is not allowed"}, 400
    except KeyError:
        return {"error": "Missing 'a' or 'b' in request body"}, 400
    return {"result": result}



#excercise 4
@app.route('/hello')
def hello():
    return "Hello, World!"

#excercise 5
@app.route('/square_post/<int:num>', methods=['POST'])  # given in postman body then it will execute this function like post method
def square_post(num):
    result = num ** 2
    return {"result": result}

@app.route('/square_get/<int:num>')    #get request method by default : given in the url then it will execute this function like post method
def square_get (num):
    result = num ** 2
    return {"result": result}

@app.route('/square_Original')    #http://127.0.0.1:5000/square_Original?num=4
def square_original():
    num = request.args.get('num', type=int)  
    return {"result": num**2}

@app.route('/iseven')    #get request method by default : given in the url then it will execute this function like post method
def iseven():
    num = request.args.get('num', type=int)
    if num is None:
        return {"error": "Missing 'num' query parameter"}, 400
    
    result = (num % 2 == 0)   # if num is even then it will return true otherwise false
    return "No is Prime" if result else "No is not Prime"


#ADV LEVEL
#1.sum of numbers
@app.route('/sum_numbers', methods=['POST'])
def sum_numbers():
    data = request.get_json()     #data = {"numbers": [1, 2, 3]}
    # numbers = data['numbers']   # works but If "numbers" is missing → ❌ CRASH (KeyError) if numbers is not there in postman body then it will crash the server and we have to handle that error and return proper response to the client
    numbers = data.get('numbers')   # When you receive JSON, it becomes a Python dictionary. If "numbers" exists → ✅ returns valueIf missing → ✅ returns None (no crash)

    if not numbers or not isinstance(numbers, list) or not all(isinstance(n, (int, float)) for n in numbers):   #isinstance([1, 2, 3], list)   # True isinstance("123", list)       # False isinstance(123, list)         # False
        return {"error": "Missing or invalid 'numbers' in request body"}, 400
    result = sum(numbers)
    return {"result": result}   

#2. max of numbers
@app.route('/max_number', methods=['POST'])
def max_number():
    data = request.get_json()
    numbers = data.get('numbers')
    if not numbers or not isinstance(numbers, list) or not all(isinstance(n, (int, float)) for n in numbers):
        return{"error":"Missing or invalid 'numbers' in request body"}, 400
    result = max(numbers)
    return {"result": result}

#3. count of prime numbers
@app.route('/count_primes', methods=['POST'])
def count_primes():
    data = request.get_json()
    numbers = data.get('numbers')
    if not numbers or not isinstance(numbers, list) or not all(isinstance(n, (int, float)) for n in numbers):
        return {"error": "Missing or invalid 'numbers' in request body"}, 400
    
    prime_count = sum(1 for num in numbers if is_prime(num))
    return {"prime_count": prime_count}

#4.count of total numbers in list
@app.route('/count_numbers', methods=['POST'])
def count_numbers():
    data = request.get_json()
    numbers = data.get('numbers')
    if not numbers or not isinstance(numbers, list) or not all(isinstance(n, (int, float)) for n in numbers): #isinstance(5, (int, float)) → True ||isinstance(3.2, (int, float) → True ||isinstance("a", (int, float))→ False
        return {"error": "Missing or invalid 'numbers' in request body"}, 400
    
    count = len(numbers)
    return {"count": count}
#5. user and its dynamic route
@app.route('/user/<username>')
def user(username):
    return f"Welcome to {username}'s profile page!"


#calculator
@app.route('/calculator', methods=['POST'])
def calculator():
    data = request.get_json()
    operation = data.get('operation')
    a = data.get('a')
    b = data.get('b')
    if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
        return {"error": "Missing 'a' or 'b' in request body"}, 400
    if operation == 'add':
        result = a + b
    elif operation == 'subtract':
        result = a - b
    elif operation == 'multiply':
        result = a * b
    elif operation == 'divide':
        if b == 0:
            return {"error": "Division by zero is not allowed"}, 400
        result = a / b
    else:
        return {"error": "Invalid operation"}, 400

    return {"result": result}

if __name__ == '__main__':    # this file is the starting point of execution  ::  THIS WILL ONLY RUN WHEN EXECUTED DIRECLTY IF I EXECUTE THIS FILE VIA OTHER FILE THEN THE FUNCTION WILL NOT EXECUTE
                              # run the server only when the file is executed directly (if i put app in place of __Main__ then i have to import app file and then i can execute this with app file)
    app.run(debug=True)   #Auto-restart on changes     Shows errors in browser (very useful for learning)


print("this will always execute")

# 🔹 GitHub Copilot → Terraform, Bash, Python - writes 40% of my code.

# 🔹 Claude → Architecture reviews, debugging complex issues.

# 🔹 ChatGPT → Documentation, runbooks, incident postmortems.

# 🔹 Cursor → When I need to refactor entire codebases.

# 🔹 Amazon Q → AWS-specific troubleshooting

# 🔹 k8sgpt → Finds Kubernetes cluster issues in seconds
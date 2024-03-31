import os
import sqlite3
import cgi
import pickle
from flask import Flask, request
from flask import Flask, request, session
from flask import Flask, redirect, request

# Bug 1: Division by zero
a = 10
b = 0
result = a / b
print(result)

# Bug 2: Index out of range
my_list = [1, 2, 3]
print(my_list[3])

# Bug 3: NameError - variable not defined
print(undefined_variable)

# Bug 4: Type mismatch
x = "5"
y = 2
result = x + y
print(result)

# Bug 5: NameError - variable not defined
print(undefined_variable)

# Bug 6: SyntaxError - missing colon
if True:
    print("Missing colon!")

# Bug 7: AttributeError - method not found
my_string = "Hello, World!"
print(my_string.uppercase())

# Bug 8: Logic error
a = 5
b = 10
if a > b:
    print("a is greater than b")
else:
    print("b is greater than a")

    # Bug 9: Command Injection

    user_input = input("Enter a file name: ")
    os.system("cat " + user_input)

    # Bug 10: SQL Injection

    user_input = input("Enter a username: ")
    conn = sqlite3.connect("mydatabase.db")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM users WHERE username = '" + user_input + "'")
    results = cursor.fetchall()
    for row in results:
        print(row)

    # Bug 11: Cross-Site Scripting (XSS)

    user_input = input("Enter your name: ")
    print("Hello, " + cgi.escape(user_input))

    # Bug 12: Insecure Deserialization

    user_input = input("Enter a serialized object: ")
    obj = pickle.loads(user_input)
    print(obj)

    # Bug 13: Insecure File Upload

    app = Flask(__name__)

    @app.route("/upload", methods=["POST"])
    def upload_file():
        file = request.files["file"]
        file.save("/path/to/uploads/" + file.filename)
        return "File uploaded successfully!"

    # Bug 14: Cross-Site Request Forgery (CSRF)

    app = Flask(__name__)
    app.secret_key = "mysecretkey"

    @app.route("/transfer", methods=["POST"])
    def transfer_money():
        amount = request.form["amount"]
        recipient = request.form["recipient"]
        # Transfer money logic here
        return "Money transferred successfully!"

    # Bug 15: Unvalidated Redirects and Forwards

    app = Flask(__name__)

    @app.route("/redirect", methods=["GET"])
    def redirect_to_url():
        url = request.args.get("url")
        return redirect(url)
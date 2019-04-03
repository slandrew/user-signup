from flask import Flask, request, redirect, render_template
import cgi
import os

app = Flask(__name__)
app.config['DEBUG'] = True

def valid_email(email):
    if len(email) < 3 or len(email) > 20:
        return False
    num_at = 0
    num_period = 0
    for char in email:
        if char == '@':
            num_at += 1
        if char == '.':
            num_period += 1
    if num_at != 1 or num_period != 1:
        return False
    return True

@app.route("/")
def index():
    return render_template('signup_page.html')

@app.route("/authenticate", methods=['POST'])
def validate():
    username = request.form['username']
    password1 = request.form['password1']
    password2 = request.form['password2']
    email = request.form['email']

    if not username:
        error = "Please enter a username."
        return render_template('signup_page.html', username_error=error, username=username, email=email)
    
    if not password1:
        error = "Please enter a password."
        return render_template('signup_page.html', password_error=error, username=username, email=email)

    if not password2:
        error = "Please confirm password."
        return render_template('signup_page.html', password_error=error, username=username, email=email)

    for char in username:
        if not char.isalpha() and not char.isdigit() or len(username) < 3 or len(username) > 20:
            error = "Please enter a username between 3 and 20 characters. No special characters allowed."
            return render_template('signup_page.html', username_error=error, username=username, email=email)

    for char in password1:
        if not char.isalpha() and not char.isdigit() or len(password1) < 3 or len(password1) > 20:
            error = "Please enter a password between 3 and 20 characters. No special characters allowed."
            return render_template('signup_page.html', password_error=error, username=username, email=email)

    if password1 != password2:
        error = "Password mismatch. Please try again."
        return render_template('signup_page.html', password_error=error, username=username, email=email)

    if not valid_email(email):
        error = "Please enter a valid email address."
        return render_template('signup_page.html', email_error=error, username=username, email=email)



    return redirect('/welcome?username={0}'.format(username))

@app.route('/welcome', methods=['POST', 'GET'])
def welcome():
    username = request.args.get('username')
    return render_template('welcome.html', username=username)

app.run()
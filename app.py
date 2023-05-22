from flask import Flask, redirect, render_template, request, session, url_for, flash
app = Flask(__name__)
import pandas as pd


users = {}
users["admin"] = "admin"
app = Flask(__name__)
app.secret_key = 'qwertyuiop1234567890'
global df

@app.route('/logout')
def logout():
    session.clear()
    flash('You have been logged out')
    return redirect(url_for('login'))

# Route for the login page
@app.route('/', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        if username in users and users[username] == password:
            # store the username in the session object
            session['username'] = username
            # redirect to the dashboard page
            return redirect(url_for('dashboard'))
        else:
            flash('Invalid username or password')
            return render_template('login.html')
    else:
        return render_template('login.html')

# Route for the dashboard page
@app.route('/index')
def dashboard():
    username = session['username']
    return render_template('index.html', username=username)

if __name__ == "__main__":
    app.run(debug=True)
from flask import Flask, Response, render_template, redirect, url_for, request,session
from database import connect
from datetime import datetime
import json

app = Flask(__name__)

#conn = connect.connect()
#cursor = conn.cursor()

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/register', methods = ["GET", "POST"])
def register():
    if request.method == "GET":
        return render_template('register.html')

    elif request.method == "POST":
        print(request.form)
        
        try:
            command = 'INSERT INTO regtable (firstname, middlename, lastname, gender, address_str, address_nr, postbox, city, email, password, account_created_at) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)'
            values = (request.form['firstname'],request.form['middlename'],request.form['lastname'],request.form['gender'],request.form['street'],
            request.form['HouseNr'],request.form['postbox'],request.form['city'],request.form['email'],request.form['psw'],datetime.now(),)
            cursor.execute(command, values)
            conn.commit()
            return redirect(url_for("regSuceed"))
        except Exception as error:
            print(error)
            return redirect(url_for("reg_reject_email"))
        
@app.route('/01')
def regSuceed():
    return render_template('register_s.html')

@app.route('/error')
def reg_reject_email():
    return render_template('register_uns_email.html')


@app.route('/login', methods = ["GET", "POST"])
def login():
    if request.method == "GET":
        return render_template('login.html')

    elif request.method == "POST":
        try:
            command = 'SELECT * FROM regtable WHERE email= %s'
            values = (request.form["email"],)
            cursor.execute(command,values)
            
            conn.commit()
            logged_user=cursor.fetchone()
            if (logged_user is None) or (logged_user["password"] != request.form["psw"]):
                return redirect(url_for("login_reject"))

            else:
                name = f'{logged_user["firstname"]} {logged_user["middlename"]} {logged_user["lastname"]}'
                return redirect(url_for("loginSuceed", name=name))

        except Exception as error:
            return render_template('login.html')

@app.route('/02')
def loginSuceed():
    return render_template('login_s.html', name=request.args.get('name'))
    
@app.route('/error')
def login_reject():
    return render_template('login_uns.html')


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=25000)
    

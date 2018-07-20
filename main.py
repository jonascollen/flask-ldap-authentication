from flask import Flask, render_template, request, redirect, session, url_for
# For LDAP-Authentication
import auth

app = Flask(__name__)

@app.route('/')
def home_page():

    # Checks cookie if user already have logged in
    if session.get('logged_in') == True:
        return ('Logged in!')
    else:
        # Sends to login page if not logged in
        return redirect(url_for('login_page'))
        
@app.route('/login', methods=['GET', 'POST'])
def login_page():
    if request.method == 'POST':

        username = request.form['username']
        password = request.form['password']

        if username != "" and password != "":
            # Validate user via LDAP-servers
            results = auth.authenticate(username, password)
            if results == 'OK':
                session['username'] = username
                session['logged_in'] = True
                return redirect(url_for('home_page'))
            else:
                failed = 'Invalid Credentials. Please try again.'
                return render_template('login.html', failed=failed)
        else:
            failed = 'You need to provide both username & password!'
            return render_template('login.html', failed=failed)
    else:
        failed = ""
        return render_template('login.html', failed=failed)


if __name__ == "__main__":
    app.run()

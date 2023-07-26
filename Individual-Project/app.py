from flask import Flask, render_template, request, redirect, url_for, flash
from flask import session as login_session
import pyrebase

config = {'apiKey': "AIzaSyAV4nP0Aw0CvO-ZSHq72-4d521IRimIh6M",
  'authDomain': "joelle-project-268cc.firebaseapp.com",
  'projectId': "joelle-project-268cc",
  'storageBucket': "joelle-project-268cc.appspot.com",
  'messagingSenderId': "782530638490",
  'appId': "1:782530638490:web:84c3485f302ef175ae6523",
  "databaseURL": ""}


firebase = pyrebase.initialize_app(config)
auth = firebase.auth()


app = Flask(__name__, template_folder='templates', static_folder='static')
app.config['SECRET_KEY'] = 'super-secret-key'

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/form', methods=['GET', 'POST'])
def form():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']
        age = int(request.form['age'])
        try:
            login_session['user'] = auth.create_user_with_email_and_password(email, password)
            UID = login_session['user']['localId']
            user = {"age":age, "email": email,"password":password}
            db.child("User").child(UID).set(user)
            
            if age <= 0 or not email or not password:
                error_msg = "Error, please try again, make sure that your age is bigger than 0, and that you enter your name and your last name, thank you!"
                return render_template('form.html', error_msg=error_msg)
            elif age >= 18:
                return redirect('/adult')
            else:
                return redirect('/minor')
        except:
            return 'submiting failed'
    return render_template('form.html')
@app.route('/minor')
def minor():
    return render_template('minor.html')
@app.route('/information')
def information():
    return render_template('information.html')
@app.route('/adult')
def adult():
    return render_template('adult.html')

@app.route('/family')
def family():
    return render_template('family.html')

@app.route('/parents')
def parents():
    return render_template('parents.html')

@app.route('/school')
def school():
    return render_template('school.html')

@app.route('/work')
def work():
    return render_template('work.html')

@app.route('/college')
def college():
    return render_template('college.html')

@app.route('/aboutus')
def aboutus():
    return render_template('aboutus.html')



if __name__ == '__main__':
    app.run(debug=True)
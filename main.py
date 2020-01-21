from flask import Flask, render_template, request
from flask_mail import Message, Mail

app = Flask(__name__)
mail = Mail(app)

app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 465
app.config['MAIL_USERNAME'] = '**********'
app.config['MAIL_PASSWORD'] = '**********'
app.config['MAIL_USE_TLS'] = False
app.config['MAIL_USE_SSL'] = True


mail = Mail(app)


@app.route('/')
def home():
    return render_template('home.html')


@app.route('/submit/', methods=['POST'])
def submit():
    email = str(request.form["send_mail"])
    print('Email is: ' + email)
    recipient = list()
    recipient.append(email)
    print(recipient)
    msg = Message('Noesis 6.0', recipients=recipient, sender='visionmanitbhopal@gmail.com')
    msg.body = request.form["email_body"]
    mail.send(msg)
    return 'Mail Sent!'


if __name__ == '__main__':
    app.run(debug=True)

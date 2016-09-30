from flask import Flask, render_template, request, flash
from forms import ContactForm
from flask_mail import Mail, Message


app = Flask (__name__)
mail = Mail()
app.secret_key = 'forrealthings'


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/about')
def about():
    return render_template('about.html')


@app.route('/contact', methods=['GET', 'POST'])
def contact():
    form = ContactForm()

    if request.method == 'POST':
        if form.validate() == False:
            flash('All fields are required.')
            return render_template('contact.html', form=form)
        else:
            msg = Message(form.subject.data, sender='contact@example.com', recipients=['hillaryksure@gmail.com'])
            msg.body = """
      From: %s &lt;%s&gt;
      %s
      """ % (form.name.data, form.email.data, form.message.data)
            mail.send(msg)

            return render_template('contact.html', success=True)

    elif request.method == 'GET':
        return render_template('contact.html', form=form)

app.config["MAIL_SERVER"] = "smtp.gmail.com"
app.config["MAIL_PORT"] = 465
app.config["MAIL_USE_SSL"] = True
app.config["MAIL_USERNAME"] = 'hillaryksure@gmail.com'
app.config["MAIL_PASSWORD"] = 'Leopard20514'

mail.init_app(app)


if __name__ == '__main__':
    app.run(debug=True)



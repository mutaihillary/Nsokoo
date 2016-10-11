import os
from flask import Flask, render_template, request, flash, redirect, url_for
from flask_wtf import Form as BaseForm
from forms import ContactForm
from flask_mail import Mail, Message
from werkzeug import secure_filename

UPLOAD_FOLDER = '/tmp/'
UPLOADED_FILES_DEST = '/home/kipkoech/uploads'
ALLOWED_EXTENSIONS = set(['txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'])


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


#@app.route('/uploader', methods=['GET', 'POST'])
"""""
def upload_file():
    if request.method == 'POST':
        f = request.files['file']
        f.save(secure_filename(f.filename))
        return 'file uploaded successfully'
@app.route('/upload')
def upload_file():
    return render_template('about.html')"""""
def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1] in ALLOWED_EXTENSIONS

@app.route('/', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        # check if the post request has the file part
        if 'file' not in request.files:
            flash('No file part')
            return redirect(request.url)
        file = request.files['file']
        # if user does not select file, browser also
        # submit a empty part without filename
        if file.filename == '':
            flash('No selected file')
            return redirect(request.url)
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            return redirect(url_for('upload_file',
                                    filename=filename))
    return "<br>".join(os.listdir(app.config['UPLOAD_FOLDER'],))

app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024

#app.config["UPLOAD_FOLDER"] = 'mutaihillary@yahoo.com'
#app.config["MAX_CONTENT_PATH"] = '10mb'

app.config["MAIL_SERVER"] = "smtp.gmail.com"
app.config["MAIL_PORT"] = 465
app.config["MAIL_USE_SSL"] = True
app.config["MAIL_USERNAME"] = 'hillaryksure@gmail.com'
app.config["MAIL_PASSWORD"] = 'Leopard20514'

mail.init_app(app)

"""""
if __name__ == '__main__':
    app.run(debug=True)
    """""
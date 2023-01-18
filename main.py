from flask import Flask, request, render_template
from services.Add_User_Microservice.micro_service import add_user_micro_service

UPLOAD_FOLDER = 'static'
ALLOWED_EXTENSIONS = {'csv'}

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.secret_key = "super secret key"


def allowed_files(filename: str):
    return '.' in filename and \
        filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


@app.route('/', methods=['GET', 'POST'])
def csv():
    if request.method == 'POST':
        if 'file' not in request.files:
            error = 'No se pudo agregar archivo'
            return render_template('form_error.html', error=error)
        file = request.files['file']
        if file.filename == '':
            error = 'No se adjuntó archivo'
            return render_template('form_error.html', error=error)
        if not allowed_files(file.filename):
            error = 'El archivo adjunto no es CSV'
            return render_template('form_error.html', error=error)
        if file and allowed_files(file.filename):
            add_user_micro_service(file)
            return render_template('form_output.html')

    return render_template('form_input.html')


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000, debug=True)

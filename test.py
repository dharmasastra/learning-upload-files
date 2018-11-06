from flask import Flask, request, redirect, url_for, flash
from flask_uploads import UploadSet, configure_uploads

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.secret_key = 'tets'



@app.route('/', methods=['GET', 'POST'])
def upload_file():

    return '''
    <!doctype html>
    <title>Upload new File</title>
    <h1>Upload new File</h1>
    <form method=post enctype=multipart/form-data>
      <p><input type=file name=file>
         <input type=submit value=Upload>
    </form>
    '''


if __name__ == '__main__':
    app.run(debug=True, port=8000)
import os
from flask import Flask, request, redirect, url_for
#from werkzeug import secure_filename
from werkzeug.utils import secure_filename

UPLOAD_FOLDER = '/upload'
# UPLOAD_FOLDER = '/Users/guodongzhang/Desktop/毕设/junitserver'
ALLOWED_EXTENSIONS = set(['txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'])

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1] in ALLOWED_EXTENSIONS

@app.route('/', methods=['GET', 'POST'])
@app.route('/upload/', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        file = request.files['file']
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            return redirect(url_for('upload_success', filename=filename))
    return '''
    <!doctype html>
    <title>Upload new File</title>
    <h1>Upload new File</h1>
    <form action="" method=post enctype=multipart/form-data>
      <p><input type=file name=file>
         <input type=submit value=Upload>
    </form>
    '''

@app.route('/upload_success')
def upload_success():
    return '''
    <!doctype html>
    <title>上传成功</title>
    <h1>上传成功</h1>
    <a href="/upload/">继续上传</a>
    '''

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080, debug=True)
from flask import Flask, render_template, request, send_file, send_from_directory
import os
app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'GET':
        return render_template('index.html')
    else:
        InputFile = request.files['file']
        InputFile.save(os.path.join("uploads", InputFile.filename))
        
        data=open(os.path.join("uploads", InputFile.filename)).read()
        data=data+"apend"
        with open(os.path.join("downloads", "downloads.txt"), mode="w") as f:
            f.write(data)
        
        #return send_from_directory("downloads", "downloads.txt",attachment_filename="downloads.txt",as_attachment=True)

        return send_file(os.path.join("downloads", "downloads.txt"),attachment_filename="downloads.txt",as_attachment=True)


if __name__ == '__main__':
    app.run(port=5001)

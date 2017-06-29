from flask import Flask, request, render_template, redirect, url_for
import os
from werkzeug.utils import secure_filename

app = Flask(__name__)

extension =
@app.route('/',methods=['GET','POST'])
def image_viewer():
    image_uploaded_path = os.path.join(app.root_path, 'static')
    if request.method == 'GET':
        lsfile = os.listdir(image_uploaded_path)
        print(lsfile)
        return render_template("image_display", imglist=lsfile)
    elif request.method == 'POST':
        file = request.files['file']
        filename = secure_filename(file.filename)
        image_asset_path = os.path.join(app.root_path, 'static', filename)
        file.save(image_asset_path)
        lsfile = os.listdir(image_uploaded_path)
        return render_template("image_display", imglist=lsfile)


if __name__ == '__main__':
    app.run(debug=True)

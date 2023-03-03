from flask import Flask,request,render_template,redirect,jsonify,url_for,send_file
import os
from yolo_detection_images import detectObjects
app = Flask(__name__)


app.config["ALLOWED_IMAGE_EXTENSIONS"] = ["PNG","JPG","JPEG"]

from werkzeug.utils import secure_filename
@app.route('/',methods = ['Get'])
def home():
    return render_template('main.html')

@app.route('/home',methods = ["GET","POST"])
def upload_image():
	uploads_dir = os.path.join(app.instance_path, 'Images')
	os.makedirs(uploads_dir, exist_ok=True)
	if request.method == "POST":
		image = request.files['file']

		if image.filename == '':
			print("Image must have a file name")
			return redirect(request.url)
		filename = secure_filename(image.filename)
		image.save(os.path.join(uploads_dir,filename))
		img_path = os.path.join(uploads_dir, filename)
		results=detectObjects(img_path)
		os.remove(img_path)
		return render_template("download.html")
		
	return render_template('main.html')



@app.route('/return-files',methods = ["GET"])
def return_file():
	try:
		return send_file('./instance/processedimage.jpg')
	except Exception as e:
		return str(e)


app.run(debug=True,port=2000)
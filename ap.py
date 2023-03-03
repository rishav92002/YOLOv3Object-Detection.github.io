from flask import Flask,request,render_template,redirect,jsonify,url_for,send_file

import os
from yolo_detection_images import detectObjects
app = Flask(__name__)

# app.config["IMAGE_UPLOADS"] = "/Users/Lenovo/Desktop/yoloapi/YOLO-v3-Object-Detection/static/Images"
uploads_dir = os.path.join(app.instance_path, 'Images')
os.makedirs(uploads_dir, exist_ok=True)
app.config["ALLOWED_IMAGE_EXTENSIONS"] = ["PNG","JPG","JPEG"]

from werkzeug.utils import secure_filename
@app.route('/',methods = ['Get'])
def home():
    return render_template('main.html')

@app.route('/home',methods = ["GET","POST"])
def upload_image():
	if request.method == "POST":
		image = request.files['file']

		if image.filename == '':
			print("Image must have a file name")
			return redirect(request.url)


		filename = secure_filename(image.filename)
		# basedir = os.path.abspath(os.path.dirname(__file__))
		
		# image.save(os.path.join(basedir,app.config["IMAGE_UPLOADS"],filename))
		image.save(os.path.join(uploads_dir,filename))
		img_path = os.path.join(uploads_dir, filename)
		results=detectObjects(img_path)
		os.remove(img_path)
		# return jsonify(results)
		return render_template("download.html")
		# return redirect(url_for('static',filename = "/Images" + filename), code=301)
		# img_path = f'/Users/Lenovo/Desktop/yoloapi/YOLO-v3-Object-Detection/static/Images/{filename}'
		
		# img_path = 'images/person.jpg'
		# results = detectObjects(img_path)
		# return jsonify(results)
	return render_template('main.html')



@app.route('/return-files',methods = ["GET"])
def return_file():
	try:
		return send_file('/Users/Lenovo/Desktop/yoloapi/YOLO-v3-Object-Detection/instance/processedimage.jpg')
	except Exception as e:
		return str(e)


 

# @app.route('/display/<filename>')
# def display_image(filename):
# 	return redirect(url_for('static',filename = "/Images" + filename), code=301)
# img_path = 'images/person.jpg'
# results = detectObjects(img_path)

# @app.route('/data',methods=['Get'])
# def display():
#     return jsonify(results)


app.run(debug=True,port=2000)
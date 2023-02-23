from flask import Flask, render_template, request
from keras.models import load_model
from tensorflow.keras.utils import load_img
from tensorflow.keras.utils import img_to_array
import numpy as np

app = Flask(__name__)

dic = {0 : 'Bed', 1 : 'Chair', 2 : 'Sofa'}

model = load_model('final_model.h5')

model.make_predict_function()

def predict_label(img_path):
    i = load_img(img_path, target_size=(224,224))
    img = np.array(i)
    img = np.expand_dims(img, axis=0)
    img = img / 255.0
    img = img.reshape(1,224,224,3)
    label = model.predict(img)
    if ((np.argmax(label)) == 0 ):
        output = "Bed"
    elif ((np.argmax(label)) == 1):
        output = "Chair"
    else: 
        output = "Sofa"
    return output


# routes
@app.route("/", methods=['GET', 'POST'])
def main():
	return render_template("index.html")

@app.route("/about")
def about_page():
	return "Image Classification!!"

@app.route("/submit", methods = ['GET', 'POST'])
def get_output():
	if request.method == 'POST':
		img = request.files['my_image']

		img_path = "static/" + img.filename	
		img.save(img_path)

		p = predict_label(img_path)

	return render_template("index.html", prediction = p, img_path = img_path)


if __name__ =='__main__':
	#app.debug = True
	app.run(debug = True)
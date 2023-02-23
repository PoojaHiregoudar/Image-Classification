# Image-Classification

- Firstly, I arragned the dataset into a folder and split the data into 75% as Training data and remaining 25% as validation data using th kera functions train_test_split.
- Next, I have reshaped the data into proper format to train the dataset. For training the model I have designed 3 convolution layers and flattend the data to feed it into deep neural network. 
- Then I compiled and ran the model on training data and tested it against validation data  to test its accuracy. The model resulted in a test accuracy of 80%.
- Once completed with all my fine tuning and satisfied with the model I saved the model for future usage.
- Later, I loaded the saved model into app.py file, which will predict the class of the images that are uploaded through the URL.
- Finally, I was able to upload the images and predict the classes as Bed, Chair and Sofa respectively. 

### Steps to execute:

- Run the app.py file through the terminal.
- Copy paste the local host URL from the terminal on to the web.
- Select the image to be uploaded and click submit button.
- After submitting, the model presents the image along with the predicted class.

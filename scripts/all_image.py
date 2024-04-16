from keras.models import load_model
from keras.preprocessing.image import load_img
from keras.preprocessing.image import img_to_array
from keras.applications.vgg16 import preprocess_input
from keras.applications.vgg16 import decode_predictions
from keras.applications.vgg16 import VGG16
import numpy as np
import os, os.path
from PIL import ImageFile, Image
ImageFile.LOAD_TRUNCATED_IMAGES = True
 
from keras.models import load_model
 
model = load_model('model_all.keras')

path = 'FracAtlas/images/Non_fractured'
imgs = []
valid_images = [".jpg"]
avg_frac = 0;
for f in os.listdir(path):
    ext = os.path.splitext(f)[1]
    if ext.lower() not in valid_images:
        continue
    imgs.append(os.path.join(path,f))

for i in imgs:  
    image = load_img(i, target_size=(224, 224))
    img = np.array(image)
    img = img / 255.0
    img = img.reshape(1,224,224,3)
    label = model.predict(img)
    avg_frac = avg_frac + label[0][0]
    
print(avg_frac/3366)
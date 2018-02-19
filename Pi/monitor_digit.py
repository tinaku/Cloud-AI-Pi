import io, picamera, readchar
from PIL import Image
import matplotlib.image as mpimg
import numpy as np
from keras.models import load_model
model = load_model('../AI/CNN_model.h5')
stream = io.BytesIO()                   # Create the in-memory stream
with picamera.PiCamera() as camera:
    camera.resolution = (896,896)
    #camera.start_preview()
    while True:
        if readchar.readkey() == 'q':
            break
        camera.capture(stream, format='jpeg')
        stream.seek(0)
        with Image.open(stream) as im:
            im = im.convert('L')
            im.thumbnail((28,28))
            im.save('28x28.png')
        img = mpimg.imread('28x28.png')
        img = img.reshape(1,28,28,1).astype('float32')
        img = np.ones(img.shape) - img
        prediction = model.predict_classes(img)
        print('Pi sees',prediction[0])
    #camera.stop_preview()
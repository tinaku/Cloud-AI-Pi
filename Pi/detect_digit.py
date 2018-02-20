import picamera, io, readchar
from keras.models import load_model
from PIL import Image
import matplotlib.image as mpimg
import numpy as np
with picamera.PiCamera() as camera:
    camera.resolution = (1920,1920)
    camera.hflip = True
    camera.vflip = True
    camera.brightness = 80
    camera.contrast = 80
    #camera.start_preview()
    stream = io.BytesIO()                       # Create an in-memory stream
    model = load_model('../AI/CNN_model.h5')    # as Camera warm-up time 2s
    print('Press any key to detect...')
    while readchar.readkey() != 'q':
        camera.capture('stream.jpg')
        stream.seek(0)
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
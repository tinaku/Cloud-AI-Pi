import picamera
from lib import detect, highlight
with picamera.PiCamera() as camera:
    camera.resolution = (1920,1920)
    camera.hflip = True
    camera.vflip = True
    camera.brightness = 100
    camera.contrast = 100
    while input('ENTER to detect, else to quit...') == '':
        camera.capture('faces.jpg')
        faces = detect.faces('faces.jpg')
        print(len(faces), 'face(s) found!')
        highlight.highlight(faces, 'faces.jpg')
        print('faces_highlight.jpg created!')
import os 
import argparse
import cv2

parser = argparse.ArgumentParser(prog="vid", description='Test opencv video.')
parser.add_argument('-f','--file', type=str, default=None, help='path to video')
args = parser.parse_args()

src = 0
if args.file and os.path.isfile(args.file):
    src = os.path.abspath(args.file)

webcam = cv2.VideoCapture(src)
cv2.namedWindow("cam-input")
while True:
    success, input_image = webcam.read()
    if not success:
        print("Could not get an image. Please check your video source")
        break
    cv2.imshow("cam-input", input_image)
    k = cv2.waitKey(1)
    if k == 27 or k == ord('q'):
        break
cv2.destroyWindow("cam-input")

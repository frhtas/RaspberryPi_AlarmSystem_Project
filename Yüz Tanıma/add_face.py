
import argparse
import cv2
import face_recognition
import time
import pickle
print("start")
ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", type=str, required=True,
    help="path to input image")

ap.add_argument("-n", "--name", type=str, required=True,
	help="name of person")

args = vars(ap.parse_args())



image = cv2.imread(args["image"])

detector = cv2.CascadeClassifier("haarcascade_frontalface_alt.xml")
boxes=detector.detectMultiScale(image)


boxes2 = [(y, x + w, y + h, x) for (x, y, w, h) in boxes]

encodings = face_recognition.face_encodings(image, boxes2)


try:
    data = pickle.loads(open("facebase.pickle", "rb").read())
    data["encodings"].append(encodings[0])
    data["names"].append(args["name"])
    f = open("facebase.pickle", "wb")
    f.write(pickle.dumps(data))
    f.write(pickle.dumps(data))
    print(data)
except:
    knownEncodings = [encodings[0]]
    knownNames = [args["name"]]
    data = {"encodings": knownEncodings, "names": knownNames}
    f = open("facebase.pickle", "wb")
    f.write(pickle.dumps(data))




import cv2
import face_recognition
import pickle
import numpy
print("imported")
image = cv2.imread("margo2.jpg")
detector = cv2.CascadeClassifier("haarcascade_frontalface_alt.xml")
boxes=detector.detectMultiScale(image)

# for (x, y, w, h) in boxes:
# 	# draw the face bounding box on the image
# 	cv2.rectangle(image, (x, y), (x + w, y + h), (0, 255, 0), 2)
boxes2 = [(y, x + w, y + h, x) for (x, y, w, h) in boxes]
	# compute the facial embeddings for each face bounding box
encoding = face_recognition.face_encodings(image, boxes2)



data = pickle.loads(open("facebase.pickle", "rb").read())

matches = face_recognition.compare_faces(data["encodings"],
	encoding[0])
name = "Unknown"
print(matches)
# check to see if we have found a match
if True in matches:
	# find the indexes of all matched faces then initialize a
	# dictionary to count the total number of times each face
	# was matched
	matchedIdxs = [i for (i, b) in enumerate(matches) if b]
	counts = {}
	# loop over the matched indexes and maintain a count for
	# each recognized face face
	for i in matchedIdxs:
		name = data["names"][i]
		counts[name] = counts.get(name, 0) + 1
	# determine the recognized face with the largest number
	# of votes (note: in the event of an unlikely tie Python
	# will select first entry in the dictionary)
	name = max(counts, key=counts.get)
print(name)



cv2.imwrite("new.jpg",image)

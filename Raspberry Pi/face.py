import cv2
import face_recognition
import pickle
import numpy
from threading import Thread
import time

class FaceRecognition(Thread):
	def __init__(self):
		Thread.__init__(self)
		self.recognize_face = False
		self.detector = cv2.CascadeClassifier("haarcascade_frontalface_alt.xml")
		self.face_database = pickle.loads(open("facebase.pickle", "rb").read())
		self.recognized_person_name =None
		self.recognization_status = False
		self.image = None
		print("Initialized Face Regognition Object")
	def run(self):
		print("Face Regognition Object Started Working")
		while(True):
			if(self.recognize_face == True):
				
				camera = cv2.VideoCapture("rtsp://gomulu:gomulu2022@10.42.0.45:554/stream2")
				if(not(camera.isOpened())):
					print("Could not read camera")
					continue
				_, image = camera.read()
				camera.release()
				cv2.imwrite("eko.jpg",image)
				boxes=self.detector.detectMultiScale(image)
				if(len(boxes) == 0):
					print("No Face Found")
				else:	
					boxes2 = [(y, x + w, y + h, x) for (x, y, w, h) in boxes]
					encoding = face_recognition.face_encodings(image, boxes2)
					matches = face_recognition.compare_faces(self.face_database["encodings"],encoding[0], tolerance=0.50)
					if True in matches:
						self.recognization_status = True
						matchedIdxs = [i for (i, b) in enumerate(matches) if b]
						counts = {}
						for i in matchedIdxs:
							self.recognized_person_name = self.face_database["names"][i]
							counts[self.recognized_person_name] = counts.get(self.recognized_person_name, 0) + 1
						self.recognized_person_name = max(counts, key=counts.get)
						print(self.recognized_person_name)
						self.recognize_face = False
					else:
						print("Person match not found")
			else:
				time.sleep(1)
				print("Suspended status, neccesary objects are initialized")
	
	def reset_recognizer(self):
		self.recognize_face = False
		self.recognization_status = False
	def start_recognizer(self):
		self.recognize_face = True
	def get_recognization_status(self):
		return self.recognization_status
	def get_recognized_people_name(self):
		if(self.recognization_status):
			return self.recognized_person_name
		else:
			return "Unknown"



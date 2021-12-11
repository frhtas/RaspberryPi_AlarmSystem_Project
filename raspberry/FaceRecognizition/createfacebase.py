import pickle
knownEncodings = []
knownNames = []
data = {"encodings": knownEncodings, "names": knownNames}
f = open("facebase.pickle", "rb+")
f.write(pickle.dumps(data))
f.close()
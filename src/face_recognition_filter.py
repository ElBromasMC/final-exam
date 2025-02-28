import face_recognition
import os
import cv2
import numpy as np

def generateEncodings(imgs_path):
    known_faces = {}
    known_faces['names'] = []
    known_faces['encodings'] = []
    for file in os.listdir(imgs_path):
        image = face_recognition.load_image_file(os.path.join(imgs_path,file))
        encoding = face_recognition.face_encodings(image)[0]
        name = os.path.splitext(file)[0]
        known_faces['names'].append(name)
        known_faces['encodings'].append(encoding)
    return known_faces


def recognizeFaces(frame, known_faces):
    small_frame = cv2.resize(frame, (0,0), fx=0.25, fy=0.25)
    rgb_small_frame = np.ascontiguousarray(small_frame[:,:,::-1])

    face_locations = face_recognition.face_locations(rgb_small_frame)
    face_encodings = face_recognition.face_encodings(rgb_small_frame, face_locations)
    i = 0

    face_names = []

    for face_encoding in face_encodings:
        matches = face_recognition.compare_faces(known_faces['encodings'], face_encoding)
        name = "Unknown"

        face_distances = face_recognition.face_distance(known_faces['encodings'], face_encoding)
        best_match_index = np.argmin(face_distances)
        if matches[best_match_index]:
            name = known_faces['names'][best_match_index]
            face_names.append(name)
    
    for (top, right, bottom, left), name in zip(face_locations, face_names):
        top *= 4
        right *= 4
        bottom *= 4
        left *= 4

        cv2.rectangle(frame, (left, top), (right, bottom), (0, 0, 255), 2)

        cv2.rectangle(frame, (left, bottom - 35), (right, bottom), (0, 0, 255), cv2.FILLED)
        font = cv2.FONT_HERSHEY_DUPLEX
        cv2.putText(frame, name, (left + 6, bottom - 6), font, 1.0, (255, 255, 255), 1)

    return frame

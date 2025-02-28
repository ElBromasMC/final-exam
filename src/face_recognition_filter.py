import face_recognition
import os
import cv2
import numpy as np

# Variables globales para almacenar detecciones previas
last_face_locations = []
last_face_names = []
frame_counter = 0  # Contador de frames
no_face_counter = 0  # Contador de frames sin detección
max_no_face_frames = 8  # Cuántos frames esperar antes de borrar las detecciones
skip_frames = 4  # Procesar solo 1 de cada N frames

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



def drawBoxes(frame, locations, names):
    for (top, right, bottom, left), name in zip(locations, names):
        top *= 4
        right *= 4
        bottom *= 4
        left *= 4
        cv2.rectangle(frame, (left, top), (right, bottom), (0, 255, 0), 2)
        cv2.rectangle(frame, (left, bottom - 35), (right, bottom), (0, 255, 0), cv2.FILLED)
        font = cv2.FONT_HERSHEY_DUPLEX
        cv2.putText(frame, name, (left + 6, bottom - 6), font, 1.0, (255, 255, 255), 1)
    return frame

def recognizeFaces(frame, known_faces):
    global frame_counter, last_face_locations, last_face_names, no_face_counter
    frame_counter += 1

    # Si no es un frame a procesar, usa las últimas detecciones
    if frame_counter % skip_frames != 0:
        return drawBoxes(frame, last_face_locations, last_face_names)

    small_frame = cv2.resize(frame, (0,0), fx=0.25, fy=0.25)
    rgb_small_frame = np.ascontiguousarray(small_frame[:,:,::-1])

    # Detección de caras
    face_locations = face_recognition.face_locations(rgb_small_frame)
    face_encodings = face_recognition.face_encodings(rgb_small_frame, face_locations)

    face_names = []

    for face_encoding in face_encodings:
        matches = face_recognition.compare_faces(known_faces['encodings'], face_encoding)
        name = "Unknown"

        if matches:
            face_distances = face_recognition.face_distance(known_faces['encodings'], face_encoding)
            best_match_index = np.argmin(face_distances)
            if matches[best_match_index]:
                name = known_faces['names'][best_match_index]

        face_names.append(name)

    # Si hay caras, actualizar las detecciones y reiniciar el contador de ausencia
    if face_locations:
        last_face_locations = face_locations
        last_face_names = face_names
        no_face_counter = 0  # Reiniciar el contador si hay caras
    else:
        no_face_counter += 1  # Aumentar el contador si no hay caras

    # **BORRAR DETECCIONES SOLO DESPUÉS DE X FRAMES SIN CARAS**
    if no_face_counter >= max_no_face_frames:
        last_face_locations = []
        last_face_names = []

    return drawBoxes(frame, last_face_locations, last_face_names)

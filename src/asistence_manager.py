import numpy as np
import os
from datetime import datetime
import face_recognition
from collections import Counter

class Classroom:
    def __init__(self):
        self.asistence_file = datetime.now().strftime("%Y_%m_%d") + "_asistence.csv"
        self.students_list = []
        self.encodings_list = []
        self.asistence_record = []

    def generateStudentData(self,imgs_path):
        for file in os.listdir(imgs_path):
            image = face_recognition.load_image_file(os.path.join(imgs_path,file))
            mat_id = os.path.splitext(file)[0].split("-")[0]
            name = os.path.splitext(file)[0].split("-")[1]
            encoding = face_recognition.face_encodings(image)[0]
            if mat_id and name:
                self.students_list.append({
                    'mat_id': mat_id,
                    'name': name,
                    'encoding': encoding
                })
                self.encodings_list.append(encoding)
            
    def checkAsistenceFile(self):
        return True if os.path.isfile(self.asistence_file) else False

    def clearAsistence(self):
        repetition = Counter(self.asistence_record)
        self.asistence_record = [key for key, value in repetition.items() if value >= 40]
    
    def registerAsistence(self):
        file = open(self.asistence_file, 'w')
        self.clearAsistence()
        for student_index, student in enumerate(self.students_list):
            if student_index in self.asistence_record:
                file.write(f"{student['mat_id']}, {student['name']}, PRESENTE\n")
            else:
                file.write(f"{student['mat_id']}, {student['name']}, FALTA\n")
        file.close()
                
    def dump(self):
        print(self.students_list)

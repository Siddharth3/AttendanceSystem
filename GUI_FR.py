from flask import Flask, jsonify, render_template
import cv2
import os
import face_recognition as fr
import numpy as np
import csv
from datetime import datetime


app = Flask(__name__)

@app.route('/')
def home():
    return render_template('Portal.html')

@app.route('/give-attendance', methods=['GET'])
def give_attendance():
    
    dataPath = 'Dataset/'
    data = os.listdir(dataPath)
    print(data)

    cascade_face = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

    video_capture = cv2.VideoCapture(0)
    data_face_encoding = []
    data_face_names = []

    for i in data:
        print(dataPath+i)
        image = fr.load_image_file(dataPath + i)
        encoding = fr.face_encodings(image)[0]
        data_face_encoding.append(encoding)
        data_face_names.append(os.path.splitext(i)[0])

    print("Names: " + str(data_face_names))

    face_names_copy = data_face_names.copy()
    face_locations = []
    face_encodings = []
    s = True

    now = datetime.now()
    todays_date = now.strftime("%Y-%m-%d")
    file_name = todays_date + '.csv'

    while True:
        _, frame = video_capture.read()
        small_frame = cv2.resize(frame, (0, 0), fx=0.25, fy=0.25)
        rgb_small_frame = cv2.cvtColor(small_frame, cv2.COLOR_BGR2RGB)
        green_frame = cascade_face.detectMultiScale(cv2.cvtColor(frame, cv2.COLOR_BGR2RGB), 1.3, 4)

        for (x, y, w, h) in green_frame:
            cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 4)
            
        if s:
            face_locations = fr.face_locations(rgb_small_frame)
            face_encodings = fr.face_encodings(rgb_small_frame, face_locations)
            face_names = []
            
            for face_encoding in face_encodings:
                matches = fr.compare_faces(data_face_encoding, face_encoding)
                name = ""
                face_distance = fr.face_distance(data_face_encoding, face_encoding)
                best_match_index = np.argmin(face_distance)

                if matches[best_match_index]:
                    name = data_face_names[best_match_index]

                face_names.append(name)

                if name in data_face_names:
                    if name in face_names_copy:
                        face_names_copy.remove(name)
                        print("Face name copy: " + str(face_names_copy))
                        current_date = now.strftime("%Y-%m-%d %H:%M:%S")
                        name_exists = False
                        
                        try:
                            # Check if file exists
                            if os.path.isfile(file_name):
                                # Check if the name already exists in the CSV
                                with open(file_name, mode='r', newline='') as f:
                                    reader = csv.reader(f)
                                    for row in reader:
                                        if row and row[0] == name:
                                            name_exists = True
                                            print(f"{name} is already present for today.")
                                            return jsonify({"message": f"{name} is already present for the day"})
                                            break

                            # If file does not exist or name is not in file, add it
                            if not name_exists:
                                with open(file_name, mode='a', newline='') as f:
                                    writer = csv.writer(f)
                                    
                                    # Write header if file is empty
                                    if os.path.getsize(file_name) == 0:
                                        writer.writerow(['Name', 'Date/Time'])
                                    
                                    # Append new entry with name and date
                                    writer.writerow([name, current_date])
                                    print(f"Attendance marked for student name: {name}.")
                                    return jsonify({"message": f"Attendance marked for student name: {name}."})

                        except FileNotFoundError:
                            print("Error: File not found.")
                            return jsonify({"message": "Error: File not found."})

        cv2.imshow('Find Me If You Can', frame)
        if cv2.waitKey(10) == ord('a'):
            break
            
            
    video_capture.release()
    cv2.destroyAllWindows()
    f.close()
    
if __name__ == '__main__':
    app.run(debug=True)
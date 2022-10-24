# import the necessary packages
from imutils.video import VideoStream, FPS
import face_recognition
import imutils
import pickle
import time
import cv2
import numpy as np
#import serial
from time_car_start import check_time, real_time, now
from detect_location import detect_position


# Initialize 'currentname' to trigger only when a new person is identified.
currentname = "Stranger"
# Determine faces from encodings.pickle file model created from train_model.py
encodingsP = "encodings.pickle"
# Create interface between arduino and computer
#arduino = serial.Serial(port='COM3', baudrate=115200, timeout=0.1)
# load the known faces and embeddings along with OpenCV's Haar
# cascade for face detection
print("[INFO] loading encodings + face detector…")
data = pickle.loads(open(encodingsP, "rb").read())
# initialize the video stream and allow the camera sensor to warm up
print("[INFO] starting video stream…")
vs = VideoStream(src=0).start()
# vs = VideoStream(usePiCamera=True).start()
time.sleep(1.0)

# start the FPS counter
fps = FPS().start()
check_time()

# loop over frames from the video file stream
while True:
    # grab the frame from the threaded video stream and resize it
    # to 500px (to speedup processing)
    frame = vs.read()
    frame = imutils.resize(frame, width=500)
    # create time start when driver start driving car
    check = real_time()[0]
    # convert the input frame from  BGR to RGB (for face
    # detection and face recognition
    rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    # (top, right, bottom, left) order of the face
    boxes = face_recognition.face_locations(rgb, model="hog")
    # compute the facial embeddings for each face bounding box
    encodings = face_recognition.face_encodings(rgb, boxes)
    names = []

    # loop over the facial embeddings
    for encoding in encodings:
        # attempt to match each face in the input image to our known
        # encodings
        matches = face_recognition.compare_faces(data["encodings"], encoding)
        face_Dis = face_recognition.face_distance(data["encodings"], encoding)
        smallest_Index = np.argmin(face_Dis)
        name = "Stranger"  # if face is not recognized, then print Stranger

        # check to see if we have found a match
        if face_Dis[smallest_Index] < 0.4:
            # find the indexes of all matched faces then initialize a
            # dictionary to count the total number of times each face
            # was matched
            matchedIdxs = [i for (i, b) in enumerate(matches) if b]
            counts = {}
            # loop over the matched indexes and maintain a count for
            # each recognized face
            for i in matchedIdxs:
                name = data["names"][i]
                counts[name] = counts.get(name, 0) + 1
            # determine the recognized face with the largest number
            # of votes (note: in the event of an unlikely tie Python
            # will select first entry in the dictionary)
            name = max(counts)

            # If someone in your dataset is identified, print their name on the screen
        if currentname != name:
            #Read data from arduino
            '''return_from_arduino = arduino.readline().decode('utf-8')
            if return_from_arduino != 'Complete Engine Start':
                # Send data to arduino if recognize the face
                arduino.write(b'Owner')
            else:
                ardino.write(b'Complete Engine Start')
                    '''
            currentname = name
            print(currentname)
        else:
            #arduino.write(b'Stranger')
            print(currentname)
        # update the list of names
        names.append(name)
    # Check face of driver each 5 minutes
    if check == 300:
        if currentname == 'Stranger':
            #arduino.write(b'Detect Stranger driving car')
            location = detect_position()
            img_name = f"data_theft/image_at_{now()[0]}h {now()[1]}m {now()[2]}s.jpg"
            cv2.imwrite(img_name, frame)
            print("Start Detect stranger's position")
            print("Current IP location is", location)
        temp = real_time()[1]
        f = open("timecheck.pickle", "wb")
        f.write(pickle.dumps(temp))
        f.close()
    # loop over the recognized faces
    for ((top, right, bottom, left), name) in zip(boxes, names):
        # draw the predicted face name on the image – color is in BGR
        cv2.rectangle(frame, (left, top), (right, bottom),
                      (0, 255, 0), 2)
        y = top - 15 if top - 15 > 15 else top + 15
        cv2.putText(frame, name, (left, y), cv2.FONT_HERSHEY_SIMPLEX,
                    .8, (255, 0, 0), 2)

    # display the image to our screen
    cv2.imshow("Facial Recognition is Running", frame)
    key = cv2.waitKey(1) & 0xFF

    # quit when 'q' key is pressed
    if key == ord("q"):
        break

    # update the FPS counter
    fps.update()
#close interface with arduino
#arduino.close()
# stop the timer and display FPS information
fps.stop()
print("[INFO] elasped time: {:.2f}".format(fps.elapsed()))
print("[INFO] approx. FPS: {:.2f}".format(fps.fps()))

# do a bit of cleanup
cv2.destroyAllWindows()
vs.stop()
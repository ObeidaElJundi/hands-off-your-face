import cv2
import numpy as np
import sys
import vlc

face_cascade = cv2.CascadeClassifier('face.xml')
sound_path = './police.mp3'
sound = vlc.MediaPlayer(sound_path)
sound_playing = False
cap = cv2.VideoCapture(0,cv2.CAP_DSHOW)
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 1280)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 720)
tracker = cv2.TrackerMIL_create()

# Read second frame.
ok, frame = cap.read()
ok, frame = cap.read()
if not ok:
    print('Cannot read video file')
    sys.exit()
# select a bounding box
bbox = cv2.selectROI(frame, False)
# Initialize tracker with first frame and bounding box
ok = tracker.init(frame, bbox)

def hand_close_to_face(box_face, box_hand):
    x_overlap = max(0, min(box_face[0]+box_face[2], box_hand[0]+box_hand[2]) - max(box_face[0], box_hand[0]))
    y_overlap = max(0, min(box_face[1]+box_face[3], box_hand[1]+box_hand[3]) - max(box_face[1], box_hand[1]))
    return x_overlap * y_overlap > 0

while(True):
    ret, frame = cap.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    face = face_cascade.detectMultiScale(frame, 1.5, 2)
    if len(face)>0:
        print(face)
        face = face[0]
        #for (x, y, w, h) in face: cv2.rectangle(frame, (x, y), (x + w, y + h), (255, 0, 0), 2)
        cv2.rectangle(frame, (face[0], face[1]), (face[0] + face[2], face[1] + face[3]), (255, 0, 0), 2)
        
        print('update tracker')
        # Update tracker
        ok, bbox = tracker.update(frame)
        print('tracker updated\nbbox:',bbox)
        # Draw bounding box
        if ok:
            # Tracking success
            p1 = (int(bbox[0]), int(bbox[1]))
            p2 = (int(bbox[0] + bbox[2]), int(bbox[1] + bbox[3]))
            cv2.rectangle(frame, p1, p2, (0,0,255), 2)
            print('ok')
            close = hand_close_to_face(face, bbox)
            #print('close:',close)
            if close:
                cv2.putText(img=frame, text='Corona!', org=(int(100 / 2 - 20), int(100 / 2)), fontFace=cv2.FONT_HERSHEY_DUPLEX, fontScale=2, color=(0, 0, 255))
                if sound_playing == False:
                    sound_playing = True
                    sound.play()
            else:
                if sound_playing == True:
                    sound_playing = False
                    sound.stop()

    cv2.imshow('Driver_frame', frame)
    k = cv2.waitKey(30) & 0xff
    if k == 27:
        break

cap.release()
cv2.destroyAllWindows()
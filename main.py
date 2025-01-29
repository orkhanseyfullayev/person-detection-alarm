import cv2
import numpy as np
from ultralytics import YOLO
import time
from mail_send import mail_send

model = YOLO("yolov8l.pt")
font = cv2.FONT_HERSHEY_SIMPLEX
camera = cv2.VideoCapture(0)

person_last_seen = {}
time_for_alarm = 5
mail_sent = True

while True:
    ret, img = camera.read()
    img = cv2.flip(img, 1) # mirror effect
    rgb_img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    results = model(rgb_img, verbose=False)
    labels = results[0].names

    detected_person = False
    current_time = time.time()

    for i in range(len(results[0].boxes)):
        x1, y1, x2, y2 = results[0].boxes.xyxy[i]
        score = results[0].boxes.conf[i]
        label = results[0].boxes.cls[i]
        x1, y1, x2, y2, score, label = int(x1), int(y1), int(x2), int(y2), float(score), int(label)
        name = labels[label]
        if score < 0.5:
            continue
        cv2.rectangle(img, (x1, y1), (x2, y2), (255, 0, 0), 2)
        text = name + " " + str(format(score, '.2f'))
        cv2.putText(img, text, (x1, y1 - 10), font, 1.2, (102, 0, 153), 2)

        if name == 'person':
            detected_person = True
        if i not in person_last_seen:
            person_last_seen[i] = current_time
            mail_sent = True
        elif current_time - person_last_seen[i] >= time_for_alarm:
            cv2.putText(img, "ALARM", (50, 50), font, 1.2, (0, 0, 255), 2)
            if mail_sent:
                cv2.imwrite('current_frame.jpg', img)
                mail_send('current_frame.jpg')
                mail_sent = False

    if not detected_person:
        person_last_seen.clear()

    cv2.imshow("camera", img)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

camera.release()
cv2.destroyAllWindows()

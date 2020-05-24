import cv2
import time
def get_tracker():
    print('Select Algorithm for tacking:')
    print('0: BOOSTING')
    print('1: MIL')
    print('2: KCF')
    print('3: TLD')
    print('4: MEDIAN FLOW')
    print('5: GOTURN')
    print('6: MOSSE')
    print('7: CSRT')
    print('Default: BOOSTING')
    choice = input('Choice: ')
    if choice == 0: tracker = cv2.TrackerBoosting_create()
    elif choice == 1: tracker = cv2.TrackerMIL_create()
    elif choice == 2: tracker = cv2.TrackerKCF_create()
    elif choice == 3: tracker = cv2.TrackerTLD_create()
    elif choice == 4: tracker = cv2.TrackerMedianFlow_create()
    elif choice == 5: tracker = cv2.TrackerGOTURN_create()
    elif choice == 6: tracker = cv2.TrackerMOSSE_create()
    elif choice == 7: tracker = cv2.TrackerCSRT_create()
    else: tracker = cv2.TrackerBoosting_create()
    return tracker
tracker = get_tracker()
tracker_name = str(tracker).split()[0][1:]
cap = cv2.VideoCapture(0)
ret, frame = cap.read()
time.sleep(0.5)
ret, frame = cap.read()
roi = cv2.selectROI(frame, False)
initial_frame = tracker.init(frame, roi)
while True:
    ret, frame = cap.read()
    success, roi = tracker.update(frame)
    (x,y,w,h) = tuple(map(int,roi))
    if success:
        cv2.rectangle(frame,(x,y),(x+w,y+h),(0,255,0),3)
    else:
        cv2.putText(frame,'FAIL',(100,200),cv2.FONT_HERSHEY_SIMPLEX,1,(0,255,0),2)
    cv2.imshow(tracker_name, frame)
    if cv2.waitKey(10) & 0xFF == 27:
        break
cap.release()
cv2.destroyAllWindows()
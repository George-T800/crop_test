import cv2

x=0
y=0
x1=x+1200
y1=y



#pirveli 
first_side_sigane_y =1430
first_side_simagle_x =1120
#meore
second_side_sigane_y = 3220 
second_side_simagle_x= 1430


cap = cv2.VideoCapture(0)
cap2 = cv2.VideoCapture(2)


while(cap.isOpened()):
    ret, frame = cap.read()
    ret2, frame2 =cap2.read()

    if ret == True:
        #frame_crop = frame[y0:y1, x0:x1]
        cv2.imshow("crop", frame)
        cv2.imshow("sss", frame2 )
#        key = cv2.waitKey(25)


    if cv2.waitKey(1) & 0XFF == ord('q'):
        break
    

cv2.destroyAllWindows()
cap.release()


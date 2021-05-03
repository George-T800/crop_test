import cv2

x=40
y=30 
x1=40
y1=200

cap=cv2.VideoCapture (0)
cap2 =cv2.VideoCapture(4)


while (cap.isOpened()):
   ret, frame = cap.read()
   ret2, frame2= cap2.read()
   if ret == True:


 
      frame_crop = frame [y:y+210, x:x+190]
      frame_crop2 = frame2 [y:y+210, x:x+190]     
# cv2.imshow("1", frame_crop)
#      cv2.imshow ("Full1", frame)
      cv2.imshow ("Full2", frame2)

      x1=190
      y1=30
      frame_crop2 = frame[y1:y1+220, x1:x1+190]
     # cv2.imshow ('2', frame_crop2)


      x1=380
      y1=30
      frame_crop3=frame [y1:y1+220, x1:x1+190]
#      cv2.imshow ('3', frame_crop3)

      x1=50
      y1=225
      frame_crop4=frame[y1:y1+220, x1:x1+190]
      #cv2.imshow ("4", frame_crop4)

      y1=225
      x1=380
      frame_crop5 = frame [y1:y1+220, x1:x1+190]
#      cv2.imshow ('5', frame_crop5)

      x=50
      y=30

      frame_crop6=frame2 [y:y+220, x:x+190]
#      cv2.imshow ("6", frame_crop6)

      x=50
      y=220
      frame_crop7=frame2 [y:y+220, x:x+190]
#      cv2.imshow ('7',frame_crop7)

      x=400
      y=30
      frame_crop8 = frame2 [y:y+220, x:x+190]
#      cv2.imshow('8', frame_crop8)

      x=380
      y=30
      frame_crop9=frame2 [y:y+220, x:x+190]
#      cv2.imshow ("9", frame_crop9)

      x=400
      y=230
      frame_crop10= frame2 [y:y+220, x:x+190]
      cv2.imshow ("10", frame_crop10)


   if cv2.waitKey(1) & 0xFF == ord ('q'):
       break

cv2.destroyAllWindows()
cap.release()

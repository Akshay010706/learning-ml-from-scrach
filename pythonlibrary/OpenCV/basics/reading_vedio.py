import cv2 as cv

#reading video
capture = cv.VideoCapture('catvideo.mp4')
#it captures the instant of the video frame
#videocaptuer fuction takes video path as an argument or 0 for you computer camera and 1.... for external camera

# we read video frame by frame
#hence we use while loop to read a video
while True:
    isTrue, frame = capture.read()
    #we show each frame
    cv.imshow('Video',frame)
    
    if cv.waitKey(20) & 0xFF==ord('d'):#if the letter d is pressed the video breaks
        break

capture.release()
cv.destroyAllWindows()    
       


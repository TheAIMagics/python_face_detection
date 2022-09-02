import cv2, time

# VideoCapture will read the 1st frame/image of the video
video = cv2.VideoCapture(0)

a= 1

while True:
    a = a+1
    # frame is a NumPy array, It represents the first image that video captures
    # check is a bool data type , it return true if Python is able to read VideoCapture object
    check, frame = video.read()
    
    # Convert each frame into a gray scale image
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    
    cv2.imshow("Capture", gray)
    
    # This will generate a new frame after every 1 ms
    key = cv2.waitKey(1)
    
    # Once user enters 'q' the window will be detroyed
    if key == ord('q'):
        break

print(a)

video.release()

cv2.destroyAllWindows()
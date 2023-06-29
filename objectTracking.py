# image processing 1
import cv2
import numpy as np
import yaml
import argparse

# Read config file
with open("./config.yml") as file:
    config = yaml.load(file, Loader=yaml.FullLoader)

# print(config)
parser = argparse.ArgumentParser()
parser.add_argument("--input","-i",help="Input type: image, webcam, video",default=config["input_type"])
parser.add_argument("--path","-p",help="Path to image or video",default=config["image_path"])

arg = parser.parse_args()

config["input_type"] = arg.input
config["image_path"] = arg.path

# create a named window
cv2.namedWindow("Trackbars")
# cv2.moveWindow("Trackbars",320,0)

# Create Trackbars
def nothing(x):
    pass
cv2.createTrackbar("hsvLow","Trackbars",80,179,nothing)
cv2.createTrackbar("hsvHigh","Trackbars",120,179,nothing)
cv2.createTrackbar("satLow","Trackbars",104,255,nothing)
cv2.createTrackbar("satHigh","Trackbars",255,255,nothing)
cv2.createTrackbar("valLow","Trackbars",83,255,nothing)
cv2.createTrackbar("valHigh","Trackbars",255,255,nothing)

# Read input
input_type = config["input_type"]

if input_type == "image":
    img_path = config["image_path"]
    img1 = cv2.imread(img_path)
elif input_type == "webcam":
    webCam=cv2.VideoCapture(0)
elif input_type == "video":
    video_path = config["video_path"]
    video =cv2.VideoCapture(video_path)
    
# Main loop
while True:
    
    if input_type == "image":
        frame = img1
    elif input_type == "webcam":
        ret,frame = webCam.read()
    elif input_type == "video":
        ret,frame = video.read()
    
    frame = cv2.resize(frame,(640,480))
    hsvL=cv2.getTrackbarPos("hsvLow","Trackbars")
    hsvH = cv2.getTrackbarPos("hsvHigh","Trackbars")
    satL=cv2.getTrackbarPos("satLow","Trackbars")
    satH = cv2.getTrackbarPos("satHigh","Trackbars")
    valL=cv2.getTrackbarPos("valLow","Trackbars")
    valH = cv2.getTrackbarPos("valHigh","Trackbars")
    hsv = cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)
    lb = np.array([hsvL,satL,valL])
    hb = np.array([hsvH,satH,valH])
    
    FGmask = cv2.inRange(hsv,lb,hb)
    cv2.imshow('FGmask',FGmask)
    # cv2.moveWindow('FGmask',400,0)
    contours,he = cv2.findContours(FGmask,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)
    contours = sorted(contours,key=lambda x:cv2.contourArea(x),reverse=True)
    for cnt in contours:
        area=cv2.contourArea(cnt)
        (x,y,w,h)=cv2.boundingRect(cnt)
        if area>=1000:
            cv2.rectangle(frame,(x,y),(x+w,y+h),(155,117,255),2)
    # cv2.drawContours(frame,contours,-1,(255,0,0),3)   
    cv2.imshow('frame',frame)
    # cv2.moveWindow('frame',0,250)
    
    if cv2.waitKey(1)==ord('q'):
        break
if input_type == "video":
    video.release()
elif input_type == "webcam":
    webCam.release()
cv2.destroyAllWindows()
    


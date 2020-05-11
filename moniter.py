import serial
import time
from datetime import datetime, date
from time import sleep
import os
import sys
from firebase_upload import put_img

ports = {"win32": "COM3", "linux": "/dev/ttyACM0"}

platform = sys.platform

if platform == "win32":
    import cv2

port = ports[platform]
print("starting on " + str(platform) + " with port " + str(port))
ser = serial.Serial(
    port=port,
    baudrate=9600,
    parity=serial.PARITY_NONE,
    stopbits=serial.STOPBITS_ONE,
    bytesize=serial.EIGHTBITS,
    timeout=0,
)


def time_print():
    time = str(datetime.now())

    return time[11 : len(time) - 4] + " "


print("Loaded")
past = 0

counts = 0
while True:

    data_raw = ser.readline().decode().strip()
    if data_raw:
        data_raw = int(data_raw)
        # print("Data is: " + data_raw)

        if data_raw > 100:
            if counts > 500:

                print(time_print() + "Lots of light detected" + ": " + str(data_raw))

                # dont activate for 10 seconds
                # sleep(5)

                # if allowed to store in db

                print("Store in db")
                # take photo
                if platform == "win32":
                    print("on windows")
                    cap = cv2.VideoCapture(0)
                    if not cap.isOpened():
                        print("Cant print")
                    else:
                        ret, frame = cap.read()

                        frame = cv2.resize(frame, (300, 230))

                        cv2.imwrite("img.jpg", frame)
                        cap.release()
                elif platform == "linux":
                    os.system("raspistill -o img.jpg -w 230 -h 300")

                put_img("img.jpg", "img.jpg")

                # past_time = datetime.now()
                counts = -2000

        # after done usig ,store
        counts += 1

        # load quickly so make it 2 less than 500

        # if gets too big, prevent int over flow
        if counts > 700:
            counts = 501

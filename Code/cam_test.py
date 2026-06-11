"""
Vision-Based Human Following Robot
Author: Saadiya Farheen

Hardware:
- Raspberry Pi 4B
- Pi Camera v1.3
- 2 x TB6612FNG Motor Drivers
- 4 x DC Gear Motors

Software:
- Python
- OpenCV
- TensorFlow Lite
- Picamera2
"""

import cv2
import numpy as np
from PIL import Image
import time
from picamera2 import Picamera2
import common as cm
import RPi.GPIO as GPIO


# =====================================================
# MODEL CONFIGURATION
# =====================================================

MODEL_DIR = "."
MODEL_FILE = "mobilenet_ssd_v2_coco_quant_postprocess.tflite"
LABEL_FILE = "coco_labels.txt"

SCORE_THRESHOLD = 0.45
TOP_K = 3


# =====================================================
# LOAD TFLITE MODEL
# =====================================================

interpreter, labels = cm.load_model(
    MODEL_DIR,
    MODEL_FILE,
    LABEL_FILE,
    edgetpu=0
)


# =====================================================
# CAMERA CONFIGURATION
# =====================================================

FRAME_W = 320
FRAME_H = 240

picam2 = Picamera2()

picam2.configure(
    picam2.create_preview_configuration(
        main={
            "size": (FRAME_W, FRAME_H),
            "format": "BGR888"
        }
    )
)

picam2.start()
time.sleep(1)

print("Camera Started")


# =====================================================
# MOTOR DRIVER 1 PINS
# =====================================================

PWMA1 = 18
AIN1_1 = 17
AIN2_1 = 27

BIN1_1 = 22
BIN2_1 = 5
PWMB1 = 19

STBY1 = 23


# =====================================================
# MOTOR DRIVER 2 PINS
# =====================================================

PWMA2 = 12
AIN1_2 = 6
AIN2_2 = 13

BIN1_2 = 20
BIN2_2 = 21
PWMB2 = 16

STBY2 = 24


# =====================================================
# GPIO SETUP
# =====================================================

GPIO.setmode(GPIO.BCM)

all_pins = [
    PWMA1, AIN1_1, AIN2_1,
    BIN1_1, BIN2_1, PWMB1, STBY1,
    PWMA2, AIN1_2, AIN2_2,
    BIN1_2, BIN2_2, PWMB2, STBY2
]

for pin in all_pins:
    GPIO.setup(pin, GPIO.OUT)

GPIO.output(STBY1, GPIO.HIGH)
GPIO.output(STBY2, GPIO.HIGH)


# =====================================================
# PWM SETUP
# =====================================================

pwmA1 = GPIO.PWM(PWMA1, 1000)
pwmB1 = GPIO.PWM(PWMB1, 1000)

pwmA2 = GPIO.PWM(PWMA2, 1000)
pwmB2 = GPIO.PWM(PWMB2, 1000)

pwmA1.start(0)
pwmB1.start(0)

pwmA2.start(0)
pwmB2.start(0)

BASE_SPEED = 40


# =====================================================
# MOTOR FUNCTIONS
# =====================================================

def move_forward(speed):
    """Move robot forward."""

    GPIO.output(AIN1_1, GPIO.HIGH)
    GPIO.output(AIN2_1, GPIO.LOW)

    GPIO.output(BIN1_1, GPIO.HIGH)
    GPIO.output(BIN2_1, GPIO.LOW)

    GPIO.output(AIN1_2, GPIO.HIGH)
    GPIO.output(AIN2_2, GPIO.LOW)

    GPIO.output(BIN1_2, GPIO.HIGH)
    GPIO.output(BIN2_2, GPIO.LOW)

    pwmA1.ChangeDutyCycle(speed)
    pwmB1.ChangeDutyCycle(speed)

    pwmA2.ChangeDutyCycle(speed)
    pwmB2.ChangeDutyCycle(speed)


def stop_all():
    """Stop all motors."""

    pwmA1.ChangeDutyCycle(0)
    pwmB1.ChangeDutyCycle(0)

    pwmA2.ChangeDutyCycle(0)
    pwmB2.ChangeDutyCycle(0)


# =====================================================
# DETECTION SETTINGS
# =====================================================

frame_count = 0
DETECTION_INTERVAL = 4

human_detected = False


# =====================================================
# MAIN PROGRAM
# =====================================================

try:

    while True:

        frame = picam2.capture_array()

        frame_count += 1

        if frame_count % DETECTION_INTERVAL == 0:

            rgb = cv2.cvtColor(
                frame,
                cv2.COLOR_BGR2RGB
            )

            pil_im = Image.fromarray(rgb)

            cm.set_input(interpreter, pil_im)

            interpreter.invoke()

            objs = cm.get_output(
                interpreter,
                score_threshold=SCORE_THRESHOLD,
                top_k=TOP_K
            )

            human_detected = False

            for obj in objs:

                if labels.get(obj.id, "") == "person":

                    human_detected = True

                    h, w = frame.shape[:2]

                    x0 = int(obj.bbox.xmin * w)
                    y0 = int(obj.bbox.ymin * h)

                    x1 = int(obj.bbox.xmax * w)
                    y1 = int(obj.bbox.ymax * h)

                    cv2.rectangle(
                        frame,
                        (x0, y0),
                        (x1, y1),
                        (0, 255, 0),
                        2
                    )

                    break

        # =============================================
        # MOVEMENT CONTROL
        # =============================================

        if human_detected:

            move_forward(BASE_SPEED)

            print("HUMAN DETECTED -> MOVING")

        else:

            stop_all()

            print("NO HUMAN -> STOP")

        cv2.imshow("Human Detection", frame)

        if cv2.waitKey(1) & 0xFF == ord("q"):
            break

finally:

    stop_all()

    pwmA1.stop()
    pwmB1.stop()

    pwmA2.stop()
    pwmB2.stop()

    GPIO.cleanup()

    picam2.stop()

    cv2.destroyAllWindows()
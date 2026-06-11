# Vision-Based Human Following Robot

A real-time autonomous human-following robot developed using Raspberry Pi 4B, Pi Camera v1.3, TensorFlow Lite, and OpenCV.

The robot detects a person through a camera feed, tracks the person's position using centroid-based tracking, and follows the target by controlling DC motors through TB6612FNG motor drivers. The system is optimized for embedded AI applications and demonstrates the practical integration of computer vision, machine learning, and robotics.

---

## Features

* Real-time human detection using TensorFlow Lite
* Human following based on centroid tracking
* Camera-based distance estimation
* Raspberry Pi GPIO motor control
* Lightweight TensorFlow Lite inference
* Real-time video processing using OpenCV
* Embedded AI implementation on Raspberry Pi
* Portable and low-cost robotic platform

---

## Hardware Components

| Component              | Quantity    |
| ---------------------- | ----------- |
| Raspberry Pi 4B (4GB)  | 1           |
| Pi Camera v1.3         | 1           |
| TB6612FNG Motor Driver | 2           |
| DC Gear Motors         | 4           |
| LM2596 Buck Converter  | 2           |
| Li-ion Batteries       | 4           |
| Robot Chassis          | 1           |
| Wheels                 | 4           |
| Jumper Wires           | As Required |

---

## Software Stack

* Python
* OpenCV
* TensorFlow Lite
* Picamera2
* NumPy
* Pillow
* RPi.GPIO
* Raspberry Pi OS

---

## Project Structure

```text
Vision-Based-Human-Following-Robot
│
├── code
│   └── cam_test.py
│
├── report
│   └── Vision_Based_Human_Following_Robot_Report.pdf
│
├── presentation
│   └── Project_Presentation.pptx
│
├── images
│   ├── robot.jpg
│   ├── hardware_setup.jpg
│   ├── detection_output.jpg
│   ├── block_diagram.png
│   └── circuit_diagram.png
│
├── requirements.txt
│
└── README.md
```
---

## System Workflow

1. Pi Camera captures live video frames.
2. Raspberry Pi processes the frames using OpenCV.
3. TensorFlow Lite performs human detection.
4. Centroid-based tracking determines the person's position in the frame.
5. Movement decisions are generated based on the detected position.
6. Raspberry Pi sends GPIO control signals to the TB6612FNG motor drivers.
7. The robot follows the detected person and stops when the target reaches a predefined distance.

---

## Final Robot Prototype

![Robot Hardware](images/robot.jpg)


---


## Hardware Block Diagram

![Block Diagram](images/block_diagram.png)


---

## Circuit Diagram

Add your circuit diagram image here.

![Circuit Diagram](images/circuit_diagram.png)


---

## Human Detection Output

Real-time human detection using TensorFlow Lite running on Raspberry Pi 4B.


![Detection Output](images/detection_output.jpg)


---

## Performance Results

| Parameter             | Result                            |
| --------------------- | --------------------------------- |
| Human Detection       | Successful                        |
| Real-Time Tracking    | Successful                        |
| Human Following       | Successful                        |
| Motor Response        | Smooth                            |
| System Stability      | Good                              |
| Average FPS           | Optimized using N-Frame Detection |
| CPU Monitoring        | Implemented                       |
| Operating Temperature | Stable During Testing             |

---

## Performance Optimization

The system was optimized to improve real-time performance on Raspberry Pi 4B.

* TensorFlow Lite was used for lightweight inference.
* Frame skipping (N-frame detection) was implemented to reduce CPU load.
* Detection was performed periodically instead of on every frame.
* Lightweight MobileNet SSD model was used for faster execution.
* GPIO motor control was optimized for smooth movement.

---

## Future Scope

* Face Recognition
* Voice-Controlled Navigation
* Mobile Application Integration
* Multi-Person Tracking
* Gesture-Based Control
* Outdoor Autonomous Navigation

---

## Installation

Clone the repository:

```bash
git clone https://github.com/YOUR_USERNAME/Vision-Based-Human-Following-Robot.git
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Run the application:

```bash
python cam_test.py
```

---

## Important Note

The repository currently contains the primary project code and documentation. Additional supporting files such as TensorFlow Lite model files and helper modules will be uploaded when available from the Raspberry Pi project environment.

---

## Author

**Saadiya Farheen**

B.Tech – Computer Science & Engineering

Vision-Based Human Following Robot Project

# 🤖 Face-Controlled Servo with Arduino

### Let your robot “look” wherever you do!

---

### 👋 What’s the Idea?

This project started with a fun thought:
**"What if I could make a servo motor follow my face, just like a robotic eye?"**

So, I combined two powerful worlds — **computer vision** and **embedded systems**. The result? A webcam tracks your face, and a servo motor connected to an Arduino turns to follow your horizontal movement in real-time.

It’s like giving your robot its first bit of *curiosity* 👁️

---

### 🎥 What You’ll See in the Demo:

* I move my face side to side.
* A servo motor responds instantly, mimicking that direction.
* The motor stops when my face is centered.

👉 It’s smooth, responsive, and super fun to watch. *(You can find the video demo in this repo or attach it on GitHub/LinkedIn)*

---

### 🧩 What’s Happening Behind the Scenes?

Here’s how the magic unfolds:

#### 🧠 Python + OpenCV + MediaPipe

* Captures webcam video in real-time.
* Tracks 468 facial landmarks.
* Focuses on the **nose tip** to determine horizontal face position.
* Converts that position into a servo angle (0°–180°).
* Sends it to Arduino via **serial communication**.

#### 🤖 Arduino + Servo

* Listens for incoming angle data over the serial port.
* Rotates the servo to that exact position.

Just like that, you’ve got face-to-servo motion!

---

### 🛠️ What You Need

| Component                                        | Why It’s Needed                 |
| ------------------------------------------------ | ------------------------------- |
| Arduino board (Uno/Nano)                         | Main microcontroller            |
| SG90 Servo motor                                 | Physical motion                 |
| Jumper wires + USB                               | Connections + power             |
| Webcam                                           | Face tracking input             |
| Python (with OpenCV, MediaPipe, NumPy, pyserial) | Computer vision + communication |

---

### 🗂️ File Overview

* `faceMeshModule.py` – Modular class for face landmark detection using MediaPipe.
* `faceMovement.py`   – Main script to capture face movement and send angles to Arduino.
* `eyeController.ino` – Arduino sketch to rotate the servo based on received angles.

---

### 🚀 What You’ll Learn

This is more than just moving a servo. It teaches:

* Real-time **face tracking** using deep learning models.
* **Mapping physical motion** to computer vision.
* Serial communication between **Python and Arduino**.
* How hardware and software come together for interactive robotics.

---

### 🌱 Room to Grow

* Add vertical tracking (tilt control).
* Use dual servos for pan & tilt.
* Smooth out jitter with angle averaging.
* Make a robotic head that reacts to people in the room!

---

### ❤️ Why I Loved This

There’s something magical about building something that reacts to *you*.
Not just sensors or switches, but your presence, your face.

It’s a beautiful intersection of **creativity**, **engineering**, and a little bit of **science fiction**.


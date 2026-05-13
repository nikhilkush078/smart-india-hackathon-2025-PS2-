# 🎮 Motion-Controlled Interactive Brick Breaker

[![Event](https://img.shields.io/badge/Event-Smart%20India%20Hackathon%202025-blue)](https://www.sih.gov.in/)
[![Team](https://img.shields.io/badge/Team-RESISTOR-red)](#)
[![Theme](https://img.shields.io/badge/Theme-Toys%20%26%20Games-orange)](#)

> **"Transforming the player's body into the controller using computer vision and tactile feedback."**

This project is an immersive reimagining of the classic **Brick Breaker** game [cite: 771]. Developed for **Smart India Hackathon 2025**, it replaces traditional button inputs with real-time motion tracking and introduces a unique haptic penalty system using a wearable shock device [cite: 767, 773, 779].

---

## 🕹️ Core Gameplay Mechanics

The game creates a real-time interactive feedback loop between the digital environment and the physical player [cite: 812].

1. **Motion Control:** A camera (or mobile phone) tracks the player's horizontal position [cite: 772, 805]. Moving left or right in the real world moves the paddle on the screen in real-time [cite: 772].
2. **Haptic Feedback:** If the player fails to catch the ball and it falls, a wearable device on the wrist delivers a small electric shock as physical feedback [cite: 773, 811].
3. **Objective:** Move physically to hit the ball, break bricks, and evade a "Game Over" [cite: 882, 883, 884].

---

## 🛠️ Technical Architecture

The system is built using affordable, accessible hardware and efficient software libraries [cite: 826, 867].

### 💻 Software Stack
* **Python:** Used for video capture and image processing [cite: 805].
* **Computer Vision:** Utilizes libraries like **OpenCV** or **MediaPipe** for accurate feature detection and position calculation [cite: 832, 839].
* **Game Engine:** Custom logic for collision detection, trajectory updates, and game state management [cite: 841, 842, 843].

### 🔌 Hardware Components
* **NodeMCU (ESP8266):** Handles wireless communication between the laptop and the wearable device via a local server [cite: 806, 810].
* **Wearable Device:** Includes electrodes and a **transistor-transformer circuit** that steps up 1.5V to 100-200V for the shock feedback [cite: 807, 850].
* **Camera Input:** A standard mobile phone camera is used for low-cost video capture [cite: 805, 814].

---

## 🚀 Impact & Benefits

* **Increased Immersion:** Combining physical movement with unique sensory feedback creates a deeper level of engagement than traditional games [cite: 774, 888].
* **Physical Health:** Promotes active participation and improves reflexes and hand-eye coordination [cite: 866, 891].
* **Low Cost:** Reduces the need for specialized controllers or expensive VR hardware [cite: 867, 869].
* **Educational Value:** Serves as a platform for learning STEM concepts, electronics, and game design [cite: 878, 893, 894].

---

## 📽️ Project Demonstration

Watch the motion tracking in action and see the integration of the wearable feedback system:

[![Watch the Video](https://img.shields.io/badge/YouTube-Watch%20Video-red?style=for-the-badge&logo=youtube)](https://youtu.be/DGcBj6XW0Ik?si=pYXWlPruaaEcNBhq)

---

## 👨‍🔬 The Team
* **Team RESISTOR** (ID: 68037) [cite: 761, 762]

---
*Developed as part of Student Innovation: Swadeshi for Atmanirbhar Bharat [cite: 754].*

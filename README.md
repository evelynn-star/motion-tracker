# 🖐️ Motion & Gesture Tracker

> Real-time hand gesture detection and face tracking using Computer Vision  
> *Educational project by Evelina, 2026*

## 📋 Overview

This Python application uses **MediaPipe** and **OpenCV** to detect and track hand landmarks, recognize gestures, and overlay face mesh in real-time through your webcam. Built while exploring Computer Vision and Human-Computer Interaction concepts.

## ✨ Features

- 👆 **Hand Landmark Detection** — Track 21 key points on each hand
-  **Gesture Recognition** — Detect finger positions and basic gestures
- 👤 **Face Mesh Overlay** — Optional 468-point face landmark tracking
- 🎮 **Interactive Controls** — Keyboard shortcuts for real-time interaction
- 📊 **Visual Feedback** — Colored markers and connections for clear visualization
- ⚡ **Real-time Processing** — Optimized for smooth ~30 FPS performance

## 🛠️ Tech Stack

- **Language**: Python 3.10+
- **Core Libraries**: 
  - OpenCV (cv2) — Video capture and image processing
  - MediaPipe — ML-powered hand and face detection
  - NumPy — Numerical operations and coordinate transformations
- **Concepts**: 
  - Landmark detection and tracking
  - RGB/HSV color space conversion
  - Real-time video stream processing
  - Modular object-oriented design

## 🚀 Installation & Setup

### Prerequisites
- Python 3.10 or higher
- Webcam

### Step-by-step

1. **Install dependencies**
   pip install -r requirements.txt
2. **Run the application**
   python Detecting_project.py
3. 🎮 Controls

| Key | Action |
|-----|--------|
| `Q` or `Esc` | Quit the application |
| `F` | Toggle face mesh tracking ON/OFF |
| `1` | Track thumb tip (landmark #4) |
| `2` | Track index finger tip (landmark #8) |
| `3` | Track middle finger tip (landmark #12) |
| `4` | Track ring finger tip (landmark #16) |
| `5` | Track pinky tip (landmark #20) |
| `Space` | Toggle gesture detection 

## 📸 Demo

*Demo GIF coming soon!*

## 👩‍💻 Author

**Evelina**  
🎓 Aspiring Computer Science student  
📍 Russia  
🌱 Currently preparing for university applications

## 📄 License

This project is open source and available for educational purposes. Feel free to use, modify, and learn from it!

---

*Part of my Computer Science portfolio for university applications. Built with ❤️ while learning Computer Vision.


   




# 🎯 Z-ULTRA Crosshair Engine V2.0

![License](https://img.shields.io/badge/license-MIT-blue.svg)
![Python](https://img.shields.io/badge/python-3.10%2B-brightgreen.svg)
![Build](https://img.shields.io/badge/build-passing-brightgreen.svg)
![Platform](https://img.shields.io/badge/platform-Windows-lightgrey.svg)

**Z-ULTRA** is a professional-grade, high-performance external crosshair overlay designed for competitive gamers. Built with **PyQt6**, it provides a seamless, lag-free experience that sits on top of any game without interfering with system files or game memory.

---

## ✨ Elite Features

- **🚀 Ultra-Fast Performance:** Utilizes GPU acceleration to ensure zero input lag and smooth rendering.
- **🛡️ 100% External & Safe:** Runs as a pure transparent overlay. No memory injection or DLL hooking, making it undetectable by most anti-cheat systems.
- **🎨 Real-Time Customization:** Instantly adjust shapes, colors, size, thickness, and opacity while in-game.
- **🖼️ Custom Asset Support:** Upload any transparent `.png` image and turn it into your own custom crosshair.
- **🔳 Advanced Reticle Shapes:** Includes professional presets like **Plus**, **T-Shape**, **Dot**, **Circle**, and **Arrows**.
- **🖱️ Zero-Interference Click-Through:** The overlay is invisible to mouse input; your clicks pass through directly to the game.
- **💾 Auto-Save Profiles:** Automatically saves your last configuration to a `config.json` file for persistence.
- **🔇 Stealth Mode:** Runs without a console window (GUI only).

---

## 🚀 Installation & Setup

### 1. Prerequisites
Ensure you have Python 3.10 or higher installed. Then, install the required library:
```bash
pip install PyQt6
2. Running the Engine
Run the main script using:


python main.py
(Note: Rename to main.pyw to run without a console window manually, or compile to EXE.)

🛠️ Compilation (Create EXE)
To distribute this as a standalone application without a console window:


pip install pyinstaller
pyinstaller --onefile --noconsole --collect-all PyQt6 main.py
🎮 How to Use
Launch the Engine: Open the application before or after starting your game.

Engine Mode: Select your preferred shape from the dropdown menu.

Load PNG: Use this to import custom crosshair designs.

Transform: Adjust the sliders to match your screen resolution and preferred scale.

Save Profile: Click to set your current settings as default for future sessions.

📂 Project Structure
Plaintext
├── Crosshair_Pro_Elite_V2.0.exe              # Core Engine & Settings UI
├── config.json          # Auto-generated configuration file
└── README.md            # Documentation
📜 License
This project is licensed under the MIT License. Feel free to use, modify, and distribute.

⚠️ Disclaimer
This tool is intended as a gaming utility. While it is an external overlay and does not modify game files, always refer to the specific Terms of Service of the games you play regarding the use of overlays.

Developed with ❤️ for the Competitive Gaming Community.
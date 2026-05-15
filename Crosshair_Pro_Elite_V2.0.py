import sys
import os
import json
import ctypes
from PyQt6.QtWidgets import (QApplication, QMainWindow, QWidget, QVBoxLayout, 
                             QHBoxLayout, QPushButton, QColorDialog, QSlider, 
                             QLabel, QComboBox, QFileDialog, QFrame)
from PyQt6.QtCore import Qt, QPoint, QRect, QTimer
from PyQt6.QtGui import QPainter, QPen, QColor, QPixmap, QFont

class CrosshairOverlay(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowFlags(Qt.WindowType.FramelessWindowHint | 
                            Qt.WindowType.WindowStaysOnTopHint | 
                            Qt.WindowType.Tool | 
                            Qt.WindowType.WindowTransparentForInput)
        self.setAttribute(Qt.WidgetAttribute.WA_TranslucentBackground)
        
        screen = QApplication.primaryScreen().size()
        self.sw, self.sh = screen.width(), screen.height()
        self.setGeometry(0, 0, self.sw, self.sh)

        self.mode = "Plus"
        self.color = QColor(0, 255, 0)
        self.size = 20
        self.thickness = 2
        self.opacity = 255
        self.custom_img = None
        self.is_visible = True

    def paintEvent(self, event):
        if not self.is_visible: return
        
        painter = QPainter(self)
        painter.setRenderHint(QPainter.RenderHint.Antialiasing)
        painter.setOpacity(self.opacity / 255)
        
        cx, cy = self.sw // 2, self.sh // 2
        
        if self.mode == "Custom Image" and self.custom_img:
            rect = QRect(cx - self.size//2, cy - self.size//2, self.size, self.size)
            painter.drawPixmap(rect, self.custom_img)
            return

        pen = QPen(self.color, self.thickness)
        painter.setPen(pen)

        if self.mode == "Plus":
            painter.drawLine(cx, cy - self.size//2, cx, cy + self.size//2)
            painter.drawLine(cx - self.size//2, cy, cx + self.size//2, cy)
        elif self.mode == "Dot":
            painter.setBrush(self.color)
            painter.drawEllipse(cx - self.thickness, cy - self.thickness, self.thickness*2, self.thickness*2)
        elif self.mode == "Circle":
            painter.drawEllipse(cx - self.size//2, cy - self.size//2, self.size, self.size)
        elif self.mode == "T-Shape":
            painter.drawLine(cx, cy, cx, cy + self.size//2)
            painter.drawLine(cx - self.size//2, cy, cx + self.size//2, cy)

class ModernSettings(QWidget):
    def __init__(self, overlay):
        super().__init__()
        self.overlay = overlay
        self.setWindowTitle("Z-ULTRA SETTINGS")
        self.setFixedSize(350, 600)
        self.setStyleSheet("background-color: #121212; color: white;")
        
        main_layout = QVBoxLayout()
        
        header = QLabel("CROSSHAIR ENGINE V2.0")
        header.setFont(QFont("Impact", 24))
        header.setStyleSheet("color: #00FFD4; margin-bottom: 10px;")
        header.setAlignment(Qt.AlignmentFlag.AlignCenter)
        main_layout.addWidget(header)

        self.add_section(main_layout, "VISUAL MODE")
        self.combo = QComboBox()
        self.combo.addItems(["Plus", "Dot", "Circle", "T-Shape", "Custom Image"])
        self.combo.setStyleSheet("background: #333; padding: 5px;")
        self.combo.currentTextChanged.connect(self.update_engine)
        main_layout.addWidget(self.combo)

        self.btn_img = self.create_button("UPLOAD ASSET (PNG)", self.upload_image)
        main_layout.addWidget(self.btn_img)

        self.add_section(main_layout, "COLOR & ALPHA")
        self.btn_color = self.create_button("PICK ENGINE COLOR", self.choose_color)
        main_layout.addWidget(self.btn_color)

        self.opacity_slider = self.create_slider(0, 255, 255, self.update_engine)
        main_layout.addWidget(QLabel("Opacity:"))
        main_layout.addWidget(self.opacity_slider)

        self.add_section(main_layout, "DIMENSIONS")
        self.size_slider = self.create_slider(4, 150, 20, self.update_engine)
        main_layout.addWidget(QLabel("Size:"))
        main_layout.addWidget(self.size_slider)

        self.thick_slider = self.create_slider(1, 15, 2, self.update_engine)
        main_layout.addWidget(QLabel("Thickness:"))
        main_layout.addWidget(self.thick_slider)

        main_layout.addStretch()
        
        self.save_btn = self.create_button("SAVE PROFILE", self.save_config)
        self.save_btn.setStyleSheet("background-color: #00FFD4; color: black; font-weight: bold;")
        main_layout.addWidget(self.save_btn)

        self.setLayout(main_layout)

    def add_section(self, layout, text):
        line = QFrame()
        line.setFrameShape(QFrame.Shape.HLine)
        line.setStyleSheet("color: #444;")
        layout.addWidget(QLabel(text))
        layout.addWidget(line)

    def create_button(self, text, func):
        btn = QPushButton(text)
        btn.setHeight = 40
        btn.setStyleSheet("background: #222; border: 1px solid #00FFD4; padding: 10px;")
        btn.clicked.connect(func)
        return btn

    def create_slider(self, mn, mx, val, func):
        s = QSlider(Qt.Orientation.Horizontal)
        s.setRange(mn, mx)
        s.setValue(val)
        s.valueChanged.connect(func)
        return s

    def update_engine(self):
        self.overlay.mode = self.combo.currentText()
        self.overlay.size = self.size_slider.value()
        self.overlay.thickness = self.thick_slider.value()
        self.overlay.opacity = self.opacity_slider.value()
        self.overlay.update()

    def choose_color(self):
        c = QColorDialog.getColor()
        if c.isValid():
            self.overlay.color = c
            self.overlay.update()

    def upload_image(self):
        path, _ = QFileDialog.getOpenFileName(self, "Asset Explorer", "", "PNG (*.png)")
        if path:
            self.overlay.custom_img = QPixmap(path)
            self.overlay.mode = "Custom Image"
            self.combo.setCurrentText("Custom Image")
            self.overlay.update()

    def save_config(self):
        config = {
            "mode": self.overlay.mode,
            "size": self.overlay.size,
            "thick": self.overlay.thickness,
            "color": self.overlay.color.name()
        }
        with open("config.json", "w") as f:
            json.dump(config, f)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    overlay = CrosshairOverlay()
    overlay.show()
    settings = ModernSettings(overlay)
    settings.show()
    sys.exit(app.exec())
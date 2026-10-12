#imports
from PySide6.QtWidgets import QApplication, QLabel, QPushButton, QWidget, QFrame
import sys

#global variables
name = "Yasser"

#application
app = QApplication(sys.argv)

#window
window = QWidget()
window.resize(1920, 1080)
window.setWindowTitle("System")
window.setStyleSheet("background-color: #111318;")


Title_label = QLabel("The System", window)
Title_label.setStyleSheet("""
    QLabel {
        font-size: 58px;
        color: #00FFDD;
        font-weight: bold;
    }
""")
Title_label.move(0, 0)

greet = QLabel(f"Welcome {name}", window)
greet.move(450, 30)
greet.setStyleSheet("""
    QLabel {
        font-size: 48px;
        color : #0095FF;
        font-weight: bold;
    }
""")

#buttons/side bars
Dashboard_button = QPushButton("Dashboard", window)
Dashboard_button.move(40, 90)
Dashboard_button.resize(250, 50)

timer_button = QPushButton("Timer", window)
timer_button.move(40, 140)
timer_button.resize(250, 50)

stats_button = QPushButton("Stats", window)
stats_button.move(40, 190)
stats_button.resize(250, 50)



window.show()
sys.exit(app.exec())
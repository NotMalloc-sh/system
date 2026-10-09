from PySide6.QtWidgets import QApplication, QLabel, QPushButton, QWidget 
import sys

app = QApplication(sys.argv)

#window
window = QWidget()
window.resize(1920, 1080)
window.setWindowTitle("System")
window.setStyleSheet("background-color: #111318;")



window.show()
sys.exit(app.exec())
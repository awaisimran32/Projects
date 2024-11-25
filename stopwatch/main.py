import sys

from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QPushButton, QHBoxLayout, QVBoxLayout
from PyQt5.QtCore import QTimer,QTime,Qt
from pygame.examples.vgrade import stopwatch


class Stopwatch(QWidget):
    def __init__(self):
        super().__init__()
        self.time=QTime(0,0,0,0)
        self.time_label=QLabel("00:00:00.00",self)
        self.start_button=QPushButton("Start",self)
        self.stop_button=QPushButton("Stop",self)
        self.reset_button=QPushButton("Reset",self)
        self.timer=QTimer(self)
        self.initUI()
    def initUI(self):
        self.setWindowTitle("Stopwatch")
        self.setWindowIcon(QIcon("stopwatch.png"))
        vbox=QVBoxLayout()
        vbox.addWidget(self.time_label)

        self.setLayout(vbox)


        hbox=QHBoxLayout()
        hbox.addWidget(self.start_button)
        hbox.addWidget(self.stop_button)
        hbox.addWidget(self.reset_button)

        vbox.addLayout(hbox)

        self.time_label.setAlignment(Qt.AlignCenter)



        self.setStyleSheet("""
            QPushButton,QLabel{
            padding:20px;
            font-weight:bold;
            
            }
            
            QPushButton{
                font-size:50px;
            }
            QLabel{
            font-size:120px;
            background-color:hsl(103, 100%, 50%);
            border-radius:20px;
            }
        """)

        self.start_button.clicked.connect(self.start)
        self.stop_button.clicked.connect(self.stop)
        self.reset_button.clicked.connect(self.reset)
        self.timer.timeout.connect(self.update_display)
        self.stop_button.setEnabled(False)

    def start(self):
        self.timer.start(10)
        self.start_button.setEnabled(False)
        self.stop_button.setEnabled(True)
    def stop(self):
        self.timer.stop()
        self.start_button.setEnabled(True)
        self.stop_button.setEnabled(False)
    def reset(self):
        self.timer.stop()
        self.time=QTime(0,0,0,0)
        self.time_label.setText("00:00:00.00")
        self.start_button.setEnabled(True)
        self.stop_button.setEnabled(False)
    @staticmethod
    def format_time(time):
        hours=time.hour()
        minutes=time.minute()
        seconds=time.second()
        milliseconds=time.msec()
        return f"{hours:02}:{minutes:02}:{seconds:02}.{milliseconds:02}"
    def update_display(self):
        self.time=self.time.addMSecs(10)
        self.time_label.setText(self.format_time(self.time))




if __name__=="__main__":
    app=QApplication(sys.argv)
    stopwatch=Stopwatch()
    stopwatch.show()
    sys.exit(app.exec_())
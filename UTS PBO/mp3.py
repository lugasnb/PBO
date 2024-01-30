import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton, QFileDialog
from PyQt5.QtMultimedia import QMediaPlayer, QMediaContent

class PemutarMusik(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Aplikasi Pemutar Musik")
        self.setGeometry(100, 100, 400, 200)

        self.layout = QVBoxLayout()

        self.media_player = QMediaPlayer()
        self.button_pilih_musik = QPushButton("Pilih Musik")
        self.button_mainkan = QPushButton("Play")
        self.button_pause = QPushButton("Pause")
        self.button_stop = QPushButton("Stop")

        self.layout.addWidget(self.button_pilih_musik)
        self.layout.addWidget(self.button_mainkan)
        self.layout.addWidget(self.button_pause)
        self.layout.addWidget(self.button_stop)

        self.button_mainkan.setEnabled(False)
        self.button_pause.setEnabled(False)
        self.button_stop.setEnabled(False)

        self.button_pilih_musik.clicked.connect(self.pilih_musik)
        self.button_mainkan.clicked.connect(self.mainkan_musik)
        self.button_pause.clicked.connect(self.pause_musik)
        self.button_stop.clicked.connect(self.stop_musik)

        self.setLayout(self.layout)

    def pilih_musik(self):
        nama_file, _ = QFileDialog.getOpenFileName(self, "Pilih File Musik", "", "File Musik (*.mp3 *.wav)")
        if nama_file:
            self.media_player.setMedia(QMediaContent(QUrl.fromLocalFile(nama_file)))
            self.button_mainkan.setEnabled(True)
            self.button_pause.setEnabled(True)
            self.button_stop.setEnabled(True)

    def mainkan_musik(self):
        self.media_player.play()

    def pause_musik(self):
        self.media_player.pause()

    def stop_musik(self):
        self.media_player.stop()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    pemutar_musik = PemutarMusik()
    pemutar_musik.show()
    sys.exit(app.exec_())

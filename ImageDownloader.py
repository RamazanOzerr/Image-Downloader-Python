import string
import sys
import requests
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QPushButton
from PyQt5.QtGui import QPixmap
import random

class ImageDownloader(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        # create GUI elements
        urlLabel = QLabel("URL:", self)
        pathLabel = QLabel("Save Path:", self)
        self.urlEdit = QLineEdit(self)
        self.pathEdit = QLineEdit(self)
        downloadButton = QPushButton("Download", self)
        imageLabel = QLabel(self)

        # set GUI elements
        urlLabel.move(20, 20)
        self.urlEdit.move(100, 20)
        pathLabel.move(20, 50)
        self.pathEdit.move(100, 50)
        downloadButton.move(100, 80)
        imageLabel.move(20, 110)

        # downloads the pic when pressed to the Download button
        downloadButton.clicked.connect(self.downloadImage)

        self.setGeometry(300, 300, 400, 200)
        self.setWindowTitle("Pic Downloader")
        self.show()

    def downloadImage(self):
        # Download the pic by using the url and path taken from the user
        random_name = self.generate_random_string(10)
        image_url = self.urlEdit.text()
        save_path = self.pathEdit.text() + "/"+ random_name + ".jpg"
        response = requests.get(image_url)
        image_data = response.content

        # Save the pic into file system
        with open(save_path, "wb") as f:
            f.write(image_data)

        # show the pic has been downloaded
        pixmap = QPixmap(save_path)
        self.imageLabel.setPixmap(pixmap)
        self.imageLabel.setScaledContents(True)

    def generate_random_string(self,length: int) -> str:
        return "".join(random.choices(string.ascii_letters + string.digits, k=length))


if __name__ == "__main__":
    app = QApplication(sys.argv)
    ex = ImageDownloader()
    sys.exit(app.exec_())

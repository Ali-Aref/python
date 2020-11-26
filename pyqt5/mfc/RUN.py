from faceRecognaization import Ui_MainWindow as main
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox
import face_recognition
import cv2
import os


class Ui_MainWindow(main):
    def setupUi(self, MainWindow):
        main.setupUi(self, MainWindow)
        self.pushButtonSelectPhoto.clicked.connect(self.selectImgClicked)
        self.pushButtonRecognation.clicked.connect(self.recongationButtonClicked)
        self.pushButtonWhoIs.clicked.connect(self.whoIsClikced)
        self.known_faces = []
        self.known_names = []

    def selectImgClicked(self):
        fileName, _ = QtWidgets.QFileDialog.getOpenFileName(
            None, "Select Image", "", "Image Files (*.png *.jpg *.jpeg)"
        )
        if fileName:
            self.name = fileName
            pixmap = QtGui.QPixmap(fileName).scaled(
                self.ImgLable.width(), self.ImgLable.height(), QtCore.Qt.KeepAspectRatio
            )
            self.ImgLable.setPixmap(pixmap)

    def recongationButtonClicked(self):
        image = face_recognition.load_image_file(self.name)
        image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)
        face_locations = face_recognition.face_locations(image)
        if face_locations:
            for face in face_locations:
                top_left = (face[3], face[0])
                bottom_right = (face[1], face[2])
                cv2.rectangle(image, top_left, bottom_right, [0, 0, 255], 2)
            cv2.imwrite(f"{self.name}-processed.jpg", image)
            pixmap = QtGui.QPixmap(f"{self.name}-processed.jpg").scaled(
                self.ImgLable.width(), self.ImgLable.height(), QtCore.Qt.KeepAspectRatio
            )
            self.ImgLable.setPixmap(pixmap)
            os.remove(f"{self.name}-processed.jpg")
        else:
            QMessageBox.about(
                MainWindow,
                "No Face Detected!",
                "Please Try an other photo or get sure the photo is protiated.",
            )

    def whoIsClikced(self):
        # loading known faces
        for name in os.listdir("known"):
            for fileName in os.listdir(f"known/{name}"):
                image = face_recognition.load_image_file(f"known/{name}/{fileName}")
                encoding = face_recognition.face_encodings(image)[0]
                self.known_faces.append(encoding)
                self.known_names.append(name)

        # image comparing
        print("now image comparing time..\nget the inputed image details..")
        image = face_recognition.load_image_file(self.name)
        locations = face_recognition.face_locations(image, model="cnn")
        encodings = face_recognition.face_encodings(image, locations)
        image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)

        for face_encoding, face_location in zip(encodings, locations):
            results = face_recognition.compare_faces(self.known_faces, face_encoding, 0.6)  # 0.6 tolerance
            match = None
            print(f"this is results : {results}")
            if True in results:
                match = self.known_names[results.index(True)]
                top_left = (face_location[3], face_location[0])
                bottom_right = (face_location[1], face_location[2])
                color = [0, 0, 255]
                cv2.rectangle(image, top_left, bottom_right, color, 2)

                top_left = (face_location[3], face_location[2])
                bottom_right = (face_location[1], face_location[2] + 25)
                color = [0, 0, 255]
                cv2.rectangle(image, top_left, bottom_right, color, cv2.FILLED)
                cv2.putText(
                    image,
                    match,
                    (face_location[3] + 10, face_location[2] + 15),
                    cv2.FONT_HERSHEY_SIMPLEX,
                    0.8,  # font size
                    (200, 200, 200),  # color
                    2,  # font thickness
                )
                cv2.imwrite(f"{self.name}-processed.jpg", image)
                pixmap = QtGui.QPixmap(f"{self.name}-processed.jpg").scaled(
                    self.ImgLable.width(), self.ImgLable.height(), QtCore.Qt.KeepAspectRatio
                )
                self.ImgLable.setPixmap(pixmap)
                os.remove(f"{self.name}-processed.jpg")

                print(f"match fooound he is : {match}")
            else:
                top_left = (face_location[3], face_location[0])
                bottom_right = (face_location[1], face_location[2])
                color = [0, 0, 255]
                cv2.rectangle(image, top_left, bottom_right, color, 2)

                top_left = (face_location[3], face_location[2])
                bottom_right = (face_location[1], face_location[2] + 25)
                color = [0, 0, 255]
                cv2.rectangle(image, top_left, bottom_right, color, cv2.FILLED)
                cv2.putText(
                    image,
                    "Unknown",
                    (face_location[3] + 10, face_location[2] + 15),
                    cv2.FONT_HERSHEY_SIMPLEX,
                    0.8,  # font size
                    (200, 200, 200),  # font color
                    2,  # font thickness
                )
                cv2.imwrite(f"{self.name}-processed.jpg", image)
                pixmap = QtGui.QPixmap(f"{self.name}-processed.jpg").scaled(
                    self.ImgLable.width(), self.ImgLable.height(), QtCore.Qt.KeepAspectRatio
                )
                self.ImgLable.setPixmap(pixmap)
                os.remove(f"{self.name}-processed.jpg")
                print("no match found!")


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

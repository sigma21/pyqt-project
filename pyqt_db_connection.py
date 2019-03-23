import sys
import sqlite3
from PyQt5 import QtWidgets

class Window(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.init_ui()
        self.connect()

    def connect(self):
        connection = sqlite3.connect("chinook.db")
        self.cursor = connection.cursor()
        connection.commit()

    def init_ui(self):
        self.albumId = QtWidgets.QLineEdit()
        self.text_area_1 = QtWidgets.QLabel("Album ID")
        self.title = QtWidgets.QLineEdit()
        self.text_area_2 = QtWidgets.QLabel("Title")
        self.artistId = QtWidgets.QLineEdit()
        self.text_area_3 = QtWidgets.QLabel("Artist ID")
        self.text_area_4 = QtWidgets.QLabel("")
        self.add_album = QtWidgets.QPushButton("Add Album")
        self.clear = QtWidgets.QPushButton("Clear")
        self.find = QtWidgets.QPushButton("Find")
        self.update = QtWidgets.QPushButton("Update")

        v_box = QtWidgets.QVBoxLayout()

        v_box.addWidget(self.text_area_1)
        v_box.addWidget(self.albumId)
        v_box.addWidget(self.text_area_2)
        v_box.addWidget(self.title)
        v_box.addWidget(self.text_area_3)
        v_box.addWidget(self.artistId)
        v_box.addWidget(self.text_area_4)

        v_box.addWidget(self.add_album)
        v_box.addWidget(self.find)
        v_box.addWidget(self.update)
        v_box.addWidget(self.clear)
        v_box.addStretch()


        h_box = QtWidgets.QHBoxLayout()
        h_box.addStretch()
        h_box.addLayout(v_box)
        h_box.addStretch()

        self.setLayout(h_box)
        self.setWindowTitle("Album Database")

        self.clear.clicked.connect(self._clear)
        self.add_album.clicked.connect(self._add_album)
        self.update.clicked.connect(self._update)
        self.find.clicked.connect(self._find)

        self.show()

    def _find(self):

        v1 = self.title.text()
        v2 = self.albumId.text()
        v3 = self.artistId.text()

        # self.cursor.execute("SELECT * FROM albums WHERE title LIKE '?'", (v2))
        self.cursor.execute("Select * From albums where title = ?", (v2,))

        data = self.cursor.fetchall()

        if len(data) == 0:
            self.text_area_4.setText("Album not found. Please try again.")
        else:
            self.text_area_4.setText(v2)

    def _clear(self):
        sender = self.sender()

        if sender.text() == "Clear":
            self.albumId.clear()
            self.title.clear()
            self.artistId.clear()

    def _update(self):
        pass

    def _add_album(self):
        album_id = self.albumId.text()
        title_name = self.title.text()
        artist_id = self.artistId.text()

        connection = sqlite3.connect("chinook.db")
        self.cursor = connection.cursor()
        self.cursor.execute("INSERT into albums VALUES(?,?,?)", (album_id, title_name, artist_id))
        connection.commit()






app = QtWidgets.QApplication(sys.argv)
window = Window()
sys.exit(app.exec_())
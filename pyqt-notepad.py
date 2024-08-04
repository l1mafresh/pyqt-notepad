import os
import sys
from platform import system
from PyQt6 import QtWidgets, QtCore, QtGui
from PyQt6.QtWidgets import QApplication, QMainWindow, QTextEdit, QStatusBar, QMenuBar, QMenu, QLabel, QFileDialog, QFontDialog, QMessageBox

class Window(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Notepad")
        self.resize(640,480)
        
        font = QtGui.QFont()

        self.text_edit = QTextEdit(self, font=font)
        self.setCentralWidget(self.text_edit)

        self.status_bar = QStatusBar(self)
        self.setStatusBar(self.status_bar)
        
        self.menu_bar = QMenuBar(self)
        self.setMenuBar(self.menu_bar)
        
        file_menu = QMenu("&File", self)
        self.menu_bar.addMenu(file_menu)
        view_menu = QMenu("&View", self)
        self.menu_bar.addMenu(view_menu)
        about_menu = QMenu("&About", self)
        self.menu_bar.addMenu(about_menu)
        
        open_file = file_menu.addAction("Open", self.action_clicked)
        save_file = file_menu.addAction("Save as", self.action_clicked)

        view_menu.addAction("System", self.action_clicked)
        view_menu.addAction("Light", self.action_clicked)
        view_menu.addAction("Dark", self.action_clicked)
        view_menu.addAction("Sepia", self.action_clicked)
        view_menu.addSeparator()
        font_settings = view_menu.addAction("Font settings", self.action_clicked)

        about = about_menu.addAction("About program", self.action_clicked)
        
        if system() == "Linux":
            self.setWindowIcon(QtGui.QIcon.fromTheme(u"accessories-text-editor"))
            open_file.setIcon(QtGui.QIcon.fromTheme(u"document-open"))
            save_file.setIcon(QtGui.QIcon.fromTheme(u"document-save-as"))
            font_settings.setIcon(QtGui.QIcon.fromTheme(u"font-x-generic"))
            about.setIcon(QtGui.QIcon.fromTheme(u"help-about"))
        else:
            self.setWindowIcon(QtGui.QIcon(os.path.join(os.path.dirname(os.path.abspath(__file__)), "icon.png")))

        self.char_count_label = QLabel("Characters: 0", alignment=QtCore.Qt.AlignmentFlag.AlignCenter)
        self.status_bar.addWidget(self.char_count_label)

        self.text_edit.textChanged.connect(self.update_char_count)

    @QtCore.pyqtSlot()
    def action_clicked(self):
        action = self.sender()
        
        if action.text() == "Open":
            fname = QFileDialog.getOpenFileName(self)[0]
            if fname:
                try:
                    with open(fname, "r") as f:
                        data = f.read()
                        self.text_edit.setText(data)
                except:
                    QMessageBox.warning(self, "Error", "Unsupported file type")  
        elif action.text() == "Save as":
            fname = QFileDialog.getSaveFileName(self, filter="Text Files (*.txt)")[0]
            if fname:
                if not fname.endswith(".txt"):
                    fname += ".txt"
                with open(fname, "w") as f:
                    text = self.text_edit.toPlainText()
                    f.write(text)

        elif action.text() == "System":
            self.setStyleSheet("")
        elif action.text() == "Light":
            self.setStyleSheet("background-color: white; color: black;")
        elif action.text() == "Dark":
            self.setStyleSheet("background-color: black; color: white;")
        elif action.text() == "Sepia":
            self.setStyleSheet("background-color: #f4ecd8; color: #5b4636;")

        elif action.text() == "Font settings":
            font, ok = QFontDialog.getFont(self.text_edit.font(), self, "Choose Font")
            if ok:
                self.text_edit.setFont(font)

        elif action.text() == "About program":
            QMessageBox.information(self, "Notepad",
                                "Lightweight notepad, writed \non Python and PyQt6 by limafresh.")

    def update_char_count(self):
        text_length = len(self.text_edit.toPlainText())
        self.char_count_label.setText(f"Characters: {text_length}")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Window()
    window.show()
    sys.exit(app.exec())

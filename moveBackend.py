from PySide2 import QtCore, QtWidgets, QtGui
import about
import sys
# import qdarkstyle
import os
import glob
import logging
import shutil
import icons_rc



class Ui_MainWindow(object):

    """This is the UI for the application"""

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(357, 170)
        MainWindow.setMinimumSize(QtCore.QSize(357, 170))
        MainWindow.setMaximumSize(QtCore.QSize(357, 170))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/newPrefix/cool-icon-32218-Windows.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.splitter = QtWidgets.QSplitter(self.centralwidget)
        self.splitter.setGeometry(QtCore.QRect(50, 60, 251, 21))
        self.splitter.setOrientation(QtCore.Qt.Horizontal)
        self.splitter.setObjectName("splitter")
        self.label = QtWidgets.QLabel(self.splitter)
        self.label.setMaximumSize(QtCore.QSize(57, 16777215))
        self.label.setStyleSheet("font: 10pt \"Segoe UI\";")
        self.label.setObjectName("label")
        self.folderName = QtWidgets.QLineEdit(self.splitter)
        self.folderName.setClearButtonEnabled(False)
        self.folderName.setObjectName("folderName")
        self.openFolder = QtWidgets.QToolButton(self.splitter)
        self.openFolder.setContextMenuPolicy(QtCore.Qt.DefaultContextMenu)
        self.openFolder.setObjectName("openFolder")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(40, 10, 311, 31))
        font = QtGui.QFont()
        font.setFamily("Palatino Linotype")
        font.setPointSize(14)
        font.setWeight(9)
        font.setItalic(False)
        font.setBold(False)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("\n"
"font: 75 14pt \"Palatino Linotype\";")
        self.label_2.setObjectName("label_2")
        self.splitter_2 = QtWidgets.QSplitter(self.centralwidget)
        self.splitter_2.setGeometry(QtCore.QRect(110, 90, 191, 28))
        self.splitter_2.setOrientation(QtCore.Qt.Horizontal)
        self.splitter_2.setObjectName("splitter_2")
        self.okButton = QtWidgets.QPushButton(self.splitter_2)
        self.okButton.setEnabled(False)
        self.okButton.setMinimumSize(QtCore.QSize(92, 28))
        self.okButton.setMaximumSize(QtCore.QSize(92, 28))
        self.okButton.setObjectName("okButton")
        self.CancelButton = QtWidgets.QPushButton(self.splitter_2)
        self.CancelButton.setMinimumSize(QtCore.QSize(93, 28))
        self.CancelButton.setMaximumSize(QtCore.QSize(93, 28))
        self.CancelButton.setObjectName("CancelButton")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 357, 26))
        self.menubar.setObjectName("menubar")
        self.menuAbout = QtWidgets.QMenu(self.menubar)
        self.menuAbout.setObjectName("menuAbout")
        MainWindow.setMenuBar(self.menubar)
        self.actionAbout = QtWidgets.QAction(MainWindow)
        self.actionAbout.setObjectName("actionAbout")
        self.menuAbout.addAction(self.actionAbout)
        self.menubar.addAction(self.menuAbout.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QtWidgets.QApplication.translate("MainWindow", "File Mover", None, -1))
        self.label.setText(QtWidgets.QApplication.translate("MainWindow", "Folder : ", None, -1))
        self.openFolder.setToolTip(QtWidgets.QApplication.translate("MainWindow", "Shortcut : Ctrl + o", None, -1))
        self.openFolder.setText(QtWidgets.QApplication.translate("MainWindow", "...", None, -1))
        self.openFolder.setShortcut(QtWidgets.QApplication.translate("MainWindow", "Ctrl+O", None, -1))
        self.label_2.setText(QtWidgets.QApplication.translate("MainWindow", "Enter the Folder path below", None, -1))
        self.okButton.setToolTip(QtWidgets.QApplication.translate("MainWindow", "Shortcut : Enter", None, -1))
        self.okButton.setText(QtWidgets.QApplication.translate("MainWindow", "OK", None, -1))
        self.okButton.setShortcut(QtWidgets.QApplication.translate("MainWindow", "Return", None, -1))
        self.CancelButton.setToolTip(QtWidgets.QApplication.translate("MainWindow", "Shortcut : Esc", None, -1))
        self.CancelButton.setText(QtWidgets.QApplication.translate("MainWindow", "Cancel", None, -1))
        self.CancelButton.setShortcut(QtWidgets.QApplication.translate("MainWindow", "Esc", None, -1))
        self.menuAbout.setTitle(QtWidgets.QApplication.translate("MainWindow", "About", None, -1))
        self.actionAbout.setText(QtWidgets.QApplication.translate("MainWindow", "About", None, -1))
        self.actionAbout.setShortcut(QtWidgets.QApplication.translate("MainWindow", "Ctrl+T", None, -1))


class cop(Ui_MainWindow,QtWidgets.QMainWindow):

    """This is the backend for the application"""
    def __init__(self):

        super().__init__()
        self.setupUi(self)
        # self.setStyleSheet(qdarkstyle.load_stylesheet_pyside2())

        self.folderName.setFocus() #This sets focus on QLineEdit automatically at the start of the app
        self.folderName.textChanged.connect(self.check) #when text is changed in QLineEdit, it checks whether it is empty or not, and accordingly enables and disables the OKButton
        self.openFolder.clicked.connect(self.getFolder)
        self.okButton.clicked.connect(self.moveFunction)
        self.CancelButton.clicked.connect(sys.exit)
        self.actionAbout.triggered.connect(self.showAbout)

    def getFolder(self):
        """
        This opens an open file dialogbox and gets the folder path only and then sets the qlinedit to the path
        """
        file = str(QtWidgets.QFileDialog.getExistingDirectory(self, "Select Directory"))#This gets the folder path as str into the variable
        self.folderName.setText(file)

    def moveFunction(self):

        """
        """
        try:
            self.path = os.path.abspath(self.folderName.text())#gets the path from qlineedit
            assert os.path.isdir(self.path), "Folder doesn't exist" #checking if it is a valid path or not, then gives out error message
        except Exception as e:
            self.errorMsg(str(e))#Opens error dialogbox with the above message
        else:
            os.chdir(self.path)#changes the working directory to that path
            extList = set(os.path.splitext(file)[-1] for file in os.listdir(self.path) if os.path.isfile(os.path.join(self.path, file)))#set of all  extensions in a folder
            ext_list = list(filter(None, extList))#removes empty strings from the list
            for exten in ext_list:
                self.moveSingleExtension(self.path, exten)
            self.doneMsg()#opens the completed dialogbox

    def errorMsg(self,m):
        msg = QtWidgets.QMessageBox.warning(self,"Error",m)

    def doneMsg(self):
        msg = QtWidgets.QMessageBox.information(self,"Done",'Completed')
        if msg == QtWidgets.QMessageBox.Ok:
            os.startfile(self.path)#when ok button is clicked, opens the des path in the explorer

    def check(self):
        """when text is changed in QLineEdit, it checks whether it is empty or not, and accordingly enables and disables the OKButton"""
        check = str(self.folderName.text())
        if check:
            self.okButton.setEnabled(True)
        else:
            self.okButton.setEnabled(False)

    def showAbout(self):
        """opens the about window"""
        self.dia = QtWidgets.QDialog()
        self.ui = about.Ui_Form()
        self.ui.setupUi(self.dia)
        self.dia.show()

    def moveSingleExtension(self, path, ext):
        """The main function to move the files. This is for a single extension
        """
        des = os.path.join(path, ext)
        if not os.path.exists(des):
            os.makedirs(des)
        # print(des)

        log_nam = os.path.join(des, 'move.log')
        # print(log_nam)
        logger = logging.getLogger(__name__)
        logger.setLevel(logging.INFO)

        formatter = logging.Formatter('%(asctime)s:%(levelname)s:%(message)s')
        file_handle = logging.FileHandler(log_nam)
        file_handle.setFormatter(formatter)

        logger.addHandler(file_handle)
        # logging.basicConfig(filename=log_nam, level=logging.INFO,
        #                     format='%(asctime)s:%(levelname)s:%(message)s')

        extFiles = glob.glob(os.path.abspath(f'{path}/*{ext}'))

        # logger = create_logger(des)
        if ext == ".html" or ext == '.htm':
            for files in extFiles:
                try:
                    shutil.move(files, des)
                    file_name = os.path.splitext(os.path.basename(files))[0]
                    # print(file_name)
                    # filenam, ext = os.path.splitext(file_name)
                    # print(filenam)
                    html_folder = file_name + '_files'
                    # print(html_folder)
                    if os.path.isdir(html_folder):
                        #print(html_folder)
                        shutil.move(html_folder, des)
                        logger.info("Moved '{2}' from '{0}' to '{1}'".format(os.path.dirname(files), des, html_folder))

                    logger.info("Moved '{2}' from '{0}' to '{1}'".format(os.path.dirname(files), des, files))
                except:
                    logger.error("'{}' already in destination folder".format(files))
        else:
            for files in extFiles:
                try:
                    shutil.move(files, des)
                    file_name = os.path.splitext(os.path.basename(files))[0]
                    logger.info("Moved '{2}' from '{0}' to '{1}'".format(os.path.dirname(files), des, files))
                except:
                    logger.error("'{}' already in destination folder".format(files))

        logger.info(f'\nProcess finished\n')
        # close_log(logger)
        # print('done')


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    kj = cop()
    kj.show()
    sys.exit(app.exec_())
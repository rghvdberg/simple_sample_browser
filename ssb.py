# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ssb.ui'
#
# Created by: PyQt5 UI code generator 5.5.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets, QtMultimedia
from PyQt5.QtWidgets import QTreeView,QFileSystemModel,QApplication


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("SSB")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.centralwidget)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")

        #
        # Directories
        #

        model_dir = QFileSystemModel()
        self.dirmodel = model_dir
        #print (self.model_dir)
        model_dir.setRootPath(homedir)
        root_dir = model_dir.setRootPath(homedir)
        # only directories
        model_dir.setFilter(QtCore.QDir.AllDirs|QtCore.QDir.NoDot)

        self.treeView_dir = QtWidgets.QTreeView(self.centralwidget)
        self.treeView_dir.setObjectName("treeView_dir")
        self.treeView_dir.setModel(model_dir)
        self.treeView_dir.setRootIndex(root_dir)
        self.treeView_dir.setSortingEnabled(True)
        self.treeView_dir.sortByColumn(0,0)
        self.treeView_dir.hideColumn(1)
        self.treeView_dir.hideColumn(2)

        self.treeView_dir.resizeColumnToContents(0)
        self.treeView_dir.resizeColumnToContents(1)
        self.treeView_dir.resizeColumnToContents(2)
        self.treeView_dir.resizeColumnToContents(3)

        self.horizontalLayout.addWidget(self.treeView_dir)

        self.treeView_dir.clicked.connect(self.test_dir)


        #
        # File Section
        #
        audio_extensions = tuple(self.audio_mimetype())
        # print (audio_extensions)
        model_files = QFileSystemModel()
        model_files.setRootPath(homedir)
        root_files = model_files.setRootPath(homedir)
        self.filemodel = model_files
        # only files
        model_files.setFilter(QtCore.QDir.Files|QtCore.QDir.NoDotAndDotDot)
        model_files.setNameFilters(audio_extensions)

        self.treeView_files = QtWidgets.QTreeView(self.centralwidget)
        self.treeView_files.setObjectName("treeView_files")
        self.treeView_files.setModel(model_files)
        self.treeView_files.setRootIndex(root_files)
        self.treeView_files.setSortingEnabled(True)
        self.treeView_files.sortByColumn(0, 0)

        self.treeView_files.selectionModel().selectionChanged.connect(self.play_audio)
        self.horizontalLayout.addWidget(self.treeView_files)
        self.verticalLayout.addLayout(self.horizontalLayout)


        self.graphicsView = QtWidgets.QGraphicsView(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.graphicsView.sizePolicy().hasHeightForWidth())
        self.graphicsView.setSizePolicy(sizePolicy)
        self.graphicsView.setBaseSize(QtCore.QSize(0, 0))
        self.graphicsView.setObjectName("graphicsView")

        self.verticalLayout.addWidget(self.graphicsView)
        self.horizontalLayout_2.addLayout(self.verticalLayout)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 25))
        self.menubar.setObjectName("menubar")
        self.menuPreferences = QtWidgets.QMenu(self.menubar)
        self.menuPreferences.setObjectName("menuPreferences")
        MainWindow.setMenuBar(self.menubar)

        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")

        MainWindow.setStatusBar(self.statusbar)
        self.toolBar = QtWidgets.QToolBar(MainWindow)
        self.toolBar.setObjectName("toolBar")

        MainWindow.addToolBar(QtCore.Qt.TopToolBarArea, self.toolBar)

        self.actionPreferences = QtWidgets.QAction(MainWindow)
        self.actionPreferences.setObjectName("actionPreferences")
        self.actionExit = QtWidgets.QAction(MainWindow)
        self.actionExit.setObjectName("actionExit")

        self.menuPreferences.addAction(self.actionPreferences)
        self.menuPreferences.addAction(self.actionExit)
        self.menubar.addAction(self.menuPreferences.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.menuPreferences.setTitle(_translate("MainWindow", "Menu"))
        self.toolBar.setWindowTitle(_translate("MainWindow", "toolBar"))
        self.actionPreferences.setText(_translate("MainWindow", "Preferences"))
        self.actionExit.setText(_translate("MainWindow", "Exit"))

    def test_dir(self, signal):
        # print(self,signal)
        self.treeView_dir.resizeColumnToContents(0)
        self.treeView_files.resizeColumnToContents(0)
        #self.treeView_dir.resizeColumnToContents(1)
        #self.treeView_dir.resizeColumnToContents(2)
        #self.treeView_dir.resizeColumnToContents(3)
        file_path=self.dirmodel.filePath(signal)
        #print(file_path)
        my_root = self.filemodel.setRootPath(file_path)
        self.treeView_files.setRootIndex(my_root)

    def audio_mimetype(self):
        mimetypes.init()
        for ext in mimetypes.types_map:
            if mimetypes.types_map[ext].split('/')[0] == 'audio':
                yield "*"+ext

    def play_audio(self, selected_indexes, deselected_indexes):
        selected_paths = tuple(self.filemodel.filePath(index) for index in self.treeView_files.selectionModel().selectedRows())

        audio_file_path = '\n'.join(selected_paths)
        print(audio_file_path)
        url= QtCore.QUrl.fromLocalFile(audio_file_path)
        print(url)
        content= QtMultimedia.QMediaContent(url)

        self.player = QtMultimedia.QMediaPlayer()
        self.player.setMedia(content)
        self.player.play()

if __name__ == "__main__":
    import sys, mimetypes,os

    homedir=os.path.expanduser('~')
    print(homedir)

    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

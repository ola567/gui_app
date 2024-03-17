from PyQt5 import QtCore, QtGui, QtWidgets

from TaskView import TaskView


class MainView(object):
    def setup_view(self, main_view):
        main_view.setObjectName("main_view")
        main_view.resize(600, 800)
        main_view.setStyleSheet("background-color: rgb(217, 217, 217);\n")
        self.centralwidget = QtWidgets.QWidget(main_view)
        self.centralwidget.setObjectName("centralwidget")

        self.add_task = QtWidgets.QPushButton(self.centralwidget)
        self.add_task.setGeometry(QtCore.QRect(20, 570, 270, 50))
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.add_task.setFont(font)
        self.add_task.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.add_task.setMouseTracking(True)
        self.add_task.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.add_task.setStyleSheet("background-color: rgb(82, 95, 207);\n"
                                    "color: rgb(255, 255, 255);\n"
                                    "border-radius: 10px;")
        self.add_task.setObjectName("add_task")
        # self.add_task.clicked.connect(self.add_task)

        self.edit_task = QtWidgets.QPushButton(self.centralwidget)
        self.edit_task.setGeometry(QtCore.QRect(310, 570, 270, 50))
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.edit_task.setFont(font)
        self.edit_task.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.edit_task.setMouseTracking(True)
        self.edit_task.setStyleSheet("background-color: rgb(82, 95, 207);\n"
                                     "color: rgb(255, 255, 255);\n"
                                     "border-radius: 10px;")
        self.edit_task.setObjectName("edit_task")

        self.delete_task = QtWidgets.QPushButton(self.centralwidget)
        self.delete_task.setGeometry(QtCore.QRect(20, 630, 560, 50))
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.delete_task.setFont(font)
        self.delete_task.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.delete_task.setStyleSheet("background-color: rgb(82, 95, 207);\n"
                                       "color: rgb(255, 255, 255);\n"
                                       "border-radius: 10px;")
        self.delete_task.setObjectName("delete_task")

        self.done = QtWidgets.QPushButton(self.centralwidget)
        self.done.setGeometry(QtCore.QRect(20, 690, 270, 50))
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.done.setFont(font)
        self.done.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.done.setStyleSheet("background-color: rgb(82, 95, 207);\n"
                                "color: rgb(255, 255, 255);\n"
                                "border-radius: 10px;")
        self.done.setObjectName("done")

        self.not_done = QtWidgets.QPushButton(self.centralwidget)
        self.not_done.setGeometry(QtCore.QRect(310, 690, 270, 50))
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.not_done.setFont(font)
        self.not_done.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.not_done.setStyleSheet("background-color: rgb(82, 95, 207);\n"
                                    "color: rgb(255, 255, 255);\n"
                                    "border-radius: 10px;")
        self.not_done.setObjectName("not_done")

        self.to_do_list = QtWidgets.QListWidget(self.centralwidget)
        self.to_do_list.setGeometry(QtCore.QRect(20, 20, 560, 530))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.to_do_list.sizePolicy().hasHeightForWidth())
        self.to_do_list.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.to_do_list.setFont(font)
        self.to_do_list.setStyleSheet("background-color: rgb(255, 255, 255);\n"
                                      "border-radius: 10 px;")
        self.to_do_list.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.to_do_list.setItemAlignment(QtCore.Qt.AlignLeading)
        self.to_do_list.setObjectName("to_do_list")

        main_view.setCentralWidget(self.centralwidget)
        self.menu = QtWidgets.QMenuBar(main_view)
        self.menu.setGeometry(QtCore.QRect(0, 0, 600, 37))
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.menu.setFont(font)
        self.menu.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.menu.setStyleSheet("background-color: rgb(82, 95, 207);\n"
                                "color: rgb(255, 255, 255);\n"
                                "border-radius: 10 px;")
        self.menu.setObjectName("menu")
        self.menu_elements = QtWidgets.QMenu(self.menu)
        self.menu_elements.setGeometry(QtCore.QRect(273, 122, 268, 200))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.menu_elements.sizePolicy().hasHeightForWidth())
        self.menu_elements.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.menu_elements.setFont(font)
        self.menu_elements.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.menu_elements.setContextMenuPolicy(QtCore.Qt.CustomContextMenu)
        self.menu_elements.setWhatsThis("")
        self.menu_elements.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.menu_elements.setStyleSheet("background-color: rgb(82, 95, 207);\n"
                                         "color: rgb(255, 255, 255);")
        self.menu_elements.setObjectName("menu_elements")
        main_view.setMenuBar(self.menu)
        self.save_to_file = QtWidgets.QAction(main_view)
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.save_to_file.setFont(font)
        self.save_to_file.setObjectName("save_to_file")
        self.read_from_file = QtWidgets.QAction(main_view)
        self.read_from_file.setCheckable(True)
        self.read_from_file.setObjectName("read_from_file")
        self.actionO_aplikacji = QtWidgets.QAction(main_view)
        self.actionO_aplikacji.setObjectName("actionO_aplikacji")
        self.save_to_file_2 = QtWidgets.QAction(main_view)
        self.save_to_file_2.setObjectName("save_to_file_2")
        self.actionWczytaj_do_pliku = QtWidgets.QAction(main_view)
        self.actionWczytaj_do_pliku.setObjectName("actionWczytaj_do_pliku")
        self.about_app = QtWidgets.QAction(main_view)
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.about_app.setFont(font)
        self.about_app.setObjectName("about_app")
        self.menu_elements.addAction(self.save_to_file_2)
        self.menu_elements.addAction(self.actionWczytaj_do_pliku)
        self.menu_elements.addAction(self.about_app)
        self.menu.addAction(self.menu_elements.menuAction())

        self.task_view_handler = None

        self.retranslate_view(main_view)
        QtCore.QMetaObject.connectSlotsByName(main_view)

    def retranslate_view(self, main_view):
        _translate = QtCore.QCoreApplication.translate
        main_view.setWindowTitle(_translate("main_view", "Dodaj zadanie"))
        self.add_task.setText(_translate("main_view", "Dodaj"))
        self.edit_task.setText(_translate("main_view", "Edytuj"))
        self.delete_task.setText(_translate("main_view", "Usun"))
        self.done.setText(_translate("main_view", "Zrobione"))
        self.not_done.setText(_translate("main_view", "Nie zrobione"))
        self.menu_elements.setTitle(_translate("main_view", "Menu"))
        self.read_from_file.setText(_translate("main_view", "Wczytaj z pliku"))
        self.actionO_aplikacji.setText(_translate("main_view", "O aplikacji"))
        self.save_to_file_2.setText(_translate("main_view", "Zapisz do pliku"))
        self.actionWczytaj_do_pliku.setText(_translate("main_view", "Wczytaj do pliku"))
        self.about_app.setText(_translate("main_view", "O aplikacji"))

    def add_task(self):
        # if self.task_view_handler is None:
        #     self.task_view_window = QtWidgets.QMainWindow()
        #     self.task_view_handler = TaskView()
        #     self.task_view_handler.setup_view(self.task_view_window)
        #     self.task_view_window.show()
        # else:
        #     self.task_view_window.show()
        print("presed")

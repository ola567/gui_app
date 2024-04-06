import ast

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QColor
from PyQt5.QtWidgets import QFileDialog

from AboutAppView import AboutAppView
from TaskView import TaskView
from ToDoList import ToDoList


class MainView(object):
    def setup_view(self, main_view):
        main_view.setObjectName("main_view")
        main_view.resize(600, 800)
        main_view.setStyleSheet("background-color: rgb(217, 217, 217);\n")
        self.centralwidget = QtWidgets.QWidget(main_view)
        self.centralwidget.setObjectName("centralwidget")

        font = QtGui.QFont()
        font.setPointSize(20)

        button_style_sheet = '''*{background-color: rgb(82, 95, 207);
                                color: rgb(255, 255, 255);
                                border-radius: 10px;}
                                *:hover{background-color: rgb(72, 85, 197);}'''

        self.add_task_button = QtWidgets.QPushButton(self.centralwidget)
        self.add_task_button.setGeometry(QtCore.QRect(20, 570, 270, 50))
        self.add_task_button.setFont(font)
        self.add_task_button.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.add_task_button.setMouseTracking(True)
        self.add_task_button.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.add_task_button.setStyleSheet(button_style_sheet)
        self.add_task_button.setObjectName("add_task")
        self.add_task_button.clicked.connect(self.add_task)

        self.edit_task_button = QtWidgets.QPushButton(self.centralwidget)
        self.edit_task_button.setGeometry(QtCore.QRect(310, 570, 270, 50))
        self.edit_task_button.setFont(font)
        self.edit_task_button.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.edit_task_button.setMouseTracking(True)
        self.edit_task_button.setStyleSheet(button_style_sheet)
        self.edit_task_button.setObjectName("edit_task")
        self.edit_task_button.clicked.connect(self.edit_task)

        self.delete_task_button = QtWidgets.QPushButton(self.centralwidget)
        self.delete_task_button.setGeometry(QtCore.QRect(20, 630, 560, 50))
        self.delete_task_button.setFont(font)
        self.delete_task_button.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.delete_task_button.setStyleSheet(button_style_sheet)
        self.delete_task_button.setObjectName("delete_task")
        self.delete_task_button.clicked.connect(self.delete_task)

        self.done_button = QtWidgets.QPushButton(self.centralwidget)
        self.done_button.setGeometry(QtCore.QRect(20, 690, 270, 50))
        self.done_button.setFont(font)
        self.done_button.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.done_button.setStyleSheet(button_style_sheet)
        self.done_button.setObjectName("done")
        self.done_button.clicked.connect(self.done)

        self.not_done_button = QtWidgets.QPushButton(self.centralwidget)
        self.not_done_button.setGeometry(QtCore.QRect(310, 690, 270, 50))
        self.not_done_button.setFont(font)
        self.not_done_button.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.not_done_button.setStyleSheet(button_style_sheet)
        self.not_done_button.setObjectName("not_done")
        self.not_done_button.clicked.connect(self.not_done)

        self.to_do_list = QtWidgets.QListWidget(self.centralwidget)
        self.to_do_list.setGeometry(QtCore.QRect(20, 20, 560, 530))
        self.to_do_list.setStyleSheet('''*{background-color: rgb(255, 255, 255);
                                        border-radius: 10px;}''')
        self.to_do_list.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.to_do_list.setItemAlignment(QtCore.Qt.AlignLeading)
        self.to_do_list.setObjectName("to_do_list")

        main_view.setCentralWidget(self.centralwidget)
        self.menu = QtWidgets.QMenuBar(main_view)
        self.menu.setGeometry(QtCore.QRect(0, 0, 600, 40))
        self.menu.setFont(font)
        self.menu.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.menu.setStyleSheet('''*{background-color: rgb(82, 95, 207);
                                     color: rgb(255, 255, 255);
                                     border-radius: 10px;}''')
        self.menu.setObjectName("menu")

        self.menu_elements = QtWidgets.QMenu(self.menu)
        self.menu_elements.setGeometry(QtCore.QRect(0, 0, 600, 200))
        self.menu_elements.setFont(font)
        self.menu_elements.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.menu_elements.setContextMenuPolicy(QtCore.Qt.CustomContextMenu)
        self.menu_elements.setStyleSheet('''*{background-color: rgb(82, 95, 207);;
                                             color: rgb(255, 255, 255);
                                             border-radius: 10px;}''')
        self.menu_elements.setObjectName("menu_elements")

        main_view.setMenuBar(self.menu)
        self.save_to_file_action = QtWidgets.QAction(main_view)
        self.save_to_file_action.setObjectName("save_to_file")
        self.save_to_file_action.triggered.connect(self.save_to_file)

        self.read_from_file_action = QtWidgets.QAction(main_view)
        self.read_from_file_action.setObjectName("read_from_file")
        self.read_from_file_action.triggered.connect(self.read_from_file)

        self.about_app_action = QtWidgets.QAction(main_view)
        self.about_app_action.setObjectName("about_app")
        self.about_app_action.triggered.connect(self.about_app)

        self.menu_elements.addAction(self.save_to_file_action)
        self.menu_elements.addAction(self.read_from_file_action)
        self.menu_elements.addAction(self.about_app_action)
        self.menu.addAction(self.menu_elements.menuAction())

        self.task_view_handler = None
        self.task_list = ToDoList()

        self.retranslate_view(main_view)
        QtCore.QMetaObject.connectSlotsByName(main_view)

    def retranslate_view(self, main_view):
        _translate = QtCore.QCoreApplication.translate
        main_view.setWindowTitle(_translate("main_view", "Lista zadań"))
        self.add_task_button.setText(_translate("main_view", "Dodaj"))
        self.edit_task_button.setText(_translate("main_view", "Edytuj"))
        self.delete_task_button.setText(_translate("main_view", "Usuń"))
        self.done_button.setText(_translate("main_view", "Zrobione"))
        self.not_done_button.setText(_translate("main_view", "Nie zrobione"))
        self.menu_elements.setTitle(_translate("main_view", "Menu"))
        self.save_to_file_action.setText(_translate("main_view", "Zapisz do pliku"))
        self.read_from_file_action.setText(_translate("main_view", "Wczytaj z pliku"))
        self.about_app_action.setText(_translate("main_view", "O aplikacji"))

    def add_task(self):
        self.task_view_window = QtWidgets.QMainWindow()
        self.task_view_handler = TaskView()
        self.task_view_handler.setup_view(add_task=self.task_view_window, parent=self, window_title='Dodaj zadanie')
        self.task_view_window.show()

    def delete_task(self):
        selected_tasks = self.to_do_list.selectedItems()
        for task in selected_tasks:
            task_number = self.to_do_list.row(task)
            self.to_do_list.takeItem(self.to_do_list.row(task))
            self.task_list.delete(task_number=task_number)

    def save_to_file(self):
        file_path, _ = QFileDialog.getSaveFileName(None, "Zapisz plik", "", "Pliki tekstowe")
        if file_path:
            with open(file_path, "w") as file:
                file.write(str(self.task_list.list))

    def read_from_file(self):
        file_path, _ = QFileDialog.getOpenFileName(None, "Otwórz plik", "", "Pliki tekstowe")
        if file_path:
            try:
                with open(file_path, "r") as file:
                    self.task_list.list = ast.literal_eval(file.read())
                    self.to_do_list.clear()
                    for task in self.task_list.list:
                        self.to_do_list.addItem(
                            f'Tytuł: {task["task_title"]}\nData ukończenia: {task["task_finish_date"]}:\nOpis: {task["task_description"]}\n')
                        if task["task_done"] == 1:
                            last_task = self.to_do_list.item(self.to_do_list.count() - 1)
                            last_task.setForeground(QColor("green"))
                            font = last_task.font()
                            font.setStrikeOut(True)
                            last_task.setFont(font)
            except Exception as e:
                print("Error reading file:", str(e))

    def done(self):
        selected_item = self.to_do_list.currentItem()
        if selected_item:
            selected_item.setForeground(QColor("green"))
            font = selected_item.font()
            font.setStrikeOut(True)
            selected_item.setFont(font)
            self.task_list.list[self.to_do_list.row(selected_item)]['task_done'] = 1

    def not_done(self):
        selected_item = self.to_do_list.currentItem()
        if selected_item:
            selected_item.setForeground(QColor("black"))
            font = selected_item.font()
            font.setStrikeOut(False)
            selected_item.setFont(font)
            self.task_list.list[self.to_do_list.row(selected_item)]['task_done'] = 0

    def about_app(self):
        self.about_app_window = QtWidgets.QMainWindow()
        self.about_app_handler = AboutAppView()
        self.about_app_handler.setup_view(self.about_app_window)
        self.about_app_window.show()

    def edit_task(self):
        task_index = self.to_do_list.currentRow()
        if task_index != -1:
            self.task_view_window = QtWidgets.QMainWindow()
            self.task_view_handler = TaskView()
            self.task_view_handler.setup_view(add_task=self.task_view_window, parent=self, window_title='Edytuj zadanie', task_index=task_index)
            self.task_view_window.show()

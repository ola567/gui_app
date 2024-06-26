from PyQt5 import QtCore, QtGui, QtWidgets


class TaskView(object):
    def setup_view(self, add_task, window_title, parent=None, task_index=None):
        # variables
        self.parent = parent
        self.task_index = task_index
        self.window_title = window_title

        self.add_task = add_task
        self.add_task.setObjectName("add_task")
        self.add_task.resize(600, 800)
        self.add_task.setStyleSheet("background-color: rgb(217, 217, 217);\n")

        font = QtGui.QFont()
        font.setPointSize(20)

        self.ok_button = QtWidgets.QPushButton(self.add_task)
        self.ok_button.setGeometry(QtCore.QRect(20, 730, 270, 50))
        self.ok_button.setStyleSheet('''*{background-color: rgb(86, 205, 14);
                                        color: rgb(255, 255, 255);
                                        border-radius: 10px;}
                                        *:hover{background-color: rgb(66, 185, 0);}''')
        self.ok_button.setObjectName("ok_button")
        self.ok_button.setFont(font)
        self.ok_button.clicked.connect(self.ok)

        self.finish_date_label = QtWidgets.QLabel(self.add_task)
        self.finish_date_label.setGeometry(QtCore.QRect(20, 370, 560, 70))
        self.finish_date_label.setFont(font)
        self.finish_date_label.setStyleSheet("background-color: rgb(82, 95, 207);\n"
                                             "color: rgb(255, 255, 255);\n"
                                             "text-align: center;\n"
                                             "border-radius: 10px;")
        self.finish_date_label.setAlignment(QtCore.Qt.AlignCenter)
        self.finish_date_label.setObjectName("finish_date_label")

        self.content_input = QtWidgets.QPlainTextEdit(self.add_task)
        self.content_input.setGeometry(QtCore.QRect(20, 270, 560, 70))
        self.content_input.setStyleSheet("background-color: rgb(255, 255, 255);\n"
                                         "border-radius: 10px;")
        self.content_input.setObjectName("content_input")

        self.cancel_button = QtWidgets.QPushButton(self.add_task)
        self.cancel_button.setGeometry(QtCore.QRect(310, 730, 270, 50))
        self.cancel_button.setStyleSheet('''*{background-color: rgb(192, 28, 40);
                                        color: rgb(255, 255, 255);
                                        border-radius: 10px;}
                                        *:hover{background-color: rgb(172, 8, 20);}''')
        self.cancel_button.setObjectName("cancel_button")
        self.cancel_button.setFont(font)
        self.cancel_button.clicked.connect(self.cancel)

        self.title_label = QtWidgets.QLabel(self.add_task)
        self.title_label.setGeometry(QtCore.QRect(20, 20, 560, 70))
        self.title_label.setFont(font)
        self.title_label.setStyleSheet("background-color: rgb(82, 95, 207);\n"
                                       "color: rgb(255, 255, 255);\n"
                                       "text-align: center;\n"
                                       "border-radius: 10px;")
        self.title_label.setAlignment(QtCore.Qt.AlignCenter)
        self.title_label.setObjectName("title_label")

        self.content_label = QtWidgets.QLabel(self.add_task)
        self.content_label.setGeometry(QtCore.QRect(20, 190, 560, 70))
        self.content_label.setFont(font)
        self.content_label.setStyleSheet("background-color: rgb(82, 95, 207);\n"
                                         "color: rgb(255, 255, 255);\n"
                                         "text-align: center;\n"
                                         "border-radius: 10px;")
        self.content_label.setAlignment(QtCore.Qt.AlignCenter)
        self.content_label.setObjectName("content_label")

        self.title_input = QtWidgets.QPlainTextEdit(self.add_task)
        self.title_input.setGeometry(QtCore.QRect(20, 100, 560, 70))
        self.title_input.setStyleSheet("background-color: rgb(255, 255, 255);\n"
                                       "border-radius: 10px;")
        self.title_input.setObjectName("title_input")

        self.finish_date_input = QtWidgets.QPlainTextEdit(self.add_task)
        self.finish_date_input.setGeometry(QtCore.QRect(20, 450, 560, 70))
        self.finish_date_input.setStyleSheet("background-color: rgb(255, 255, 255);\n"
                                             "border-radius: 10px;")
        self.finish_date_input.setObjectName("finish_date_input")

        if self.task_index is not None:
            self.title_input.insertPlainText(self.parent.task_list.list[self.task_index]['task_title'])
            self.content_input.insertPlainText(self.parent.task_list.list[self.task_index]['task_description'])
            self.finish_date_input.insertPlainText(self.parent.task_list.list[self.task_index]['task_finish_date'])

        self.retranslate_view(self.add_task)
        QtCore.QMetaObject.connectSlotsByName(self.add_task)

    def retranslate_view(self, add_task):
        _translate = QtCore.QCoreApplication.translate
        add_task.setWindowTitle(_translate("add_task", self.window_title))
        self.ok_button.setText(_translate("add_task", "Akceptuj"))
        self.finish_date_label.setText(_translate("add_task", "Data ukończenia"))
        self.cancel_button.setText(_translate("add_task", "Anuluj"))
        self.title_label.setText(_translate("add_task", "Tytuł"))
        self.content_label.setText(_translate("add_task", "Treść"))

    def ok(self):
        task_title = self.title_input.toPlainText()
        task_description = self.content_input.toPlainText()
        task_finish_date = self.finish_date_input.toPlainText()
        if self.task_index is not None:
            self.parent.to_do_list.item(self.task_index).setText(f'Tytuł: {task_title}\nData ukończenia: {task_finish_date}\nOpis: {task_description}\n')
            self.parent.task_list.edit(task_index=self.task_index, new_task=(task_title, task_description, task_finish_date))
        else:
            self.parent.task_list.add((task_title, task_description, task_finish_date, 0))
            self.parent.to_do_list.addItem(f'Tytuł: {task_title}\nData ukończenia: {task_finish_date}\nOpis: {task_description}\n')
        self.add_task.close()

    def cancel(self):
        self.add_task.close()

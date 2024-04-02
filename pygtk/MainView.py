import gi

from pygtk.TaskView import TaskView
from pygtk.ToDoList import ToDoList

gi.require_version("Gtk", "3.0")
from gi.repository import Gtk, Gdk


class MainView(Gtk.Window):
    def __init__(self):
        super().__init__(title="Lista zadań")
        self.set_default_size(600, 800)

        # variables
        self.task_list = ToDoList()

        # elements
        self.grid = Gtk.Grid()
        box = Gtk.Box(orientation=Gtk.Orientation.VERTICAL)

        self.menu_bar = Gtk.MenuBar()
        menu = Gtk.Menu()
        menu_item = Gtk.MenuItem(label="Menu")
        menu_item.set_submenu(menu)

        save_to_file_item = Gtk.MenuItem(label="Zapisz do pliku")
        save_to_file_item.connect("activate", self.save_to_file)
        menu.append(save_to_file_item)

        read_from_file_item = Gtk.MenuItem(label="Wczytaj z pliku")
        read_from_file_item.connect("activate", self.read_from_file)
        menu.append(read_from_file_item)

        about_app_item = Gtk.MenuItem(label="O aplikacji")
        about_app_item.connect("activate", self.about_app)
        menu.append(about_app_item)

        self.menu_bar.append(menu_item)

        self.to_do_list = Gtk.ListBox()
        self.add_task_button = Gtk.Button(label="Dodaj")
        self.add_task_button.connect("clicked", self.add_task)
        self.edit_task_button = Gtk.Button(label="Edytuj")
        self.edit_task_button.connect("clicked", self.edit_task)
        self.delete_task_button = Gtk.Button(label="Usuń")
        self.edit_task_button.connect("clicked", self.edit_task)
        self.done_task_button = Gtk.Button(label="Zrobione")
        self.done_task_button.connect("clicked", self.done)
        self.not_done_task_button = Gtk.Button(label="Nie zrobione")
        self.not_done_task_button.connect("clicked", self.not_done)

        self.grid.attach(self.to_do_list, 0, 0, 2, 1)
        self.grid.attach(self.add_task_button, 0, 1, 1, 1)
        self.grid.attach(self.edit_task_button, 1, 1, 1, 1)
        self.grid.attach(self.delete_task_button, 0, 2, 2, 1)
        self.grid.attach(self.done_task_button, 0, 3, 1, 1)
        self.grid.attach(self.not_done_task_button, 1, 3, 1, 1)

        self.grid.set_halign(Gtk.Align.CENTER)
        self.grid.set_valign(Gtk.Align.CENTER)

        box.pack_start(self.menu_bar, False, False, 0)
        box.pack_start(self.grid, True, True, 0)

        self.add(box)

    def add_task(self, widget):
        task_window = TaskView(parent=self)
        task_window.connect('destroy', task_window.destroy())
        task_window.show_all()

    def edit_task(self, widget):
        selected_row = self.to_do_list.get_selected_row()
        task_index = selected_row.get_index()
        if selected_row and task_index != -1:
            task_view_window = TaskView(parent=self, task_index=task_index)
            task_view_window.connect('destroy', task_view_window.destroy)
            task_view_window.show_all()

    def delete_task(self, widget):
        selected_row = self.to_do_list.get_selected_row()
        if selected_row:
            task_number = selected_row.get_index()
            self.to_do_list.remove(selected_row)
            self.task_list.delete(task_number=task_number)

    def done(self, widget):
        # selected_item = self.to_do_list.currentItem()
        # if selected_item:
        #     selected_item.setForeground(QColor("green"))
        #     font = selected_item.font()
        #     font.setStrikeOut(True)
        #     selected_item.setFont(font)
        #     self.task_list.list[self.to_do_list.row(selected_item)]['task_done'] = 1
        pass

    def not_done(self, widget):
        # selected_item = self.to_do_list.currentItem()
        # if selected_item:
        #     selected_item.setForeground(QColor("black"))
        #     font = selected_item.font()
        #     font.setStrikeOut(False)
        #     selected_item.setFont(font)
        #     self.task_list.list[self.to_do_list.row(selected_item)]['task_done'] = 0
        pass

    def save_to_file(self, widget):
        # file_path, _ = QFileDialog.getSaveFileName(None, "Save File", "", "Text Files")
        # if file_path:
        #     with open(file_path, "w") as file:
        #         file.write(str(self.task_list.list))
        pass

    def read_from_file(self, widget):
        # file_path, _ = QFileDialog.getOpenFileName(None, "Open File", "", "Text Files")
        # if file_path:
        #     try:
        #         with open(file_path, "r") as file:
        #             self.task_list.list = ast.literal_eval(file.read())
        #             self.to_do_list.clear()
        #             for task in self.task_list.list:
        #                 self.to_do_list.addItem(
        #                     f'{task["task_title"]} {task["task_finish_date"]}: \n    {task["task_description"]}')
        #                 if task["task_done"] == 1:
        #                     last_task = self.to_do_list.item(self.to_do_list.count() - 1)
        #                     last_task.setForeground(QColor("green"))
        #                     font = last_task.font()
        #                     font.setStrikeOut(True)
        #                     last_task.setFont(font)
        #     except Exception as e:
        #         print("Error reading file:", str(e))
        pass

    def about_app(self, widget):
        # self.about_app_window = QtWidgets.QMainWindow()
        # self.about_app_handler = AboutAppView()
        # self.about_app_handler.setup_view(self.about_app_window)
        # self.about_app_window.show()
        pass

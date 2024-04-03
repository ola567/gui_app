import ast

import gi

from pygtk.AboutAppView import AboutAppView
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
        task_window.connect('destroy', task_window.destroy)
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
        selected_item = self.to_do_list.get_selected_row()
        if selected_item:
            selected_item_index = selected_item.get_index()
            selected_item_label = selected_item.get_child()
            selected_item_label.set_property("use_markup", True)
            selected_item_label.set_markup('<span strikethrough="true" foreground="green">{}</span>'.format(selected_item_label.get_text()))
            self.task_list.list[selected_item_index]['task_done'] = 1

    def not_done(self, widget):
        selected_item = self.to_do_list.get_selected_row()
        if selected_item:
            selected_item_index = selected_item.get_index()
            selected_item_label = selected_item.get_child()
            selected_item_label.set_property("use_markup", True)
            selected_item_label.set_markup('<span strikethrough="false" foreground="black">{}</span>'.format(selected_item_label.get_text()))
            self.task_list.list[selected_item_index]['task_done'] = 0

    def save_to_file(self, widget):
        dialog = Gtk.FileChooserDialog(title="Save File", parent=self, action=Gtk.FileChooserAction.SAVE)
        dialog.add_buttons(Gtk.STOCK_CANCEL, Gtk.ResponseType.CANCEL, Gtk.STOCK_SAVE, Gtk.ResponseType.OK)

        response = dialog.run()
        if response == Gtk.ResponseType.OK:
            file_path = dialog.get_filename()
            if file_path:
                with open(file_path, "w") as file:
                    file.write(str(self.task_list.list))
        dialog.destroy()

    def read_from_file(self, widget):
        dialog = Gtk.FileChooserDialog(title="Open File", parent=self, action=Gtk.FileChooserAction.OPEN)
        dialog.add_buttons(Gtk.STOCK_CANCEL, Gtk.ResponseType.CANCEL, Gtk.STOCK_OPEN, Gtk.ResponseType.OK)
        filter_text = Gtk.FileFilter()
        filter_text.set_name("Text files")
        filter_text.add_mime_type("text/plain")
        dialog.add_filter(filter_text)
        response = dialog.run()
        if response == Gtk.ResponseType.OK:
            file_path = dialog.get_filename()
            if file_path:
                try:
                    with open(file_path, "r") as file:
                        self.task_list.list = ast.literal_eval(file.read())
                        # clear list
                        for row in self.listbox.get_children():
                            self.listbox.remove(row)
                        for task in self.task_list.list:
                            new_task = Gtk.ListBoxRow()
                            label = Gtk.Label(label=f'{task["task_title"]} {task["task_finish_date"]}: \n    {task["task_description"]}')
                            new_task.add(label)
                            self.to_do_list.add(new_task)
                            if task["task_done"] == 1:
                                # get last element
                                children = self.to_do_list.get_children()
                                last_item = children[-1]
                                last_item_label = last_item.get_children()[0]
                                last_item_label.set_property("use_markup", True)
                                last_item_label.set_markup('<span strikethrough="true" foreground="green">{}</span>'.format(last_item_label.get_text()))
                            new_task.show_all()
                except Exception as e:
                    print("Error reading file:", str(e))
        dialog.destroy()

    def about_app(self, widget):
        about_app_window = AboutAppView()
        about_app_window.connect('destroy', about_app_window.destroy)
        about_app_window.show_all()

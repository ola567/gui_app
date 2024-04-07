import ast

import gi

from pygtk.AboutAppView import AboutAppView
from pygtk.CssProvider import CssProvider
from pygtk.TaskView import TaskView
from pygtk.ToDoList import ToDoList

gi.require_version("Gtk", "3.0")
from gi.repository import Gtk, Gdk


class MainView(Gtk.Window):
    def __init__(self):
        super().__init__(title="Lista zadań")
        self.set_default_size(600, 800)
        self.set_name('background')

        # variables
        self.task_list = ToDoList()

        # elements
        window_box = Gtk.Box(orientation=Gtk.Orientation.VERTICAL)
        self.add(window_box)

        # create menu
        self.menu_bar = Gtk.MenuBar()
        self.menu_bar.set_name('menu')
        window_box.pack_start(self.menu_bar, False, False, 0)

        menu = Gtk.Menu()
        menu.set_name('menu')
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

        # create scrolled listbox
        scrolled_window = Gtk.ScrolledWindow()
        scrolled_window.set_hexpand(True)
        scrolled_window.set_vexpand(True)
        window_box.pack_start(scrolled_window, True, True, 0)
        self.to_do_list = Gtk.ListBox()
        self.to_do_list.set_name("to_do_list")
        scrolled_window.add(self.to_do_list)

        # buttons
        button_box = Gtk.Box(orientation=Gtk.Orientation.VERTICAL)
        window_box.pack_start(button_box, False, False, 0)

        box_one = Gtk.Box()
        button_box.pack_start(box_one, True, True, 0)
        self.add_task_button = Gtk.Button(label="Dodaj")
        self.add_task_button.set_name('buttons')
        self.add_task_button.connect("clicked", self.add_task)
        box_one.pack_start(self.add_task_button, True, True, 0)
        self.edit_task_button = Gtk.Button(label="Edytuj")
        self.edit_task_button.set_name('buttons')
        self.edit_task_button.connect("clicked", self.edit_task)
        box_one.pack_start(self.edit_task_button, True, True, 0)

        box_two = Gtk.Box()
        button_box.pack_start(box_two, True, True, 0)
        self.delete_task_button = Gtk.Button(label="Usuń")
        self.delete_task_button.set_name('buttons')
        self.delete_task_button.connect("clicked", self.delete_task)
        box_two.pack_start(self.delete_task_button, True, True, 0)

        box_three = Gtk.Box()
        button_box.pack_start(box_three, True, True, 0)
        self.done_task_button = Gtk.Button(label="Zrobione")
        self.done_task_button.set_name('buttons')
        self.done_task_button.connect("clicked", self.done)
        box_three.pack_start(self.done_task_button, True, True, 0)
        self.not_done_task_button = Gtk.Button(label="Nie zrobione")
        self.not_done_task_button.set_name('buttons')
        self.not_done_task_button.connect("clicked", self.not_done)
        box_three.pack_start(self.not_done_task_button, True, True, 0)


    def add_task(self, widget):
        task_window = TaskView(parent=self, window_title='Dodaj zadanie')
        task_window.show_all()

    def edit_task(self, widget):
        selected_row = self.to_do_list.get_selected_row()
        if selected_row:
            task_index = selected_row.get_index()
            if selected_row and task_index != -1:
                task_view_window = TaskView(parent=self, task_index=task_index, window_title='Edytuj zadanie')
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
        dialog = Gtk.FileChooserDialog(title="Zapisz plik", parent=self, action=Gtk.FileChooserAction.SAVE)
        dialog.add_buttons(Gtk.STOCK_CANCEL, Gtk.ResponseType.CANCEL, Gtk.STOCK_SAVE, Gtk.ResponseType.OK)

        response = dialog.run()
        if response == Gtk.ResponseType.OK:
            file_path = dialog.get_filename()
            if file_path:
                with open(file_path, "w") as file:
                    file.write(str(self.task_list.list))
        dialog.destroy()

    def read_from_file(self, widget):
        dialog = Gtk.FileChooserDialog(title="Otwórz plik", parent=self, action=Gtk.FileChooserAction.OPEN)
        dialog.add_buttons(Gtk.STOCK_CANCEL, Gtk.ResponseType.CANCEL, Gtk.STOCK_OPEN, Gtk.ResponseType.OK)
        filter_text = Gtk.FileFilter()
        filter_text.set_name("Pliki tekstowe")
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
                        for row in self.to_do_list.get_children():
                            self.to_do_list.remove(row)
                        for task in self.task_list.list:
                            new_task = Gtk.ListBoxRow()
                            label = Gtk.Label(label=f'Tytuł: {task["task_title"]}\nData ukończenia: {task["task_finish_date"]}\nOpis:{task["task_description"]}\n')
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
        about_app_window.show_all()

import gi

gi.require_version("Gtk", "3.0")
from gi.repository import Gtk, Gdk


class TaskView(Gtk.Window):
    def __init__(self, parent, task_index=None):
        super().__init__(title="Lista zadań")
        self.set_default_size(600, 800)

        # variables
        self.parent = parent
        self.task_index = task_index

        # elements
        box = Gtk.Box(orientation=Gtk.Orientation.VERTICAL)
        box_window = Gtk.Box(orientation=Gtk.Orientation.VERTICAL)
        box_title = Gtk.Box(orientation=Gtk.Orientation.VERTICAL)
        box_content = Gtk.Box(orientation=Gtk.Orientation.VERTICAL)
        box_date = Gtk.Box(orientation=Gtk.Orientation.VERTICAL)
        box_buttons = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL)

        self.window_label = Gtk.Label(label='Dodaj zadanie')
        self.title_label = Gtk.Label(label='Tytuł')
        self.title_input = Gtk.Entry()
        self.content_label = Gtk.Label(label='Treść')
        self.content_input = Gtk.Entry()
        self.date_label = Gtk.Label(label='Data ukończenia')
        self.date_input = Gtk.Entry()
        self.ok_button = Gtk.Button(label='Ok')
        self.ok_button.connect("clicked", self.ok)
        self.cancel_button = Gtk.Button(label='Anuluj')
        self.cancel_button.connect("clicked", self.cancel)


        box_window.pack_start(self.window_label, True, True, 0)
        box_title.pack_start(self.title_label, True, True, 0)
        box_title.pack_start(self.title_input, True, True, 0)
        box_content.pack_start(self.content_label, True, True, 0)
        box_content.pack_start(self.content_input, True, True, 0)
        box_date.pack_start(self.date_label, True, True, 0)
        box_date.pack_start(self.date_input, True, True, 0)
        box_buttons.pack_start(self.ok_button, True, True, 0)
        box_buttons.pack_start(self.cancel_button, True, True, 0)

        box.pack_start(box_window, False, False, 0)
        box.pack_start(box_title, True, True, 0)
        box.pack_start(box_content, True, True, 0)
        box.pack_start(box_date, True, True, 0)
        box.pack_start(box_buttons, True, True, 0)

        if self.task_index is not None:
            self.title_input.set_text(self.parent.task_list.list[self.task_index]['task_title'])
            self.content_input.set_text(self.parent.task_list.list[self.task_index]['task_description'])
            self.date_input.set_text(self.parent.task_list.list[self.task_index]['task_finish_date'])

        self.add(box)

    def ok(self):
        task_title = self.title_input.get_text()
        task_description = self.content_input.get_text()
        task_finish_date = self.date_input.get_text()
        if self.task_index is not None:
            self.parent.to_do_list.item(self.task_index).setText(f'{task_title} {task_finish_date}: \n    {task_description}')
            self.parent.task_list.edit(task_index=self.task_index, new_task=(task_title, task_description, task_finish_date))
        else:
            self.parent.task_list.add((task_title, task_description, task_finish_date, 0))
            self.parent.to_do_list.addItem(f'{task_title} {task_finish_date}: \n    {task_description}')
        self.destroy()

    def cancel(self):
        self.close()

import gi

gi.require_version("Gtk", "3.0")
from gi.repository import Gtk, Gdk


class TaskView(Gtk.Window):
    def __init__(self, parent, window_title, task_index=None):
        super().__init__(title=window_title)
        self.set_default_size(600, 800)
        self.set_name('background')

        # variables
        self.parent = parent
        self.task_index = task_index
        self.window_title = window_title

        # elements
        box = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=20)
        box_title = Gtk.Box(orientation=Gtk.Orientation.VERTICAL)
        box_content = Gtk.Box(orientation=Gtk.Orientation.VERTICAL)
        box_date = Gtk.Box(orientation=Gtk.Orientation.VERTICAL)
        box_buttons = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=20)

        self.title_label = Gtk.Label(label='Tytuł')
        self.title_label.set_name('task_field_label')
        self.title_input = Gtk.Entry()
        self.title_input.set_name('task_field_input')
        self.content_label = Gtk.Label(label='Treść')
        self.content_label.set_name('task_field_label')
        self.content_input = Gtk.Entry()
        self.content_input.set_name('task_field_input')

        self.date_label = Gtk.Label(label='Data ukończenia')
        self.date_label.set_name('task_field_label')
        self.date_input = Gtk.Entry()
        self.date_input.set_name('task_field_input')

        self.ok_button = Gtk.Button(label='Akceptuj')
        self.ok_button.set_name('ok_button')
        self.ok_button.connect("clicked", self.ok)
        self.cancel_button = Gtk.Button(label='Anuluj')
        self.cancel_button.set_name('cancel_button')
        self.cancel_button.connect("clicked", self.cancel)

        box_title.pack_start(self.title_label, True, True, 0)
        box_title.pack_start(self.title_input, True, True, 0)
        box_content.pack_start(self.content_label, True, True, 0)
        box_content.pack_start(self.content_input, True, True, 0)
        box_date.pack_start(self.date_label, True, True, 0)
        box_date.pack_start(self.date_input, True, True, 0)
        box_buttons.pack_start(self.ok_button, True, True, 0)
        box_buttons.pack_start(self.cancel_button, True, True, 0)

        box.pack_start(box_title, True, True, 0)
        box.pack_start(box_content, True, True, 0)
        box.pack_start(box_date, True, True, 0)
        box.pack_start(box_buttons, False, False, 0)

        if self.task_index is not None:
            self.title_input.set_text(self.parent.task_list.list[self.task_index]['task_title'])
            self.content_input.set_text(self.parent.task_list.list[self.task_index]['task_description'])
            self.date_input.set_text(self.parent.task_list.list[self.task_index]['task_finish_date'])

        self.add(box)

    def ok(self, widget):
        task_title = self.title_input.get_text()
        task_description = self.content_input.get_text()
        task_finish_date = self.date_input.get_text()
        if self.task_index is not None:
            self.parent.task_list.edit(task_index=self.task_index, new_task=(task_title, task_description, task_finish_date))
            # edit in ListBox
            if 0 <= self.task_index < len(self.parent.to_do_list.get_children()):
                row = self.parent.to_do_list.get_children()[self.task_index]
                label = row.get_child().get_children()[0]
                if isinstance(label, Gtk.Label):
                    label.set_text(f'Tytuł: {task_title}\nData ukończenia: {task_finish_date}\nOpis: {task_description}\n')
        else:
            self.parent.task_list.add((task_title, task_description, task_finish_date, 0))
            # add to ListBox
            new_task = Gtk.ListBoxRow()
            grid = Gtk.Grid()
            new_task.add(grid)
            label = Gtk.Label(label=f'Tytuł: {task_title}\nData ukończenia: {task_finish_date}\nOpis: {task_description}\n')
            grid.attach(label, 0, 0, 1, 1)
            self.parent.to_do_list.add(new_task)
            new_task.show_all()
        self.destroy()

    def cancel(self, widget):
        self.destroy()

import gi

from pygtk.CssProvider import CssProvider
from pygtk.MainView import MainView

gi.require_version("Gtk", "3.0")
from gi.repository import Gtk, Gdk


class ToDoListAppView(Gtk.Window):
    def __init__(self):
        super().__init__(title="Lista zadań")
        self.set_default_size(600, 800)
        self.set_name('start_view')

        # load styles
        css_provider = CssProvider()
        css_provider.load_styles()

        # elements
        self.app_name_label = Gtk.Label(label='Lista zadań')
        self.app_name_label.set_name('app_name_label')
        self.app_icon = Gtk.Image.new_from_file("img/app_icon.png")
        self.start_app_button = Gtk.Button(label='Start')
        self.start_app_button.set_name('start_app_button')
        self.start_app_button.connect("clicked", self.on_button_clicked)

        self.grid = Gtk.Grid(row_spacing=30)
        self.grid.attach(self.app_name_label, 1, 0, 1, 1)
        self.grid.attach(self.app_icon, 0, 0, 1, 1)
        self.grid.attach(self.start_app_button, 0, 1, 2, 1)

        self.grid.set_halign(Gtk.Align.CENTER)
        self.grid.set_valign(Gtk.Align.CENTER)

        self.add(self.grid)

    def on_button_clicked(self, widget):
        win = MainView()
        win.connect("destroy", Gtk.main_quit)
        win.show_all()
        self.destroy()

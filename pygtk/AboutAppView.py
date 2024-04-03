import gi

gi.require_version("Gtk", "3.0")
from gi.repository import Gtk, Gdk


class AboutAppView:
    def __init__(self):
        super().__init__(title="O aplikacji")
        self.set_default_size(600, 800)

        box = Gtk.Box()

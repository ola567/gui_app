import gi

from pygtk.ToDoListApp import ToDoListAppView

gi.require_version("Gtk", "3.0")
from gi.repository import Gtk


if __name__ == "__main__":
    win = ToDoListAppView()
    win.show_all()
    Gtk.main()

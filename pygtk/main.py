import gi

from pygtk.ToDoListApp import MyWindow

gi.require_version("Gtk", "3.0")
from gi.repository import Gtk


if __name__ == "__main__":
    win = MyWindow()
    win.connect("destroy", Gtk.main_quit)
    win.show_all()
    Gtk.main()

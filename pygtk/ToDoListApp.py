import gi

gi.require_version("Gtk", "3.0")
from gi.repository import Gtk


class ToDoListAppView(Gtk.Window):
    def __init__(self):
        super().__init__(title="Hello World")
        self.button = Gtk.Button(label="Click Here")
        self.button.connect("clicked", self.on_button_clicked)
        self.add(self.button)

    def on_button_clicked(self, widget):
        print('cliclked')

    # def start_app(self):
    #     if self.main_view_handler is None:
    #         self.main_view_window = QtWidgets.QMainWindow()
    #         self.main_view_handler = MainView()
    #         self.main_view_handler.setup_view(self.main_view_window)
    #         self.main_view_window.show()
    #         self.ToDoListApp.close()
    #     else:
    #         self.main_view_window.show()
    #         self.ToDoListApp.close()

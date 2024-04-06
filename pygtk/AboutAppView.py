import gi

gi.require_version("Gtk", "3.0")
from gi.repository import Gtk, Gdk


class AboutAppView(Gtk.Window):
    def __init__(self):
        super().__init__(title="O aplikacji")
        self.set_default_size(600, 230)

        box = Gtk.Box(orientation=Gtk.Orientation.VERTICAL)
        about_app_content = Gtk.Label(label="Aplikacja umożliwia stworzenie listy zadań do zrobienia. Zadania można \n"
                                            "dodawać, edytować, usuwać, oznaczać jako zrobione i nie zrobione. Oprócz \n"
                                            "tego listę można zapisać w pliku tekstowym, jak również wczytać z pliku.")

        box.pack_start(about_app_content, True, True, 0)

        self.add(box)

import gi

gi.require_version("Gtk", "3.0")
from gi.repository import Gtk, Gdk


class CssProvider:
    def __init__(self):
        screen = Gdk.Screen.get_default()
        self.provider = Gtk.CssProvider()
        style_context = Gtk.StyleContext()
        style_context.add_provider_for_screen(
            screen, self.provider, Gtk.STYLE_PROVIDER_PRIORITY_APPLICATION
        )

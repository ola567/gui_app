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

        self.styles_css = b"""
                #buttons {
                    background: rgb(82, 95, 207);
                    color: rgb(255, 255, 255);
                    border-radius: 10px;
                    font-size: 20px;
                }
                #buttons:hover {
                    background: rgb(72, 85, 197);
                }
                #ok_button {
                    background: rgb(86, 205, 14);
                    color: rgb(255, 255, 255);
                    border-radius: 10px;
                    font-size: 20px;
                }
                #ok_button:hover {
                    background: rgb(66, 185, 0);
                }
                #cancel_button {
                    background: rgb(192, 28, 40);
                    color: rgb(255, 255, 255);
                    border-radius: 10px;
                    font-size: 20px;
                }
                #cancel_button:hover {
                    background: rgb(172, 8, 20);
                }
                #task_field_label {
                    background: rgb(82, 95, 207);
                    color: rgb(255, 255, 255);
                    border-radius: 10px;
                    font-size: 20px;
                }
                #task_field_input{
                }
                #app_name_label {
                    font-size: 40px;
                    color: rgb(255, 255, 255);
                }
                #start_app_button {
                    background: rgb(239, 139, 235);
                    color: rgb(255, 255, 255);
                    border-radius: 10px;
                    font-size: 20px;
                }
                #start_app_button:hover {
                    background: rgb(229, 129, 225);
                }
                #start_view {
                    background: rgb(82, 95, 207);
                }
                #background {
                    background-color: rgb(217, 217, 217);
                }
                """

    def load_styles(self):
        self.provider.load_from_data(self.styles_css)

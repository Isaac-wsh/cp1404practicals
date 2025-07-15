from kivy.app import App
from kivy.lang import Builder
from kivy.core.window import Window

class MilesConverterApp(App):
    def build(self):
        """Set window size and title, then load and return the root widget from the KV file."""
        Window.size = (400, 200)
        self.title = "Convert Miles to Kilometres"
        self.root = Builder.load_file('convert_miles_km.kv')
        return self.root
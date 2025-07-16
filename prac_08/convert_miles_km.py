from kivy.app import App
from kivy.lang import Builder
from kivy.core.window import Window

CONVERSION_FACTOR = 1.60934

class MilesConverterApp(App):
    def build(self):
        """Set window size and title, then load and return the root widget from the KV file."""
        Window.size = (400, 200)
        self.title = "Convert Miles to Kilometres"
        self.root = Builder.load_file('convert_miles_km.kv')
        return self.root

    def handle_convert(self):
        """Convert miles to kilometres and display result."""
        try:
            miles = float(self.root.ids.input_miles.text)
            km = miles * CONVERSION_FACTOR
            self.root.ids.output_label.text = str(round(km, 5))
        except ValueError:
            self.root.ids.output_label.text = "0.0"

    def handle_up(self):
        """Increase miles input by 1."""
        try:
            miles = float(self.root.ids.input_miles.text)
        except ValueError:
            miles = 0
        miles += 1
        self.root.ids.input_miles.text = str(miles)

    def handle_down(self):
        """Decrease miles input by 1."""
        try:
            miles = float(self.root.ids.input_miles.text)
        except ValueError:
            miles = 0
        miles -= 1
        self.root.ids.input_miles.text = str(miles)

MilesConverterApp().run()

from kivy.app import App
from kivy.lang import Builder
from kivy.core.window import Window
from kivy.app import StringProperty

MILES_TO_KM = 1.60934


class DistanceConverter(App):
    message = StringProperty()

    def build(self):
        Window.size = 500, 250
        self.title = "Convert Miles to Kilometres"
        self.root = Builder.load_file("miles_to_km.kv")
        return self.root

    # def handle_convert(self, value):
    #     value = self.convert_to_number(value)
    #     kilometres = value * MILES_TO_KM
    #     self.root.ids.output_label.text = str(kilometres)

    def handle_calculate(self, value):
        value = self.convert_to_number(value)
        self.update_message(value)

    def handle_increment(self, text, change):
        miles = self.convert_to_number(text) + change
        self.root.ids.input_number.text = str(miles)

    def update_message(self, miles):
        self.message = str(miles * MILES_TO_KM)

    @staticmethod
    def convert_to_number(value):
        try:
            value = float(value)
            print("Converted")  # This runs twice if incrementing an existing number
            return value
        except ValueError:
            return 0.0


DistanceConverter().run()

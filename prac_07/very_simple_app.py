from kivy.app import App
from kivy.lang import Builder
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.properties import StringProperty


class DynamicWidget(App):
    # def __init__(self, **kwargs):
    #     """Construct main app."""
    #     super().__init__(**kwargs)
    #     # basic data example - dictionary of names: phone numbers
    #     # TODO: After running it, add another entry to the dictionary and see how the layout changes
    names = ["Geoff", "Jacob"]

    def build(self):
        """Build the Kivy app from the kv file."""
        self.title = "Dynamic Stuff"
        self.root = Builder.load_file('very_simple_app.kv')
        return self.root

    def create_widgets(self):
        for name in self.names:
            temp_button = Label(text=name)
            print(name)
            # temp_button.bind(on_release=self.press_entry)
            # self.status_text = name
            self.root.ids.entries_box.add_widget(temp_button)


DynamicWidget().run()

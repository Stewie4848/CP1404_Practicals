class ProgrammingLanguage:
    def __init__(self, name="", typing="", reflection=bool, year=0):
        self.name = name
        self.typing = typing
        self.reflection = reflection
        self.year = year

    def is_dynamic(self):
        self.typing.lower()
        if self.typing == "dynamic":
            return True
        else:
            return False

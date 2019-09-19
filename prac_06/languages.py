from prac_06.programming_language import ProgrammingLanguage

ruby = ProgrammingLanguage("Ruby", "Dynamic", True, 1995)
python = ProgrammingLanguage("Python", "dynamic", True, 1991)
visual_basic = ProgrammingLanguage("Visual basic", "Static", False, 1991)
languages = [ruby, python, visual_basic]
print("The dynamically typed languages are:")
for language in languages:
    if language.is_dynamic():
        print(language.name)
# print(ruby)
# print(python)
# print(visual_basic)

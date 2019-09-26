from prac_06.guitar import Guitar

x = Guitar("Gibson", 1951, 2000)
y = Guitar("Alex", 1971, 500)
print(x)
print(y)
print("Expected: 68")
print("Got:", x.get_age())
print("Expected: True")
print("Got", x.is_vintage())
print("Expected: 48")
print("Got", y.get_age())
print("Expected: False")
print("Got", y.is_vintage())

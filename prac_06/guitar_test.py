from prac_06.guitar import Guitar

x = Guitar("Gibson", 1951, 2000)
y = Guitar("Alex", 1971, 500)
print(x)
print(y)

print(x.get_age())
print(x.is_vintage())
print(y.get_age())
print(y.is_vintage())

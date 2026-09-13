my_string = "Cybersecurity"
print(my_string[::-1])


test_string = "   aCCESS gRANTED tO uSER   "

print(test_string.strip())
print(test_string.capitalize())
print(test_string.title())
print(test_string.upper())
print(test_string.lower())

def find_discriminant(a, b, c):
    return (b ** 2) - (4 * a * c)

print(find_discriminant(2, 5, -3))
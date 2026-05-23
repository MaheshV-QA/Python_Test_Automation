# 1) \n => New Line
print("Hello\nWorld")
# Output:
# Hello
# World

# 2) \t => Horizontal Tab
print("Name:\tJohn")
# Output:
# Name:    John

# 3) \r => Carriage Return
print("Hello\rWorld")
# Output:
# World   (overwrites "Hello" with "World")

# 4) \b => Backspace
print("Helloo\b World")
# Output:
# Hello World  (removes the extra 'o')

# 5) \f => Form Feed (not usually visible, acts like a page break)
print("Hello\fWorld")
# Output:
# HelloWorld  (you may just see a strange character or spacing depending on your terminal)

# 6) \v => Vertical Tab (moves text down vertically, like a line break but not always visible)
print("Hello\vWorld")
# Output:
# HelloWorld  (similar to \n but with less support)

# 7) \' => Single Quote
print('It\'s a sunny day!')
# Output:
# It's a sunny day!

# 8) \" => Double Quote
print("He said, \"Hello!\"")
# Output:
# He said, "Hello!"

# 9) \\ => Backslash
print("This is a backslash: \\")
# Output:
# This is a backslash: \

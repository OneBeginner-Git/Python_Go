from sys import argv
script, filename = argv

txt = open(filename)
print("File name: %r"% filename)
print(txt.read())


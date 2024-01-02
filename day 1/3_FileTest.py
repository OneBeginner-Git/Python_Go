# coding=UTF-8

from sys import argv
script, filename = argv

txt = open(filename, encoding="utf-8")
print("File name: %r"% filename)
print(txt.read())
txt.close()

filename2 = input("Choose your file: ")
txt2 = open(filename2, encoding="utf-8")
print(txt2.read())
txt2.close()

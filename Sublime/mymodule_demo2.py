from mymodule import sayhi,__version__

sayhi()
print("Версия",__version__)

print(dir())

del sayhi

print(dir())
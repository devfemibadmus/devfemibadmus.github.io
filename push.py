import os, sys
os.system("git add .")
print("\033[1;33;40m no spacing in ur input rather use '-'")
a = input("\033[1;33;40m what did u do? \033[1;32m")
os.system("git commit -m "+str(a))
os.system("git push heroku master -f")
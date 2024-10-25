import os, sys
import vecto as ve

os.system("clear ; echo 'Från termianlen'")

print(f"{'='*30}main.py{'='*30}\n" )

print("Globals")
print(globals()['ve'])

print("sys.modules")
print(sys.modules['ve'])
import os

print(f"test things inside binder_test.py")
print(os.path.abspath(__file__))

def test():
    print("test() called inside binder_test.py")

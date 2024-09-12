import mysql.connector

# Exception Handling

def test():
    return 1/0

print("Start")

try:
    print(1)
    test()
    print(3)
except:
    print("Khata")
finally:
    print("Finally")

print("End")
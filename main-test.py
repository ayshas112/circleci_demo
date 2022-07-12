from main import add

def TestAdd():
    assert add(2, 3) == 5
    print("Add function works correctly")

if __name__ == '__main__':
    TestAdd()

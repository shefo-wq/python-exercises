x = 10

def one():
    global x
    x = 2
    print(f"print variable from global scope {x}")

def two():
    x = 4
    print(f"print variable from global scope {x}")

print(f"print variable from function scope {x}")
one()
two()
print(f"print variable from function scope {x}")
print(f"print variable from global scope after one function is called {x}")
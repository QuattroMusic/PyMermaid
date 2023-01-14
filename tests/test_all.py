import wrappers as w

total_info = [0, 0, 0]


def test_something(module: str):
    # dinamically import the module from a variable, execute it and store the result
    print(f"Testing {module}\n")
    __import__(module, fromlist=[''])

    total_info[0] += w.tests_info[0]
    total_info[1] += w.tests_info[1]
    total_info[2] += w.tests_info[2]
    w.clear_info()
    
    print("-----------\n")


# tests all files
test_something("flowchart")
test_something("requirement")

# print all tests info
print(f"Tests passed: {total_info[1]} / {total_info[1] + total_info[2]}")
print(f"Tests executed in {round(total_info[0], 6)}s\n")

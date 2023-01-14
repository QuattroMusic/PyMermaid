from time import time

# time spent, successful tests, unsuccessful tests
tests_info: list[int, int, int] = [0, 0, 0]


def test_this(func):
    """
    Wrapping function that returns the execution time of a function
    """
    start = time()
    result = func()  # for the tests we're not going to use args and kwargs
    end = time()
    failed = False

    # check if the result is the same as the expected
    if result[0] == result[1]:
        tests_info[1] += 1
        res = "test passed successfully"
    else:
        tests_info[2] += 1
        res = "test passed unsuccessfully"
        failed = True
    
    print(f"Executed {func.__name__} in {round(end - start, 4)}s, {res}")

    if failed:
        # print if we failed the test
        print(repr(result[0]))
        print(repr(result[1]))
    
    tests_info[0] += end - start


def evaluate_general():
    print()
    print(f"Tests passed: {tests_info[1]} / {tests_info[1] + tests_info[2]}")
    print(f"Tests executed in {round(tests_info[0], 6)}s\n")


def clear_info():
    global tests_info
    tests_info = [0, 0, 0]

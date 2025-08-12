from main_functions import return_characters_appearing_twice

# Simple test for characters appearing twice 
def tests_for_return_characters_appearing_twice():
    tests = [
        # Test 1 for original ouctome for caiopa with output of a
        (['c', 'a', 'i', 'o', 'p', 'a'], ['a']),
        # Test 2 for characters appearing twice with output of a and b
        (['a', 'b', 'a', 'b', 'c'], ['a', 'b']),
        # Test 3 for no repeats wtith output of empty list
        (['x', 'y', 'z'], []),
        # Test 4 for triple repeats with output of m
        (['m', 'm', 'm'], ['m']),  
        # Test 5 for empty input with output of empty list
        ([], []),
        # Test 6 for space char repeated
        (['a', ' ', 'b', ' ', 'c'], [' ']),  
    ]

    for i, (input_data, expected) in enumerate(tests, start=1):
        output = return_characters_appearing_twice(input_data)
        passed = output == expected
        print(f"Test {i}: Input={input_data} → Output={output} "
              f"Expected={expected} → {'PASS ✅' if passed else 'FAIL ❌'}")

if __name__ == "__main__":
    print("Running sample tests...\n")
    tests_for_return_characters_appearing_twice()

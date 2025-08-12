def return_characters_appearing_twice(chars: list[str]) -> list[str]:
    """
    An algorithm that given a string of characters, for example {'c','a','i','o','p','a'},
    will print out the list of characters appearing at least 2 times. 
    In this specific example, it would return {'a'}.
    """
    freq = {}
    for ch in chars:
        freq[ch] = freq.get(ch, 0) + 1

    seen = set()
    result = []
    for ch in chars:
        if ch not in seen and freq[ch] >= 2:
            result.append(ch)
            seen.add(ch)
    return result

# Time complexity: O(n) where n is the number of characters in the input list.
# Space complexity: O(k) in the worst case, where k is the number of unique characters in the input list.



def longestBalanced(s: str) -> int:
    """For this problem we have three cases
    case 1: only one letter exists
    case 2: if only two letters are equal a=b, b=c or a=c
    case 3: all three are equal
    """
    n = len(s)
    if n == 0:
        return 0

    # Best max_lenwer across all cases.
    max_len = 0

    # Case 1: substring contains only one distinct letter (e.g., "aaaa").
    # Longest such balanced substring is just the longest run of same char.
    run = 0
    prev = None
    for ch in s:
        if ch == prev:
            run += 1
        else:
            run = 1
            prev = ch
        if run > max_len:
            max_len = run

    # Case 2: substring contains exactly two letters with equal counts.
    # Do this for pairs: (a,b), (a,c), (b,c).
    for x, y in (("a", "b"), 
                 ("a", "c"),
                 ("b", "c")
                 ):
        diff = 0  # diff = count(x) - count(y) in current valid segment
        first = {0: -1}  # earliest index where each diff was seen

        for i, ch in enumerate(s):
            # Third letter breaks this pair-only segment.
            if ch != x and ch != y:
                diff = 0
                first = {0: i}
                continue

            # Update pair-difference state.
            diff += 1 if ch == x else -1

            # Same diff seen before => equal x/y counts in between.
            if diff in first:
                max_len = max(max_len, i - first[diff])
            else:
                first[diff] = i

    # Case 3: substring contains all three letters with equal counts.
    # Use prefix-state: (count(a)-count(b), count(a)-count(c)).
    ca = cb = cc = 0
    first = {(0, 0): -1}  # earliest index for each 2D state

    for i, ch in enumerate(s):
        if ch == "a":
            ca += 1
        elif ch == "b":
            cb += 1
        elif ch == "c":
            cc += 1

        state = (ca - cb, ca - cc)

        # Same state seen before => equal added counts of a,b,c in between.
        if state in first:
            max_len = max(max_len, i - first[state])
        else:
            first[state] = i

    return max_len

import string

import adventinput


SYMBOLS = "!\"#$%&'()*+,-/:;<=>?@[\]^_`{|}~"

def find_nums(line: str) -> list[(int, int)]:
    """
    Takes a line from the input and returns a list of tuples that represent the start and end
    indices of all the numbers found in that line

    Note: Can return an empty list if no numbers found.
    """
    res = []
    start = None
    for idx, c in enumerate(line):
        if c in string.digits and start is None:
            # New run of digits
            start = idx
        elif c not in string.digits and start is not None:
            # Run of digits has ended
            res.append((start, idx - 1))
            start = None

    if start is not None:
        # We finished iterating but we still had a run of digits
        res.append((start, idx)) # if this doesn't work, substitute len(line) for idx

    return res

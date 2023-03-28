def main(list1):
    """
    A list of several elements is given. True if all items are the same, otherwise return False.
    Args:
        list1 (list): parameter
    Returns:
        bool: return answer
    """
    x = 0
    while x < len(list1):
        if list1[0] == list1[x]:
            return True
        else:
            return False
        x += 1
    return list1

print(main(['x', 'x', 'y', 'y', 'z']))
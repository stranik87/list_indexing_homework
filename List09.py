def main(list1):
    """
    A list of several elements is given. True if all items are the same, otherwise return False.
    Args:
        list1 (list): parameter
    Returns:
        bool: return answer
    """
    x = all(list1)
    return x

print(main(['x', 'x', 'y', 'y', 'z']))
def main(list1):
    """
    A list of units and zeros with a length of five is given. Replace zero with False.
    Args:
        list1 (list): parameter
    Returns:
        list: return answer
    """
    x = 0

    while x < len(list1):
        if list1[x] == 0:
            list1[x] = False
        x += 1
    return list1

print(main([1, 0, 0, 0, 0]))
    
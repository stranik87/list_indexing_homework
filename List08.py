def main(list1):
    """
    A list of ones and zeros, five in length, is given. replace one with True, replace zeros with False.
    Args:
        list1 (list): parameter
    Returns:
        list: return answer
    """
    x = 0

    while x < len(list1):
        if list1[x] == 0:
            list1[x] = False
        else:
            list1[x] = True
        x += 1
    return list1, x

print(main([1, 0, 0, 0, 0]))
    
    
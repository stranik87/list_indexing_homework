def main(list1):
    """
    A list of several elements is given. True if all items are the same, otherwise return False.
    Args:
        list1 (list): parameter
    Returns:
        bool: return answer
    """
    x = len(list1)*[list1[0]]==list1
    print(x)
    return x
    


print(main([ 'z', 'y', 'y' ]))


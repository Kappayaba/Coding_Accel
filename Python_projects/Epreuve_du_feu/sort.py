import sys

#Exo 4

def print_sort(lst):
    if not(check_sort(lst)):
        return False
    else:
        answer = ''
        for i in higher_sort(lst):
            answer += '{} '.format(i)

        print(answer)
        return True


def check_sort(lst):
    """

    Check if a list is sorted.

    """
    for i in range(1, len(lst)):
        if(lst[i-1] < lst[i]):
            return False
    return True

def higher_sort(lst):
    """

    Sort a list, reverse gnome sort, recursive manner.

    """
    for i in range(1, len(lst)):
        if(lst[i-1] < lst[i]):
            replace = lst[i]
            del lst[i]
            lst.insert(0, replace)
            higher_sort(lst)
    return lst

def selective_sort(lst):
    min = lst[0]
    for i in range(len(lst)):
        if lst[i] < min:
            min = lst[i]
    lst.remove(min)
    lst.insert(0, min)
    print(lst)


def sort(arg):
    """

    Ask the way you want to sort a list and sort it.

    """

    lst = []

    for i in range(1, len(arg)):
        lst.append(int(arg[i]))


    higher_sort(lst)
    
    return print_sort(lst)

    # try:
    #     choice = int(input("""### HOW TO SORT ###\nRecursive : 1\nSelective : 2\n\nCHOICE : """))

    #     if choice == 1:
    #         return recursive_sort(lst)
    #     else:
    #         return selective_sort(lst)
    # except NameError:
    #     print("""\n\n #########################\n\n YOU NEED TO PUT AN 1 or 2\n\n #########################\n\n""")
    # except SyntaxError:
    #     print("""\n\n #########################\n\n YOU NEED TO PUT AN 1 or 2\n\n #########################\n\n""")

if __name__ == "__main__":
    sort(sys.argv)
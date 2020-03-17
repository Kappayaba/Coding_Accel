import sys

#Exo 4

def print_sort(lst):
    answer = ''
    for i in higher_sort(lst):
        answer += '{} '.format(i)


    print("")
    print(answer)


def switch_in_list(lst, coord1, coord2):
    a = lst[coord1]
    lst[coord1] = lst[coord2]
    lst[coord2] = a
    
    return lst

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
            print(lst)
            higher_sort(lst)
    return lst


def bubble_sort(lst):
    for i in range(1,len(lst)):
        for i in range(len(lst)-i):
            bubble = lst[i]
            if bubble > lst[i+1]:
                switch_in_list(lst, i, i+1)
        print(lst)
            
    return lst

def sort(arg):
    """

    Ask the way you want to sort a list and sort it.

    """

    lst = []

    for i in range(1, len(arg)):
        lst.append(int(arg[i]))
    
    try:
        choice = int(input("""### HOW TO SORT ###\n\nGnome method : 1\nBubble method : 2\n\n\nCHOICE : """))
        print("")
        if choice == 1:
            return print_sort(higher_sort(lst))
        elif choice == 2:
            return print_sort(bubble_sort(lst))

    except NameError:
        print("""\n\n #########################\n\n YOU NEED TO PUT AN 1 or 2\n\n #########################\n\n""")

    except SyntaxError:
        print("""\n\n #########################\n\n YOU NEED TO PUT AN 1 or 2\n\n #########################\n\n""")


if __name__ == "__main__":
    sort(sys.argv)
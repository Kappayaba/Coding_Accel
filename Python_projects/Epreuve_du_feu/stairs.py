#Exo 1
import sys
def stairs(n):
    for i in range(1,n+1):
        print( ' ' * (n - i) + '#' * i )

    return 0

if __name__ == "__main__":

    try:
        stairs(int(sys.argv[1]))
    except ValueError:
        print('~~~~~Put a number bro~~~~~')
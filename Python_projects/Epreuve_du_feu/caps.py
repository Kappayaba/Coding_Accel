#Exo 2
import sys
def Maj(string):
    new_string = ''

    for i in range(len(string)):
        if(i % 2 == 0):
            new_string += string[i].upper()
        else:
            new_string += string[i].lower()
    return new_string

if __name__ == "__main__":
    print(Maj(sys.argv[1]))
#Exo 2
import sys

def Maj(*arg):
    sentence = ''
    new_string = ''
    len_lst = []
    for string in arg[0]:
        len_lst.append(len(string))
        sentence += string 
    
    for i in range(len(sentence)):
        if i % 2 == 0:
            new_string += sentence[i].lower()
        else:
            new_string += sentence[i].upper()

    for e in len_lst:
        new_string = new_string[e:] + ' ' + new_string[:e]


    return new_string[1:]

if __name__ == "__main__":
    print(Maj(sys.argv[1:]))
#Exo 3
import sys
def factoriel(n):
    if(n==0):
        return 1
    else:
        return n * factoriel(n-1)

if __name__ == "__main__":
    print(factoriel(int(sys.argv[1])))
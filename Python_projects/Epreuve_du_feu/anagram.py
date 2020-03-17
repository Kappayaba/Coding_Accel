#Exo 5
import sys
def file_to_list(f1):
	f = open(f1)
	lst = []
	e = ''

	for l in f:
		lst.append(l.replace('\n', ''))

	f.close()

	return lst

def anagram(word, file):
    lst = file_to_list(file)
    answer = []


    for w in lst:
        puzzle = ''

        if w == word:
            answer.append(w)
            continue

        if len(w) != len(word):
            continue
    
        for letters in w:
            if w.count(letters) == word.count(letters):
                puzzle += letters
        
        if len(puzzle) == len(word):
            answer.append(w)

    return answer

if __name__ == "__main__":
    print(anagram(sys.argv[1], sys.argv[2]))
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
    word_list = list(word)
    word_list.sort()
    for w in lst:
        if w == word:
            answer.append(w)
            continue

        if len(w) != len(word):
            continue
    
        anagram_lst = list(w)
        anagram_lst.sort()

        if anagram_lst == word_list:
            answer.append(w)

    return answer


if __name__ == "__main__":
    try:
        print(anagram(sys.argv[1], sys.argv[2]))
    except IndexError:
        print('\n\n /!\ You forgot to put a word or the file of your dictionary /!\ \n\n')
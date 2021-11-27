f = open('Rosalind/rosalind_gc.txt').read()
a = list(f.split('>'))

def CGperc(string):
    dic = {'A':0, 'C':0, 'G':0, 'T':0}

    for a in string:
        if a == 'A':
            dic['A'] += 1
        elif a == 'T':
            dic['T'] += 1
        elif a == 'C':
            dic['C'] += 1
        elif a == 'G':
            dic['G'] += 1
    perc = (dic['C'] + dic['G'])/len(string)*100
    return perc


print(a)
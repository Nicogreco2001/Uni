f = open('Rosalind/rosalind_lcsm.txt').read()
list = list(f.split('>'))
n = 1
dnaseq = []
while n < len(list):
    list[n] = list[n].replace('\n', '')
    dnaseq.append(list[n][13:])
    n += 1
print(dnaseq)

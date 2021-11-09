k = int(input())
s = input()
s_lower = s.lower()
ab = 'a b c d e f g h i j k l m n o p q r s t u v w x y z'.split()
rot_ab = ['' for _ in range(26)]
c = 0
while c <= 25:
    if (c-k) >= 0:
        rot_ab[c-k] = ab[c]
        c += 1
    else:
        rot_ab[c-k+26] = ab[c]
        c+= 1
rot_s = ''
for a in s_lower:
    if a != '-':
        indx = ab.index(a)
        
        rot_s = F"{rot_s}{rot_ab[indx]}"
    else:
        rot_s = F"{rot_s}-"
print(rot_s)
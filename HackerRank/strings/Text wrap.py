string = "abcdefghij"
max_width = 3
for i in range(1,5):
    if i == 1:
        f = i * max_width
        string = string[:f] + "\n" + string[f:]
    else:
        f = i * (max_width+1)
        string = string[:f] + "\n" + string[f:]

print(string)
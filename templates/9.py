f = open('путь к файлу')
l = [list(map(int, i.split('\t'))) for i in f]

cnt = 0
for row in l:
    if (условия):
        cnt += 1

print(cnt)
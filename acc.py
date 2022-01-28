file1 = open('evalOut.outcon120.out.outcon119.outcon120.out.tsv', 'r')
#file1 = open('evalOut.foo09093.out.out09092.foo09093.out.tsv', 'r')
#file1 = open('copy1118.tsv', 'r')
#file1 = open('Newout.tsv', 'r')
line = file1.readline()
count = 0
wrongCount = 0
newcount = 0
goldLine = ''
predLine = ''
while line:
    if 'gold' in line:
        goldLine = line.replace('gold', 'predicted')
        goldLine = goldLine.strip()
        newcount += 1
    if 'predicted' in line:
        predLine = line.strip()
        if predLine == goldLine:
            count += 1
            print('found')
        else:
            print('not')
            print(count)
            print(predLine)
            print(goldLine)
            wrongCount += 1
    line = file1.readline()


print(count, wrongCount)
print(count/newcount)


import re
from word2number import w2n
file1 = open('evalOut.outcon119.out.outcon119.outcon119.out.tsv', 'r')
file2 = open('npcOut')
line = file1.readline()

count = 0
newcount = 0
goldLine = ''
predLine = ''
bothCor = 0
NPCCor = 0
ModelCor = 0
noneCor = 0

thresh = -5.2


while line:
    if 'gold' in line:
        goldLine = line.replace('gold', 'predicted')
        newcount += 1
    if 'predicted' in line:
        line21 = file2.readline()
        try:
            if line21[0] == '2':
                line21 = file2.readline()
        except:
            break
        line22 = file2.readline()
        line23 = file2.readline()
        predLine = line

        isNum = re.findall('one|two|three|four|five|six|seven|eight|nine|ten|fifteen|twenty|thirty|forty|fifty|sixty|seventy|eighty|ninety|hundred', line21)
        isDir = re.findall('left|right|north|south|east|west', line21)

        #print(predLine, '\n', goldLine, '\n', line21, '\n', line22, '\n', line23)

        confs = re.findall('-\d\.\d\d\d', line23)
        if len(confs) > 0:
            conf = float(confs[0])
        else:
            conf = -10

        goldLine = goldLine.replace(' ','')
        predLine = predLine.replace(' ', '')
        goldLine = goldLine.replace('\t', '')
        predLine = predLine.replace('\t', '')

        if len(isNum) >= 1:
        #if conf < thresh:
            if goldLine == predLine:
                count += 1
            else:
                print(goldLine)
                print(predLine)

        else:
            fScore = float(line22[len(line22) - 5:])
            if fScore > 0.9:
                count += 1
#-----------------
        '''
        if len(isDir) >= 1:
            # if conf < thresh:
            if goldLine == predLine:
                count += 1
            else:
                print(goldLine)
                print(predLine)

        else:
            fScore = float(line22[len(line22) - 5:])
            if fScore > 0.9:
                count += 1
        '''


    line = file1.readline()

print(count/183)

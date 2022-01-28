import re
file1 = open('evalOut.foo1118.out.out1118.foo1118.out.tsv', 'r')
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
ModelOnlyCor = 0
NPCOnlyCor = 0
modelError = 0
NPCError = 0
linecount = 0

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

        if predLine == goldLine:
            count += 1
            ModelCor += 1
            fScore = float(line22[len(line22) - 5:])
            if fScore > 0.9:
                bothCor += 1
                NPCCor += 1
            else:
                ModelOnlyCor += 1
                NPCError += 1
        else:
            modelError += 1
            fScore = float(line22[len(line22) - 5:])
            if fScore > 0.9:
                count += 1
                NPCOnlyCor += 1
                NPCCor += 1
            else:
                noneCor += 1

                count += 1
    if 'gold' not in line:
        if 'predicted' not in line:
            if 'taskDesc' not in line:
                if predLine != goldLine:
                    print(line)
                    linecount += 1

    line = file1.readline()

print(count/newcount)
print('Count', count)
print('Both Correct',bothCor)
print('None Correct',noneCor)
print('Model Correct',ModelCor)
print('NPC Correct',NPCCor)
print('NPC Only Correct',NPCOnlyCor)
print('Model Only Correct', ModelOnlyCor)
print('Model Total Error',modelError)
print('NPC Only Error',NPCError)
print('Line count', linecount/2)



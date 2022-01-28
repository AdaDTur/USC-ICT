import edlib
file1 = open('newOut.tsv', 'r')
line = file1.readline()
count = {}

while line:
    if 'predicted' in line:
        line = line.replace("predicted", "gold")
        r = edlib.align(goldLine, line, task='path')
        x = edlib.getNiceAlignment(r, goldLine, line)
        line = x['target_aligned']
        goldLine = x['query_aligned']
        for i in range(len(goldLine)):
            if (line[i] == '\t') and (goldLine[i] != '\t'):
                temp = list(goldLine)
                temp[i] = '\t'
                goldLine = ''.join(temp)
            elif (goldLine[i] == '\t') and (line[i] != '\t'):
                temp = list(line)
                temp[i] = '\t'
                line = ''.join(temp)
        predcommands = line.split('\t')

        predCom = (len(predcommands))
        goldcommands = goldLine.split('\t')
        goldCom = len(goldcommands)

        for i in range(1, predCom):
            goldsplit = goldcommands[i].split()
            predsplit = predcommands[i].split()
            #print(predcommands[i], goldcommands[i])
            if len(goldsplit) > 0 and len(predsplit) > 0:
                print(goldsplit[0] + "XXX" + predsplit[0])
                if('-' in predsplit[0]):
                    predsplit[0] = '-'
                if ('-' in goldsplit[0]):
                    goldsplit[0] = '-'
                if ('-' in predsplit[0] or predsplit[0] == 'go' or predsplit[0] == 'pick' or predsplit[0] == 'slice' or predsplit[0] == 'cool' or predsplit[0] == 'heat' or predsplit[0] == 'toggle' or predsplit[0] == 'clean' or predsplit[0] == 'put') and ('-'  in goldsplit[0] or goldsplit[0] == 'go' or goldsplit[0] == 'pick' or goldsplit[0] == 'slice' or goldsplit[0] == 'cool' or goldsplit[0] == 'heat' or goldsplit[0] == 'toggle' or goldsplit[0] == 'clean' or goldsplit[0] == 'put'):
                    if predsplit[0] + goldsplit[0] in count:
                         count[predsplit[0] + goldsplit[0]] += 1
                    else:
                        count[predsplit[0] + goldsplit[0]] = 1
    elif 'gold' in line:
        goldLine = line
    line = file1.readline()

#print(count)
for keys,values in count.items():
    print(keys,":",values)

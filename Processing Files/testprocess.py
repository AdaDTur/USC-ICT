import re
npcfile = open('npctest.txt')
file = open("npctest01", "w")
line = npcfile.readline()
pred = ''
npcpred = {}
utt = ''
count = 0
while line:
    line = line.lower()
    if line[0] == '2' or line[0] == '3':
        line = npcfile.readline()
        continue
    #print(line)
    elif str(count) + ')' in line:
        matches = re.findall('[^\(]+', line)
        utt = matches[0].strip()
        count += 1
    elif line[0] == '1':
        matches = re.findall('[^\(]+', line)
        pred = matches[0].strip()
        pred = pred.replace('1\t', '')
        #print(pred)
        npcpred[utt] = pred
        print(utt, ':', pred)
    elif 'F-Score' in line:
        pred = ''
    line = npcfile.readline()

norm = open('normTest0909.txt')
line = norm.readline()
while line:
    fields = line.split('\t')
    utt = fields[0].strip()
    if utt in npcpred:
        predOut = npcpred[utt]
    else:
        predOut = 'none'
    file.write(utt + ' [SEP] ' + predOut + '\t' + fields[1])
    line = norm.readline()
file.close()

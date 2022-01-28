import re
npcfile = open('npctxt')
file = open("npctrain01", "w")
line = npcfile.readline()
pred = ''
npcpred = {}
while line:
    if line[0] == '2' or line[0] == '3':
        line = npcfile.readline()
        continue
    #print(line)
    elif 'Anybody' in line:
        matches = re.findall('[^\(]+', line)
        utt = matches[0].strip()
        #print(utt + '...')
    elif line[0] == '1':
        matches = re.findall('[^\(]+', line)
        pred = matches[0].strip()
        pred = pred.replace('1\t', '')
        #print(pred)
        npcpred[utt] = pred
    elif 'F-Score' in line:
        pred = ''
    line = npcfile.readline()

norm = open('normTrain0909.txt')
line = norm.readline()
while line:
    matches = re.findall('[^\[]+', line)
    utt = matches[0].strip()
    if utt in npcpred:
        predOut = npcpred[utt]
    else:
        predOut = 'none'
    file.write(utt + ' [SEP] ' + predOut + ' [' + matches[1] + '\n')
    line = norm.readline()
file.close()
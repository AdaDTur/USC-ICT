import pandas as pd
import re
from num2words import num2words

data = pd.read_csv('NPCTrain.html', sep='\t', encoding = "ISO-8859-1")

count = 0
dataType = {}

'''
for i in range(len(data)):
    if data['Type'][i] not in dataType:
        dataType[data['Type'][i]] = 1
    else:
        dataType[data['Type'][i]] += 1
print(dataType)


file = open("train0806.txt", "w")

for i in range(len(data)):
    newText = data['Text'][i].lower()
    newText = re.sub(r'\d+', 'num', newText)
    newText = newText.replace('. . .', '')
    question = text2int(data['Question'][i].lower())
    question = re.sub(r'\d+', 'num', question)
    if ',' in newText:
        newText = newText.replace(',', ' <\s>')

    file.write(question + ' [SEP] ' + newText + ' <\s>' + ' [EOS] ' + '\n')
file.close()
'''

file = open("npcTrain01Norm.txt", "w")
for i in range(len(data)):
    newText = data['Text'][i].lower()
    match = re.findall(r'\d+', newText)
    for m in match:
        newText = newText.replace(m, num2words(m))
    newText = newText.replace('. . .', '')
    newText = newText.replace('-', ' ')
    question = data['Question'][i].lower()
    question = question.replace('-', ' ')
    match = re.findall(r'\d+', question)
    for m in match:
        question = question.replace(m, num2words(m))
    if ',' in newText:
        newText = newText.replace(',', ' <\s>')
    #match = re.findall(r'\d+', newText)
    file.write(question + ' [SEP] ' + newText + ' <\s>' + ' [EOS] ' + '\n')
file.close()
exit()
'''
#testing code \/

file = open("norm.txt", "w")
for i in range(len(data)):
    if data['Type'][i] == 'tr':
        newText = data['Text'][i].lower()
        match = re.findall(r'\d+', newText)
        for m in match:
            newText = newText.replace(m, num2words(m))
        newText = newText.replace('. . .', '')
        newText = newText.replace('-', ' ')
        question = data['Question'][i].lower()
        question = question.replace('-', ' ')
        match = re.findall(r'\d+', question)
        for m in match:
            question = question.replace(m, num2words(m))
        if ',' in newText:
            newText = newText.replace(',', ' <\s>')
        file.write(question + '\t' + newText + ' <\s>' + '\n')
file.close()
exit()
'''
'''
#non-tr
file = open("npcTest01.txt", "w")
for i in range(len(data)):
    newText = data['Text'][i].lower()
    match = re.findall(r'\d+', newText)
    for m in match:
        newText = newText.replace(m, num2words(m))
    newText = newText.replace('. . .', '')
    newText = newText.replace('-', ' ')
    question = data['Question'][i].lower()
    question = question.replace('-', ' ')
    match = re.findall(r'\d+', question)
    for m in match:
        question = question.replace(m, num2words(m))
    if ',' in newText:
        newText = newText.replace(',', ' <\s>')
    file.write(question + '\t' + newText + ' <\s>' + '\n')
file.close()
exit()

'''





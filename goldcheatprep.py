import pandas as pd
import re
from num2words import num2words

#data = pd.read_csv('NPCTrain.html', sep='\t', encoding = "ISO-8859-1")
data = pd.read_csv('traumTest.tsv', sep = '\t')


count = 0
dataType = {}
'''
file = open("goldTrain.txt", "w")
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
    file.write(question + ' [SEP] ' + newText + ' [SEP] ' + newText + ' <\s>' + ' [EOS] ' + '\n')
file.close()
'''
file = open("goldTest.txt", "w")
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
    file.write(question + ' [SEP] ' + newText + '\t' + newText + ' <\s>' + '\n')
file.close()
exit()

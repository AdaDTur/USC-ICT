import pandas as pd

data = pd.read_csv('traumTest.tsv', sep='\t', encoding = "ISO-8859-1")

count = 0
dataType = {}

for i in range(len(data)):
    if data['Type'][i] not in dataType:
        dataType[data['Type'][i]] = 1
    else:
        dataType[data['Type'][i]] += 1
print(dataType)

'''
file = open("train0720.txt", "w")

for i in range(len(data)):
    newText = data['Text'][i]
    if ',' in data['Text'][i]:
        newText = data['Text'][i].replace(',', ' <\s>')
    file.write(data['Question'][i].lower() + ' [SEP] ' + newText + ' <\s>' + ' [EOS] ' + '\n')
file.close()


file = open("trTrain0722.txt", "w")
for i in range(len(data)):
    if data['Type'][i] == 'tr':
        newText = data['Text'][i]
        if ',' in data['Text'][i]:
            newText = data['Text'][i].replace(',', ' <\s>')
        file.write(data['Question'][i].lower() + ' [SEP] ' + newText + ' <\s>' + ' [EOS] ' + '\n')
file.close()

'''
#testing code \/

file = open("trTest0722.txt", "w")
for i in range(len(data)):
    if data['Type'][i] == 'tr':
        newText = data['Text'][i]
        if ',' in data['Text'][i]:
            newText = data['Text'][i].replace(',', ' <\s>')
        file.write(data['Question'][i].lower() + '\t' + newText + ' <\s>' + '\n')
file.close()
'''

#non-tr

file = open("test0720.txt", "w")
for i in range(len(data)):
    newText = data['Text'][i]
    if ',' in data['Text'][i]:
        newText = data['Text'][i].replace(',', ' <\s>')
    file.write(data['Question'][i].lower() + '\t' + newText + ' <\s>' + '\n')
file.close()

'''







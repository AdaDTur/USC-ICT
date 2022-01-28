import random
lines = open('shuffle2.tsv').readlines()
random.shuffle(lines)
open('newshuff', 'w').writelines(lines)

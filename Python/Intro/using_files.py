with open('xmen.txt', 'w+') as f:
    f.write('Beast\n')
    f.write('Phoenix\n')
    f.writelines([
        'Cyclops\n',
        'Bishop\n',
        'Nightcrawler\n',
    ])

f = open('xmen.txt', 'r')
with f:
    print(f.read())
    print("Read again")
    f.seek(0)
    print(f.read())

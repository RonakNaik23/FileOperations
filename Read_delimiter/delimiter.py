
file = '/home/ronak/code/delimietr.dat'
with open(file, 'r') as de_lim:
    for line in de_lim:
        print ( line.split('|') )

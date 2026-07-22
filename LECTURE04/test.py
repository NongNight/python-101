rows = int(input('How many rows: '))
columns = int(input('How many columns: '))

for star in range(rows * columns): 
    if (star+1) % columns == 0 :
        print('')
    else:
        print("*",end="")
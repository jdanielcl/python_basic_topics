# continue, else, break

countries = ['Bogota','Colombia','America','Tierra']

for x in countries:
    if x == 'America':
        #jumps to the next iteration
        continue
    print(x)
else:
    print('Loop Finished!')


print("---------------")

for x in countries:
    if x == 'America':
        #jumps to the next iteration
        break
    print(x)
else:
    print('Loop Finished!')

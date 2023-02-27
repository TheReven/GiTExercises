Belgium = 'Belgium,10445852,Brussels,737966,Europe,1830,Euro,Catholicism,Dutch,French,German'

# a)

Belgium_hyphens = '-' * len(Belgium.split(',')[0])
print(Belgium_hyphens)
Brussels_hyphens = '-' * len(Belgium.split(',')[2])
print(Brussels_hyphens)

# b)

colons = Belgium.replace(',', ':')
print(colons)
semicolons = Belgium.replace(',', ';')
print(semicolons)

# c)

cities = Belgium.split(',')
population = int(cities[1]) + int(cities[3])
print(population)
population2 = int(cities[3]) + int(cities[5])
print(population2)
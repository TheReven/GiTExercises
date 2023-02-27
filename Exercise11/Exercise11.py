Belgium = 'Belgium,10445852,Brussels,737966,Europe,1830,Euro,Catholicism,Dutch,French,German'

# a)
Belgium_whole_hyphens = '-' * len(Belgium.split(','))
print(Belgium_whole_hyphens)
Belgium_hyphens = '-' * len(Belgium.split(',')[0])
print(Belgium_hyphens)
Brussels_hyphens = '-' * len(Belgium.split(',')[2])
print(Brussels_hyphens)

# b)

colons = Belgium.replace(',', ':')
print("String with Colons: " + colons)
semicolons = Belgium.replace(',', ';')
print("String with Semi Colons: " + semicolons)

# c)

cities = Belgium.split(',')
population = int(cities[1]) + int(cities[3])
print("Belgium + Brussels Population:", + population)

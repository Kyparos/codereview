'Знайти суму усіх числених значень списку'
spis = [['edef'], 'efdwefwe', 1, 1.2, 41, 'wdwdd']
suma = 0
for elem in spis:
    if isinstance(elem,(int,float)):
        suma+=elem
print(suma)
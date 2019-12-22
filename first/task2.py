'Залишити у списку лише слова у нижньому регістрі'
text = 'ghbhb UHEFUHF efuhefh HfeJfheu huhuhH efe j'
for word in text.split(' '):
    if word == word.lower():
        print(word, end=' ')

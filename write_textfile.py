fw = open('pycamp.txt', 'w', encoding='utf-8')

fw.write('Hello')
fw.write(' Python\n')

fw.close()

fa = open('pycamp.txt', 'a', encoding='utf-8')

fa.write('Hello, again.\n')
fa.write('Python\n')
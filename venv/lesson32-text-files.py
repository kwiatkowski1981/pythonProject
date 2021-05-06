# handler = open('test.txt')
# line = handler.readline()
# print(line)
# handler.close()

# with open('test.txt') as handler:
#     # line = handler.readline()
#     line2 = handler.readlines()   # kazda linia pokazuje sie jako element listy
#     # print(line)
#     print('\n')
#     print(line2)


with open('test.txt', 'r') as handler:  # 'r' domyśnie zaimplementowane, mozna pominac ale dla czytelnosci kodu dodawać
    for line in handler:
        print(line.strip())


with open('test.txt', 'a') as handler:
    handler.write('kolejna linijka dodana do pliku\n')
    print(line.strip())


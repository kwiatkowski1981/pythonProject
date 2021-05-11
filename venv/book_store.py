from json import load, dump

with open("book_store.json", "r") as data:
    book_store = load(data)
    print(data)
    # id, tytuły, autor, ilosci stron
    
    # dane pojedynczej książki
    print(f"ISBN: {book_store['isbn']}")
    print(f"Tytuł książki: {book_store['title']}")
    print(f"Ilość stron: : {book_store['pages']}")
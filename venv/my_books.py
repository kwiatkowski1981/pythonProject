from json import load, dump

with open("my_books.json", "r") as data:
    my_books = load(data)
    # print(my_books)
    print(f"Lista książek w sklepiku: {my_books['books']}")

    for book in my_books["books"]:
        print(f"ISBN - {book['isbn']} - \"{book['title']}\" napisana przez: {book['author']}"
              f" w {book['year']} roku. Zawiera {book['pages']} stron.")

    # for book in my_books["books"]:
    #     print(f"Tytuł książki: \"{book['title']}\"")
    #     print(f"Ilość stron: : {book['pages']}")

    author = input("Author: ")
    title = input("Title: ")
    isbn = input("ISBN: ")
    pages = input("Pages: ")
    year = input("Year: ")

    with open("my_books.json", "w") as data:
        my_books["books"].append({
            "id": len(my_books["books"]) + 1,
            "title": title,
            "isbn": isbn,
            "pages": pages,
            "year": year,
            "author": author
        })

        dump(my_books, data)

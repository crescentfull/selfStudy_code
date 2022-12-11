class Book:
    def __init__(self, title, author, pages):
        self.title = title
        self.author = author
        self.pages = pages
    def __str__(self):
        return f"제목 : {self.title}, 저자 : {self.pages}, 페이지수 : {self.pages} "
    
    # len() 함수를 페이지수를 리턴하게끔 만듬
    def len(self):
        return self.pages
    
if __name__ == "__main__":
    book = Book("python","sss",104)
    print(book)
    print("책 페이지 : ", book.len())
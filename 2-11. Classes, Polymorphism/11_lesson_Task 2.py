class Library(): 
    
    def __init__(self):
		self.books = []
		self.authors = []
        self.obj_book_id = Book(book_id)
        self.obj_author_name = Author(author_name)
    
    def book_lst(self):
		if i in self.books:
			if i.book_id == self.obj_book_id:
				raise ValueError('This book in library already')
			else: 
				self.books.append(self.obj_book_id, Book(year), self.obj_author_name)
        
    def group_by_author(self):
        for i in self.books:			
            if book[2] == Author(author_name):
                self.authors.append(i)
        return self.authors
    
    def group_by_year(self):
        for i in self.books:
            if book[1] == Book(year):
                self.books.append(book)
        return self.books
                             
class Book():
    def __init__(self, book_id, year, author_name):
        self.book_id = book_id
        self.year = year
        self.obj_author_name = Author(author_name)
	
	def __str__(self):
		return f'{book_id[self.book_id]}, {year[self.year]}'
		
class Author():

    def __init__(self, author_name, country, birthday):
        self.author_name = author_name
        self.country = country
        self.birthday = birthday
        
    def __str__(self):
		return f'{author_name[self.author_name]}, {country[self.country]}'


my_library = Library()
book_1 = [Book("Harry Potter and the Sercerer's Stone", 1997), Author("J.K Rowling", "England", "July 31, 1965")]   
book_2 = [Book("Harry Potter and the Chamber of Secrets", 1998), Author("J.K Rowling", "England", "July 31, 1965")]
book_3 = [Book("The Great Divorce", 1945), Author("C. S. Lewis", "England", "Nov 29, 1898")]


my_library.new_book(book_1)
print(my_library.book_by_year())

print(book_1)

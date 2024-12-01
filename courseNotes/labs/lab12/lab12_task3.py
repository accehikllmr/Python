from typing import List
import doctest

class Book:
    """ A class of a book. """
    def __init__(self, title: str, author: str, publication_year: int, isbn: str) -> None:
        """
        Constructor of the class Book.
        The accepted book range is from 1900 (including) to the current year (e.g., 2023)
        isbn is a string consist of 10 or 13 digits (and digits only)
        
        >>> programming_book = Book("Introduction to Programming", "Sam", 2003, "7623256234")
        >>> programming_book._title
        'Introduction to Programming'
        >>> programming_book._author
        'Sam'
        >>> programming_book._publication_year
        2003
        >>> programming_book._isbn
        '7623256234'
        """
        
        pass

    def get_title(self) -> str:
        """
        Get the title of the book
        
        >>> programming_book = Book("Introduction to Programming", "Sam", 2003, "7623256234")
        >>> programming_book.get_title()
        'Introduction to Programming'
        """
        
        pass
    
    def get_author(self) -> str:
        """
        Get the author of the book
        
        >>> programming_book = Book("Introduction to Programming", "Sam", 2003, "7623256234")
        >>> programming_book.get_author()
        'Sam'
        """
        
        pass
    
    def get_publication_year(self) -> str:
        """
        Get the author of the book
        
        >>> programming_book = Book("Introduction to Programming", "Sam", 2003, "7623256234")
        >>> programming_book.get_publication_year()
        2003
        """
        
        pass
    
    def get_isbn(self) -> str:
        """
        Get the ISBN of the book
        
        >>> programming_book = Book("Introduction to Programming", "Sam", 2003, "7623256234")
        >>> programming_book.get_isbn()
        '7623256234'
        """
        
        pass      

    def __str__(self) -> str:
        """
        The string representation of an instance
        
        >>> programming_book = Book("Introduction to Programming", "Sam", 2003, "7623256234")
        >>> print(programming_book)
        Title: Introduction to Programming, Author: Sam, Year: 2003, ISBN: 7623256234
        """
        
        pass

    def __eq__(self, other) -> bool:
        """
        Return whether two books are the same book. It is the same if and only if the ISBN is the same as ISBN uniquely identify a book.
        
        >>> programming_book_1 = Book("Introduction to Programming", "Sam", 2003, "7623256234")
        >>> programming_book_2 = Book("Introduction to Programming", "Sam", 2013, "9782352438")
        >>> programming_book_1 == programming_book_2
        False
        """
        
        pass


class Library:
    """ A library that stores only one copy of each book """
    
    def __init__(self) -> None:
        """
        Constructor
        
        >>> my_library = Library()
        >>> my_library._books
        []
        """
        
        pass

    def get_books(self) -> List[Book]:
        """
        Get all the books
        
        >>> programming_book = Book("Introduction to Programming", "Sam", 2003, "7623256234")
        >>> my_library = Library()
        >>> my_library._books = [programming_book]
        >>> len(my_library.get_books)
        1
        """
        
        pass

    def add_book(self, book: Book) -> None:
        """
        Add a book to the library. The book is not added is the library already has the book.
        
        >>> programming_book = Book("Introduction to Programming", "Sam", 2003, "7623256234")
        >>> my_library = Library()
        >>> my_library.add_book(programming_book)
        >>> my_library._books[0] is programming_book
        True
        """
        
        pass

    def search_by_title(self, title: str) -> List[Book]:
        """
        Return a list of Book with the title provided
        
        >>> programming_book = Book("Introduction to Programming", "Sam", 2003, "7623256234")
        >>> music_book = Book("Music", "Sam", 1992, "6123556127")
        >>> my_library = Library()
        >>> my_library.add_book(programming_book)
        >>> my_library.add_book(music_book)
        >>> my_library.search_by_title("Introduction to Programming")[0] is programming_book
        True
        """
        
        pass

    def search_by_author(self, author: str) -> List[Book]:
        """
        Return a list of Book written by author
        
        >>> programming_book = Book("Introduction to Programming", "Sam", 2003, "7623256234")
        >>> music_book = Book("Music", "Sam", 1992, "6123556127")
        >>> my_library = Library()
        >>> my_library.add_book(programming_book)
        >>> my_library.add_book(music_book)
        >>> sam_books = my_library.search_by_author("Sam")
        >>> programming_book in sam_books and music_book in sam_books
        True
        """
        
        pass

    def search_by_isbn(self, isbn: str) -> Book:
        """
        Return the book with the isbn. Return None if the book cannot be found
        
        >>> programming_book = Book("Introduction to Programming", "Sam", 2003, "7623256234")
        >>> music_book = Book("Music", "Sam", 1992, "6123556127")
        >>> my_library = Library()
        >>> my_library.add_book(programming_book)
        >>> my_library.add_book(music_book)
        >>> book_to_find = my_library.search_by_isbn("7623256234")
        >>> book_to_find is programming_book
        True
        """
        
        pass

    def __str__(self) -> str:
        """
        Return a string representation that include all the book information
        
        >>> programming_book = Book("Introduction to Programming", "Sam", 2003, "7623256234")
        >>> music_book = Book("Music", "Sam", 1992, "6123556127")
        >>> my_library = Library()
        >>> my_library.add_book(programming_book)
        >>> my_library.add_book(music_book)
        >>> print(my_library)
        Title: Introduction to Programming, Author: Sam, Year: 2003, ISBN: 7623256234
        Title: Music, Author: Sam, Year: 1992, ISBN: 6123556127
        """
        
        pass

if __name__ == '__main__':
    doctest.testmod()


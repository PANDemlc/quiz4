from dataclasses import dataclass

@dataclass
class Book:
    title: str
    author: str
    pages: int
    price: float

    def description(self) -> str:
        return f"{self.title} was written by {self.author} with {self.pages} pages for only ${self.price}!"
    
book = Book("Cool Book", "Braden B", 999, 19.99)
print(book.description())
from fastapi import FastAPI, Body
import copy

app = FastAPI()

BOOKS = [
  {
    "id": "1",
    "title": "Harry Potter and the Sorcerer's Stone",
    "original_uk_title": "Harry Potter and the Philosopher's Stone",
    "publication_year": 1997,
    "order": 1,
    "page_count": {
      "us_scholastic_hardcover": 309,
      "uk_bloomsbury_hardcover": 223
    },
    "categories": ["Fantasy", "Adventure", "Coming-of-Age", "School Story"]
  },
  {
    "id": "2",
    "title": "Harry Potter and the Chamber of Secrets",
    "publication_year": 1998,
    "order": 2,
    "page_count": {
      "us_scholastic_hardcover": 341,
      "uk_bloomsbury_hardcover": 251
    },
    "categories": ["Fantasy", "Mystery", "Adventure", "School Story"]
  },
  {
    "id": "3",
    "title": "Harry Potter and the Prisoner of Azkaban",
    "publication_year": 1999,
    "order": 3,
    "page_count": {
      "us_scholastic_hardcover": 435,
      "uk_bloomsbury_hardcover": 317
    },
    "categories": ["Fantasy", "Mystery", "Time Travel", "Coming-of-Age"]
  },
  {
    "id": "4",
    "title": "Harry Potter and the Goblet of Fire",
    "publication_year": 2000,
    "order": 4,
    "page_count": {
      "us_scholastic_hardcover": 734,
      "uk_bloomsbury_hardcover": 636
    },
    "categories": ["Fantasy", "Adventure", "Sports & Competition", "Dark Fantasy"]
  },
  {
    "id": "5",
    "title": "Harry Potter and the Order of the Phoenix",
    "publication_year": 2003,
    "order": 5,
    "page_count": {
      "us_scholastic_hardcover": 870,
      "uk_bloomsbury_hardcover": 766
    },
    "categories": ["Fantasy", "Political Drama", "Coming-of-Age", "Dark Fantasy"]
  },
  {
    "id": "6",
    "title": "Harry Potter and the Half-Blood Prince",
    "publication_year": 2005,
    "order": 6,
    "page_count": {
      "us_scholastic_hardcover": 652,
      "uk_bloomsbury_hardcover": 607
    },
    "categories": ["Fantasy", "Mystery", "Romance", "Tragedy"]
  },
  {
    "id": "7",
    "title": "Harry Potter and the Deathly Hallows",
    "publication_year": 2007,
    "order": 7,
    "page_count": {
      "us_scholastic_hardcover": 759,
      "uk_bloomsbury_hardcover": 607
    },
    "categories": ["Fantasy", "Adventure", "War & Rebellion", "Tragedy"]
  }
]

@app.get("/health")
async def health_check():
    return {"status": "healthy"}

@app.get("/api/books")
def get_books(category: str = None):
    filtered_books = copy.deepcopy(BOOKS)
    if category:
        filtered_books = [book for book in filtered_books if category in book.get("categories")]
    return {
        "data": filtered_books
    }

@app.get("/api/books/id/{book_id}")
async def get_book_detail(book_id: str):
    print(f"book_id is {book_id}")
    for book in BOOKS:
        if book_id == book.get("id"):
            return book

@app.get("/api/books/year/{publication_year}")
async def get_book_detail_by_year(publication_year: str):
    print(f"Input publication_year is {publication_year}")
    for book in BOOKS:
        print(f"publication_year is {book.get("publication_year")}")
        if publication_year == str(book.get("publication_year")):
            return book
    return {
        "message": "Book Not Found"
    }

@app.get("/api/books/publication_years")
async def get_publication_years():
    years = [book.get("publication_year") for book in BOOKS]
    return years
        
@app.post("/api/books")
async def create_book(payload=Body()):
    BOOKS.append(payload)

    return {
        "status": "success",
        "message": "Book created"
    }



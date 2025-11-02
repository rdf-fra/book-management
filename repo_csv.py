import csv # to handle CSV files

def load_books(filename):
    """Return all books from a CSV file as a list of dictionaries."""
    with open(filename) as csvfile:
        reader = csv.DictReader(csvfile, delimiter=';')
        # Return a list of dictionaries
        return list(reader) 
    
def save_books(filename, list_of_books):
    """Save all books to the CSV file.

    Args:
        filename (str): The path to the CSV file.
        list_of_books (list of dict): List of dictionaries, each representing a book.
    """
    if not list_of_books:
        # raise an ValueError if the list is empty
        raise ValueError("The list of books is empty.")
    
    with open(filename, "w", newline="") as csvfile:
        # define the columns
        fieldnames = ["isbn", "title", "categorie", "total", "available"]
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames, delimiter=";")
        writer.writeheader()
        writer.writerows(list_of_books)
        


library = {
    1: {"title": "1984", "author": "George Orwell", "status": "available"},
    2: {"title": "Devils", "author": "Dostoyevski", "status": "borrowed"},
    3: {"title": "Pig Farm", "author": "George Orwell", "status": "borrowed"},
    4: {"title": "Pod Igoto", "author": "Ivan Vazov", "status": "available"}
}

def querry_books(library, *args):
    result = []
    for library_name, library_details in library.items():
        if any(arg in library_details.values() for arg in args):
            result.append(library_details["title"])
    return result
    
def update_books(library, **keys):
    for library_name, library_details in library.items():
         for key, values in keys.items():
            if library_details["status"] != values and library_details["title"] == str(key):
                 library_details["status"] = values
                 print(f"Updated '{key}' to status: '{values}'")
            elif key != library_details["title"]:
                print(f"Book {key} not found, thus status is not set")





print("Query Results:", querry_books(library, "available", "Ivan Vazov"))

print(update_books(library,**{"1984": "borrowed", "Devils": "available"}))
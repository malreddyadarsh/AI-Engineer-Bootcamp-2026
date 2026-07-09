def add_movie(movies):
    name=input("Enter movie name :").strip().lower()
    for movie in movies:
        if movie==name:
            print("Movie already exists.")
            return 
    movies.append(name)
    print("Movie added successfully.")
    return movies

def remove_movie(movies):
    name=input("Enter movie name for removal :").strip().lower()
    for movie in movies:
        if movie==name:
            movies.remove(movie)
            print("Movie removed Successfully.")
            return movies
    print ("Movie not found")

def search_movie(movies):
    name=input("Enter movie name for searching :").strip().lower()
    for movie in movies:
        if movie==name:
            print("Movie name found in the list")
            print(movie,"at position ", movies.index(movie) )
            return
    print("Movie name not found.")

def sort_alphabetically(movies):
    sort_movies=movies.copy()
    sort_movies.sort()
    print(sort_movies)
    return

def display_all(movies):
    print("\n====Movies List====")
    i=0
    for movie in movies:
        print(" :",i," ",movie)
        i+=1
    return

def menu():
    print("\n====Movie Collection Manager====")
    print("1. Add movie")
    print("2. Remove movie")
    print("3. Search movie")
    print("4. Sort alphabetically")
    print("5.Display all movies")
    print("6. Exit")

def main():
    movies=[]
    while True:
        menu()
        ch=int(input("Enter your choice: "))
        if ch==1:
            add_movie(movies)
        elif ch==2:
            remove_movie(movies)
        elif ch==3:
            search_movie(movies)
        elif ch==4:
            sort_alphabetically(movies)
        elif ch==5:
            display_all(movies)
        elif ch==6:
            print("Thank you for choosing")
            break
        else:
            print("Invalid option")

main()

movies = {
    "Django Unchained": {
        "John": 10,
        "Jack": 9
    },
    "Troy": {}
}
def find_movie(movie_name):
    return movies.get(movie_name)

def add_movie(movie_name):
    if movie_name in movies:
        print("This movie already exists!")
    else:
        movies[movie_name] = {}
        print("Movie added successfully")

def add_rating(movie_name):
    movie = find_movie(movie_name)
    if movie is None:
        print("этот фильм не существует")
        return

    user_name = input("Введите свое имя: ")
    if user_name in movie:
        print("вы оценили этот фильм.")
        return

    rating = float(input("Введите свой рейтинг (0-10): "))
    if rating < 0 or rating > 10:
        print("рейтинг должен быть от 0 до 10")
        return

    movie[user_name] = rating
    print(f"для фильма {movie_name}добавлен рейтинг: {user_name} оценил его {rating}")

def display_ratings():
    for movie_name, ratings in movies.items():
        if not ratings:
            print(f"Rating is not yet available for {movie_name}")
        else:
            avg_rating = sum(ratings.values()) / len(ratings)
            print(f"{movie_name} is rated {avg_rating:.1f}")

while True:
    print("\n=== СИСТЕМА РЕЙТИНГОВ ===")
    print("1. добавить фильм ")
    print("2. добавить рейтинг фильму ")
    print("3. посмотреть рейтинг всех фильмов")
    print("4. выход")

    choice = input("Введите ваш выбор (1-4): ")

    if choice == "1":
        movie_name = input("Введите название фильма: ").strip().title()
        add_movie(movie_name)

    elif choice == "2":
        movie_name = input("Enter the movie name: ").strip().title()
        add_rating(movie_name)

    elif choice == "3":
        display_ratings()

    elif choice == "4":
        print("выход из программы...")
        break

    else:
        print("Invalid choice. Please enter a number from 1 to 4.")
        
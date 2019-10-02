# menu() should run all the functions whilst the user wants to
# process_input() returns what the user wants to do: add a movie, search, exit etc
# add_movie() lets the user add a movie to the movies dictionary
# search for a movie lets the user search for all movies in the dictionary with a given key-value
# exit exits the menu loop


def menu():
    movies = [
        {'name': 'Die Hard', 'year': '2001', 'genre': 'action'},
        {'name': 'Mulan', 'year': '2001', 'genre': 'disney'},
        {'name': 'Mean Girls', 'year': '2008', 'genre': 'teen'}
    ]
    process = 'a'
    while process != 'e':
        process = input('What do you want to do: add a movie (a), see your movies (c) search the database (s) or exit (e)? ')
        if process == 'a':
            add_movie(movies)
        elif process == 'c':
            see_all_movies(movies)
        elif process == 's':
            search_movies(movies)
        else:
            print('Leaving the database')


def add_movie(movie_database):
    name = input('Please enter the name of the movie you want to add: ')
    year = input('Please enter the year of the movie you want to add: ')
    genre = input('Please entre the genre of the movie you want to add: ').lower()
    movie_database.append({'name': name, 'year': year, 'genre': genre})


def see_all_movies(movie_database):
    name_list = []
    for movie in movie_database:
        name_list.append(movie['name'])
        names_to_print = ', '.join(name_list)
    print(f'The names of the movies in your database are: {names_to_print}')


def search_movies(movie_database):
    search_category = input('Do you want to search for year (year) or genre (genre)? ')
    search_criteria = input(f'Please enter the {search_category} you want to search for: ')
    successful_search_store = []
    for movie in movie_database:
        if movie[search_category] == search_criteria:
            successful_search_store.append(movie['name'])
    successful_search_to_print = ', '.join(successful_search_store)
    print(f'The movies with a {search_category} of {search_criteria} are {successful_search_to_print}')


menu()

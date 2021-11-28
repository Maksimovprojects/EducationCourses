# RUNESTONE ENVIRONMENT
import requests_with_caching
import json
import requests

def get_movies_from_tastedive(word):
    url = "https://tastedive.com/api/similar"
    param_dict = {"q": word, "type": "movies", "limit": "5"}
    get_movies = requests_with_caching.get(url, params=param_dict)
    get_movies_js = get_movies.json()
    return get_movies_js
get_movies_from_tastedive("Black Panther")


def extract_movie_titles(get_movies_js):
    lst_mov = []
    for dic in get_movies_js['Similar']['Results']:
        lst_mov.append(dic['Name'])
    return lst_mov
extract_movie_titles(get_movies_from_tastedive("Tony Bennett"))


def get_related_titles(lst):
    upd_lst = []
    for name in lst:
        upd_lst.extend(extract_movie_titles(get_movies_from_tastedive(name)))
    return list(set(upd_lst))
get_related_titles(["Black Panther", "Captain Marvel"])


def get_movie_data(word):
    url = 'http://www.omdbapi.com/'
    params_dict = {'t': word, "r": 'json'}
    omdb_resp = requests_with_caching.get(url, params=params_dict)
    return omdb_resp.json()


def get_movie_rating(ombd_data):
    data_lst = ombd_data["Ratings"]
    for dic in data_lst:
        if dic['Source'] == "Rotten Tomatoes":
            return int(dic["Value"][:2])   #num = ombd_data["Ratings"][1]["Value"][:2],   return int(num)
    return 0
get_movie_rating(get_movie_data("Deadpool 2"))

def get_sorted_recommendations(list):
    new_list = get_related_titles(list)
    print(new_list)
    print("------------------------------------------------")
    new_dict = {}
    for i in new_list:
        rating = get_movie_rating(get_movie_data(i))
        new_dict[i] = rating
    print(new_dict)
    print("------------------------------------------------")
    #print(sorted(new_dict, reverse=True))
    print([i[0] for i in sorted(new_dict.items(), key=lambda item: (item[1], item[0]), reverse=True)])
    return [i[0] for i in sorted(new_dict.items(), key=lambda item: (item[1], item[0]), reverse=True)]



def get_sorted_recommendations(lst):
    mov_lst = get_related_titles(lst)
    key_lst = []
    for name in lst:
        key_lst.append(get_movie_rating(get_movie_data(name))
    mov_key = list(zip(new_lst, key_lst))
    sort_lst = sorted(get_related_titles(lst), reverse=True, key=lambda)
    return sort_lst

get_sorted_recommendations(["Bridesmaids", "Sherlock Holmes"])

#-------------------------------------------------------------------------

def get_sorted_recommendations(list):
    new_list = get_related_titles(list)
    new_dict = {}
    for i in new_list:
        rating = get_movie_rating(get_movie_data(i))
        new_dict[i] = rating
    print(new_dict)
    #print(sorted(new_dict, reverse=True))
    return [i[0] for i in sorted(new_dict.items(), key=lambda item: (item[1], item[0]), reverse=True)]






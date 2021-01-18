import os
from flask import Flask, render_template, request,json, jsonify, current_app as app

app = Flask(__name__)

movies_path = os.path.join(app.static_folder, 'data', 'movies.json')

@app.route('/')
def movies():
    with open(movies_path, 'r') as jsondata:
        movies = json.load(jsondata)
    return jsonify(movies)

@app.route('/movies/search', methods=['GET'] )
def movies_list():
    results = []

    with open(movies_path, 'r') as jsondata:
        movies = json.load(jsondata)

    if 'cast' in request.args:
        cast = request.args['cast']

        for movie in movies:

            if cast in movie['cast']:
                results.append(cast)


    if 'genres' in request.args:
        genres = request.args['genres']

        for movie in movies:

            if genres in movie['genres']:
                results.append(genres)


    if 'title' in request.args:
        title_search = request.args['title'].lower()

        for movie in movies:
            for title in movie["title"]:

                if title_search in title.lower():
                    print("This is a movie in our data.")
                    results.append(movie)  


    if 'year' in request.args:
        year = request.args['year']

        for movie in movies:           
            if (year == str(movie['year'])):
                
                print("Movie found")
                results.append(movie)


    if (len(results) == 0):
        return "No movies were found with that search."
    else:
        return render_template(jsonify(results))



if __name__ == '__main__':
    app.run( debug=True, host='0.0.0.0')

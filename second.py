from flask import Flask, request, jsonify

app = Flask(__name__)

books_list = [

    {
        "id": 0,
        "author": "lucky saini",
        "language": "hindi",
        "title": "enjoy"
    },
    {
        "id": 1,
        "author": "ayush saini",
        "language": "english",
        "title": "make"
    },
    {
        "id": 2,
        "author": "deepika saini",
        "language": "grammer",
        "title": "create"
    },
    {
        "id": 3,
        "author": "hitesh saini",
        "language": "super",
        "title": "man"
    }

]


# @app.route('/books', method=['GET', 'POST'])
@app.route('/books', methods=['GET', 'POST'])
def books():
    if request.method == 'GET':
        if len(books_list) > 0:
            return jsonify(books_list)
        else:
            return 'Nothing Found', 404
    if request.method == 'POST':
        new_author = request.form['author']
        new_lan = request.form['language']
        new_tit = request.form['title']
        iD = books_list[-1]['id'] + 1
        new_obj = {
            "id": iD,
            "author": new_author,
            "language": new_lan,
            "title": new_tit

        }
        books_list.append(new_obj)
        return jsonify(books_list), 201


@app.route('/book/<int:id>', methods=['GET', 'PUT', 'DELETE'])
def single_book(id):
    if request.method == 'GET':
        for book in books_list:
            if book['id'] == id:
                return jsonify(book)
            pass
    if request.method == 'PUT':
        for book in books_list:
            if book['id'] == id:
                book['author'] = request.form['author']
                book['language'] = request.form['language']
                book['title'] = request.form['title']
                updated_bool = {
                    'id': id,
                    'author': book['author'],
                    'language': book['language'],
                    'title': book['title'],

                }
                return jsonify(updated_bool)
    if request.method == 'DELETE':
        for index , book in enumerate(books_list):
            if book['id'] ==id:
                books_list.pop(index)
                return jsonify(books_list)



if __name__ == '__main__':
    app.run(debug=True)

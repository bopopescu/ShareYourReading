from flask import Flask, render_template, request, redirect, url_for, session
import config
from models import User, Post
from exts import db
from decorator import login_required
from lxml import etree
import requests


key = "swpFwgtISW6ufbWB5ffFug"

app = Flask(__name__)
app.config.from_object(config)
db.init_app(app)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/login/', methods={'GET', 'POST'})
def login():
    if request.method == 'GET':
        return render_template('login.html')
    else:
        username = request.form.get('username')
        password = request.form.get('password')
        user = User.query.filter(User.username == username, User.password == password).first()
        if user:
            session['user_id'] = user.id
            # If you want to stay logged in for 31 days
            session.permanent = True
            return redirect(url_for('index'))
        else:
            return u'Login failed. Wrong username or password'


@app.route('/register/', methods={'GET', 'POST'})
def register():
    if request.method == 'GET':
        return render_template('register.html')
    else:
        username = request.form.get('username')
        password1 = request.form.get('password1')
        password2 = request.form.get('password2')
        user_type = 0

        if len(username) == 0:
            return u'The username cannot be empty!'
        if len(username) > 20:
            return u'The username exceed 20 characters!'
        if len(password1) > 20:
            return u'The password exceed 20 characters!'
        if len(password1) < 6:
            return u'The password is too short!'

        # If the user name is registered, it can no longer be registered
        user = User.query.filter(User.username == username).first()
        if user:
            return u'The username has been registered!'
        else:
            # psw1need to be equal to psw2
            if password1 != password2:
                return u'The two passwords are not identical. Please enter again.'
            else:
                user = User(username=username, password=password1, user_type=user_type)
                db.session.add(user)
                db.session.commit()
                # If the registration is successful, the page will jump to the login page
                return redirect(url_for('login'))


@app.route('/search/', methods={'GET', 'POST'})
def search():
    if request.method == 'GET':
        q = request.args.get('q')
        params = {"key": key,
                  "q": q}
        res = requests.get(url="https://www.goodreads.com/search/index.xml", params=params)
        # print(res.content)

        data = etree.XML(res.content)

        num = 0
        ratings = []
        titles = []
        book_ids = []
        authors = []
        urls = []
        for a in data.iter('work'):
            book_rating = a.find('average_rating').text
            ratings.append(book_rating)

            book_title = a.find('best_book').find('title').text
            titles.append(book_title)

            book_id = a.find('best_book').find('id').text
            book_ids.append(book_id)

            author = a.find('best_book').find('author').find('name').text
            authors.append(author)

            image_url = a.find('best_book').find('image_url').text
            urls.append(image_url)

            num = num + 1
        context = {
            'num': num,
            'book_ids': book_ids,
            'book_titles': titles,
            'book_authors': authors,
            'book_ratings': ratings,
            'image_urls': urls

        }
        return render_template('search.html', **context)


# @login_required
@app.route('/trends/', methods={'GET'})
def trends():
    context = {
        # 'posts': Post.query.order_by('-post_time').all()
        'posts': Post.query.all()
    }

    return render_template('trends.html', **context)


@app.route('/bd/<book_id>')
def bd(book_id):
    # params = {"key": key,
    #           "id": book_id}
    # res = requests.get(url="https://www.goodreads.com/book/show.xml", params=params)
    # data = etree.XML(res.content)
    # title = data.find('title').text
    context = {

    }
    return render_template('book_detail.html', **context)

@app.route('/pd/<post_id>')
def pd(post_id):
    post_model = Post.query.filter(Post.post_id == post_id).first()
    return render_template('post_detail.html', post=post_model)


@app.route('/add_comment/',methods=['POST'])
def add_comment():
    content = request.form.get('comment_content')


@app.route('/logout/')
def logout():
    session.pop('user_id')
    # way2: del session['user_id']
    # way3: session.clear()
    return redirect(url_for('login'))


@app.route('/pd')
@app.context_processor
def my_context_processor():
    user_id = session.get('user_id')
    if user_id:
        user = User.query.filter(User.id == user_id).first()
        if user:
            return {'user': user}
    return {}


if __name__ == '__mian__':
    app.run()

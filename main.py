from flask import Flask, request, redirect, render_template
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['DEBUG'] = True
app.config['SQLALCHEMY_DATABASE_URI']= 'mysql+pymysql://build-a-blog:lc101@localhost:8888/build-a-blog'
app.config['SQLALCHEMY_ECHO'] =True

db = SQLAlchemy(app)

class Blog(db.model):
    id = db.Column(db.Integer, primary_key = True)
    title = db.Column(db.String(120))
    body = db.Column(db.String(120))

    def __init__(self, title, body):
        self.title = title
        self.body = body 

@app.route('/')
def index():
    return render_template('base.html')

@app.route("/blog", methods=['GET'])
def blog():
    blog_id = request.args.get('id')
    
    if blog_id == None:
        blog = Blog.query.filter_by(id = blog_id).all()
        return render_template('base.html', title = title, blog=blog)

    else:
        blog = Blog.query.get(blog_id.desc()).all()
        return render_template('base.html', title = title, blog=blog)
   

@app.route("/new_post", methods=['POST', 'GET'])
def new_post():

    if request.method == 'POST':
        blog_title = request.form['blog-title']
        blog_body = request.form['blog-entry']
        title_error = ''
        body_error = ''

        if not blog-title:
            title_error = "Please enter a blog title"
        if not blog_body:
            body_error = "Please enter a blog entry"
        if not title_error and not body_error:
            new_post = Blog(blog_title, blog_body)
            db.session.add(new_post)
            db.session.commit()
            return redirect('/blog?id={}'.format(new_post.id))
        else:
            return render_template('newpost.html', title = "Add a New Entry", header='New Entry', blog_title=blog_title, blog_body=blog_body, title_error=title_error, body_error=body_error)

    return render_template('new_post.html, title = 'Add a New Entry')

if __name__ == '__main__':
    app.run()
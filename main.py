from flask import Flask, request, redirect, render_template
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['DEBUG'] = True
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://build-a-blog:root@localhost:3306/build-a-blog'
app.config['SQLALCHEMY_ECHO'] = True
db = SQLAlchemy(app)

header_form="""
<!DOCTYPE html>
<html>
<header>
    <title>Build-A-Blog</title>
    <a href="#Main blog page">Main Blog Page</a>
    <a href="#Add a new bolg post">Add A New Blog Post</a>
</header>
<body>
"""
footer_form="""
</body>
</html>
"""
blog_form="""
<form>
    <h1 style="text-align:center;">BUILD A BLOG</h1>
</form>

"""
new_blog="""
<form>
    <h1 style="text-align:center;">ADD A NEW BLOG ENTRY</h1>
    <b><label for="title-blog">Title for your new Blog:</label><br></b>
    <input type="text" name="title-blog" value='{tile-blog}' /><br>
    <b><label for="blog-details" style="text-align:center;">Your new Blog:</label><br></b>
    <textarea name="text">{details}</textarea><br>
    <input type="submit" value="ADD ENTRY" />
</form>
"""
@app.route('/')
def index():
    return redirect('/blog')

@app.route('/blog', methods=['POST','GET'])
def blog_page():    
    content = header_form+blog_form+footer_form
    return content
    
@app.route('/new-blog', methods=['POST','GET'])
def new_blog_page():
    content = header_form+new_blog+footer_form
    return content
    

app.run()
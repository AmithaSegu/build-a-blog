from flask import Flask, request, redirect, render_template
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['DEBUG'] = True
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://build-a-blog:root@localhost:3306/build-a-blog'
app.config['SQLALCHEMY_ECHO'] = True
db = SQLAlchemy(app)


class Blog(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(120))
    detail = db.Column(db.String(120))

    def __init__(self,title,detail):
        self.title=title
        self.detail=detail


@app.route('/')
def index():
    return redirect('/blog')

@app.route('/blog', methods=['POST','GET'])
def blog_page():
    if request.args:
        blog_id = request.args.get("id")
        blog = Blog.query.get(blog_id) 
        return render_template('blog_page.html',blog=blog)        
    else:
        blogs= Blog.query.all()
        return render_template("main_blog_page.html",blogs=blogs)
    
    return render_template('main_blog_page.html')

@app.route('/newpost', methods=['POST','GET'])
def new_blog_page():
    title_error=""
    detail_error=""
    if request.method=='GET':
        return render_template('new_post_page.html')

    if request.method=='POST':
        titles = request.form['title_blog']
        details = request.form['detail']
        
        if titles == "":
            title_error="PLEASE ENTER VALID TITLE"
            #return title_error
            return render_template('new_post_page.html',title_error=title_error,detail_error=detail_error)
        
        if details == "":
            detail_error="PLEASE ENTER A VALID DETAIL"
            #return detail_error
            return render_template('new_post_page.html',title_error=title_error,detail_error=detail_error)
        
        if title_error=="" and detail_error=="":
            title_detail = Blog(titles,details)
            db.session.add(title_detail)
            db.session.commit()
            return render_template("blog_page.html",titles=titles,details=details)

        return render_template('new_post_page.html',title_error=title_error,detail_error=detail_error)
    
if __name__ =='__main__':
    app.run()
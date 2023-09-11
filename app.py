from flask import Flask, request, render_template, redirect, url_for, flash
from flask_sqlalchemy import SQLAlchemy
from wtforms import TextAreaField
from wtforms.validators import DataRequired
from flask_wtf import FlaskForm
from flask import session

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+mysqlconnector://root:12345@127.0.0.1/blog_database'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

# Define the BlogUser model with the existing table
class BlogUser(db.Model):
    __tablename__ = 'blog_users'  # Set the table name to match the existing table
    user_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    first_name = db.Column(db.String(50))
    last_name = db.Column(db.String(50))
    mobile_number = db.Column(db.String(15))
    email_address = db.Column(db.String(100))
    date_of_birth = db.Column(db.Date)
    city = db.Column(db.String(50))
    country = db.Column(db.String(50))
    create_password = db.Column(db.String(100))
    confirm_password = db.Column(db.String(100))
    blogpost = db.Column(db.Text)


    

class BlogPostForm(FlaskForm):
    blogpost = TextAreaField('Blog Post', validators=[DataRequired()])

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/login", methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        # Retrieve data from the login form
        email = request.form['email']
        password = request.form['password']

        # Query the database to find a user with the provided email
        user = BlogUser.query.filter_by(email_address=email).first()

        if user:
            # If a user with the provided email exists, check the password
            if user.confirm_password == password:
                flash('Login successful.', 'success')
                return redirect(url_for('dashboard', email_address=email))
            else:
                flash('Invalid password. Please try again.', 'danger')
        else:
            flash('User not found. Please check your email or register.', 'danger')

    return render_template("login.html")



@app.route("/register", methods=['GET', 'POST'])
def register():
    form = BlogPostForm() 
    if request.method == 'POST':
        # Retrieve data from the HTML form using request.form
        first_name = request.form['first_name']
        last_name = request.form['last_name']
        mobile_number = request.form['mobile_number']
        email_address = request.form['email_address']
        date_of_birth = request.form['date_of_birth']
        city = request.form['city']
        country = request.form['country']
        create_password = request.form['create_password']
        confirm_password = request.form['confirm_password']

        # Perform database operations or user registration logic here
        new_user = BlogUser(
            first_name=first_name,
            last_name=last_name,
            mobile_number=mobile_number,
            email_address=email_address,
            date_of_birth=date_of_birth,
            city=city,
            country=country,
            create_password=create_password,
            confirm_password=confirm_password,
            blogpost=''  
        )

        # Add the new user to the database session and commit the changes
        db.session.add(new_user)
        db.session.commit()

        flash('Registration successful. You can now log in.', 'success')
        return redirect(url_for('login'))

    return render_template("register.html",form=form)

# @app.route("/main_page/<string:first_name>/<string:last_name>")
# def main_page(first_name, last_name):
#     # Query the database for all blog posts by users with the given first_name and last_name
#     all_blog_posts = BlogUser.query.filter_by(first_name=first_name, last_name=last_name).all()
#     return render_template("main_page.html", all_blog_posts=all_blog_posts)

@app.route("/main_page")
def main_page():
    # Query the database for all user data
    all_users = BlogUser.query.all()
    return render_template("main_page.html", all_users=all_users)



@app.route("/dashboard/<string:email_address>")
def dashboard(email_address):
    # Fetch a user's data from the existing 'blog_users' table
    user = BlogUser.query.filter_by(email_address=email_address).first()
 # You can modify this query as needed
    return render_template("dashboard.html",user=user)





@app.route("/create_blog/<int:user_id>/<string:first_name>/<string:email_address>", methods=['GET', 'POST'])
def create_blog(user_id, first_name,email_address):
    form = BlogPostForm()
   
    user = BlogUser.query.filter_by(user_id=user_id, first_name=first_name).first()
    
    if user is None:
        flash('User not found.', 'danger')
        return redirect(url_for('dashboard'))

    if form.validate_on_submit():
        
        # Update the user's blog post in the existing 'blog_users' table
        user.blogpost = form.blogpost.data
        
        db.session.commit()
        flash('Blog post created successfully.', 'success')
        return redirect(url_for('dashboard',email_address=email_address))
    
    # Pass the 'user' object to the template
    return render_template("create_blog.html", form=form, user=user)



@app.route("/about_us")
def about_us():
    return render_template("about_us.html")

if __name__ == '__main__':
    app.secret_key = '123@123'  # Add a secret key for session security
    app.run(debug=True)

from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Dummy data for blog posts
posts = [
    {
        'title': 'First Post',
        'content': 'This is the content of the first post.',
        'author': 'John Doe'
    },
    {
        'title': 'Second Post',
        'content': 'This is the content of the second post.',
        'author': 'Jane Doe'
    }
]

@app.route('/')
def home():
    return render_template('index.html', posts=posts)

@app.route('/post/<int:post_id>')
def post(post_id):
    post = posts[post_id - 1]  # Dummy logic to retrieve post by ID
    return render_template('post.html', post=post)

if __name__ == '__main__':
    app.run(debug=True)

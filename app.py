from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# A simple user database (replace with your actual user data)
users = {
    'username': 'password',
    'user2': 'password2'
}

@app.route('/')
def index():
    return render_template('instructions.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    print("enter login",request.method )
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
       
        if username in users and users[username] == password:
            return redirect(url_for('success'))
        else:
            return redirect(url_for('failure'))

    return render_template('login.html')
@app.route('/failure')
def failure():
    return 'Login failed!'

@app.route('/success')
def success():
    quiz_data = [
    {
        "question": "What is the capital of France?",
        "options": ["Berlin", "Madrid", "Paris", "Rome"],
        "correctAnswer": "Paris"
    },
    {
        "question": "What is the capital of France?",
        "options": ["Berlin", "Madrid", "Paris", "Rome"],
        "correctAnswer": "Paris"
    },
    {
        "question": "What is the capital of France?",
        "options": ["Berlin", "Madrid", "Paris", "Rome"],
        "correctAnswer": "Paris"
    },
    {
        "question": "What is the capital of France?",
        "options": ["Berlin", "Madrid", "Paris", "Rome"],
        "correctAnswer": "Paris"
    },
    {
        "question": "What is the capital of France?",
        "options": ["Berlin", "Madrid", "Paris", "Rome"],
        "correctAnswer": "Paris"
    },
    {
        "question": "What is the capital of France?",
        "options": ["Berlin", "Madrid", "Paris", "Rome"],
        "correctAnswer": "Paris"
    },
    {
        "question": "What is the capital of France?",
        "options": ["Berlin", "Madrid", "Paris", "Rome"],
        "correctAnswer": "Paris"
    }
    # Add more questions...
    ]
    questions_per_page = 4
    current_page = int(request.args.get('page', 1))  # Get the current page from the query parameter
    start_index = (current_page - 1) * questions_per_page
    end_index = start_index + questions_per_page
    page_quiz_data = quiz_data[start_index:end_index]

    return render_template('success.html', quiz_data=page_quiz_data, current_page=current_page,questions_per_page=questions_per_page)


if __name__ == '__main__':
    app.run(debug=True)
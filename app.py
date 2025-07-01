from flask import Flask, render_template, request, redirect, url_for, flash, jsonify

app = Flask(__name__) 
app.secret_key = 'your_secret_key'


@app.route('/')
def index():  
    return render_template('index.html')

@app.route('/test-css')
def test_css():
    return '''
    <link rel="stylesheet" href="/static/style.css">
    <h1 class="hero">If this is styled, CSS is working!</h1>
    '''

@app.route('/contact', methods=['POST'])
def contact(): 
    name = request.form['name'] 
    email = request.form['email'] 
    message = request.form['message'] 
    flash('Message sent successfully!', 'success') 
    return redirect(url_for('index'))
    
@app.route('/toggle-theme', methods=['POST'])
def toggle_theme(): 
    theme = request.json.get('theme') 
    response = jsonify({'theme': theme}) 
    response.set_cookie('theme', theme) 
    return response


if __name__ == '__main__': 
    app.run(debug=True)

from app import app

# first route
@app.route('/')
@app.route('/index')
def index():
    return 'Hello, World'
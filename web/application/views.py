from application import app


@app.route('/')
def top_page():
    hello = "TOP page Hello world !!"
    return hello


@app.route('/hello')
def hello():
    hello = "Hello world"
    return hello
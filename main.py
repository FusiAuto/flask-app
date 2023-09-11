from flask import Flask, send_file, url_for

app = Flask('recorder')


@app.route('/')
def home():
    path = 'render - start command.png'
    # return send_file(path)
    url = url_for('static', filename='render - start command.png')
    return url


app.run()
# http://127.0.0.1:5000/static/render%20-%20start%20command.png
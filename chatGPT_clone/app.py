from flask import Flask, render_template
import os

# Create the application object
app = Flask(__name__)

#API key
api_key = os.getenv('API_KEY')
print(api_key)

#Home route
@app.route('/')
def index():
    return render_template('index.html')


# Start the server with the 'run()' method
if __name__ == '__main__':
    app.run()
from flask import Flask 

# Create the application object
app = Flask(__name__)

#Home route
@app.route('/')
def index():
    return "Hello, World!"


# Start the server with the 'run()' method
if __name__ == '__main__':
    app.run()
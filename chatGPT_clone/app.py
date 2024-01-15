from flask import Flask, request, render_template
import os, json
from openai import OpenAI

client = OpenAI(api_key=os.getenv('API_KEY'))

# Create the application object
app = Flask(__name__)

#API key
api_key = os.getenv('API_KEY')
print(api_key)

#Home route
@app.route('/')
def index():
    return render_template('index.html')

#Get bot response
@app.route("/get")
def get_bot_response():
    userText = request.args.get('msg')
    response = client.completions.create(
        model="gpt-3.5-turbo-instruct",
        prompt=userText,
        max_tokens=1024,
        top_p=1,
        temperature=0.9
    )

    print(response.choices[0].text)
    answer = response.choices[0].text
    return str(answer)


# Start the server with the 'run()' method
if __name__ == '__main__':
    app.run()
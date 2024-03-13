from flask import Flask, request, render_template
import os
from openai import OpenAI

#Define details and config
app = Flask(__name__)
app.config.from_object('config.DevelopmentConfig')

#define the oai client
oai_api_key = app.config['API_KEY']
client = OpenAI(api_key=oai_api_key)

@app.route("/", methods = ["GET", "POST"])
def index():
    if request.method == 'POST':
        #code err
        code = request.form['code']
        error = request.form['error']

        #define the error explanation response
        explanation_prompt = (f"Explain the error in this code without fixing it: "
                             f"\n\n{code}\n\nError:\n\n{error}")
        explanation_response = client.completions.create(
            model="gpt-3.5-turbo-instruct",
            prompt=explanation_prompt,
            max_tokens=1024,
            top_p=1,
            temperature=0.9
        )
        explanation = explanation_response.choices[0].text

        #define the fix code response

        fixed_code_prompt = (f"Fix this code: \n\n{code}\n\nError:\n\n{error}"
                             f"\n Respond onlt with the fixed code")
        fixed_code_response = client.completions.create(
            model="gpt-3.5-turbo-instruct",
            prompt=fixed_code_prompt,
            max_tokens=1024,
            top_p=1,
            temperature=0.9
        )
        fixed_code = fixed_code_response.choices[0].text
        return render_template("index.html",
                           explanation=explanation,
                           fixed_code=fixed_code)
    return render_template("index.html")


if __name__ == "__main__":
    app.run()
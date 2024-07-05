import ollama
from flask import Flask, render_template, url_for, request, redirect
app = Flask(__name__)

@app.route('/', methods=['POST', 'GET'])
def index():
    if request.method=='POST':
        try:
            text_content = request.form["text"]
            LLM_chat(text=text_content)
        except:
            return "There was an issue while thinking for a response"
        return redirect('/')
    else:

        return render_template("index.html", messages=messages)

def LLM_chat(text):
    messages.append(
    {
        'role': 'user',
        'content': text,
    })

    response = ollama.chat(model='llama3:instruct', messages=messages)
    messages.append(response['message'])


if __name__=="__main__":
    messages = []

    app.run(debug=True)
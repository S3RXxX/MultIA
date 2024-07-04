import ollama
from flask import Flask, render_template, url_for, request, redirect
app = Flask(__name__)

@app.route('/', methods=['POST', 'GET'])
def index():
    if request.method=='POST':
        try:
            text_content = request.form["text"]
            # LLM_chat(text=text_content)
            messages.append({"role":"debugging", "content": text_content})
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

    return f" \n {response['message']['content']} \n"
    # print()
    # print(response['message']['content'])
    # print()

# @app.route('/get')
# def get_bot_response():    
#     userText = request.args.get('msg')  
#     response = LLM_chat(userText)  
#     return response

if __name__=="__main__":
    messages = []

    app.run(debug=True)
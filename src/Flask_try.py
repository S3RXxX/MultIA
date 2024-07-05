import ollama
from flask import Flask, render_template, url_for, request, redirect
app = Flask(__name__)
messages = []

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
        # afegir missatges a BD
        return render_template("index.html", messages=messages)

def LLM_chat(text):
    messages.append(
    {
        'role': 'user',
        'content': text,
    })

    response = ollama.chat(model='llama3:instruct', messages=messages)
    messages.append(response['message'])
    
######################### future funcs to interact w DB
def add_to_db(message):
    pass

def remove_from_db(message_id):
    pass

def edit_db(message_id, new_content):
    pass
############################################

@app.route('/delete/<int:n>')
def delete(n):
    n -= 1 ## loop.index starts w 1
    global messages
    try:
        #### borrar a BD
        messages = messages[:n]
        return redirect('/')
    except:
        return "There was an error while erasing your messages"

@app.route('/update/<int:n>', methods=['POST', 'GET'])
def update(n):
    global messages
    n -= 1
    print(n)
    if request.method == 'POST':
        new_content = request.form['text']
        try:
            role = messages[n]['role']
            messages[n] = {'role': role, 'content': new_content}
            return redirect('/')
        except:
            return "There was an error while erasing your messages"
    else:
        old_content = messages[n]['content']
        return render_template('update.html', n=n, old_content=old_content)
        




if __name__=="__main__":
    app.run(debug=True)
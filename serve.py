from flask import Flask, render_template, render_template_string
import os

app = Flask(__name__)

# File paths
URL_FILE = 'urls.txt'
PANDA_FILE = 'panda.txt'

def get_next_url():
    if not os.path.exists(URL_FILE):
        return None
    
    # Read all lines from the file
    with open(URL_FILE, 'r') as f:
        urls = f.readlines()
    
    if urls:
        # Remove the first URL and write back the remaining URLs
        next_url = urls[0].strip()
        with open(URL_FILE, 'w') as f:
            f.writelines(urls[1:])
        return next_url
    return None

def get_sad_panda():
    if os.path.exists(PANDA_FILE):
        with open(PANDA_FILE, 'r') as f:
            return f.read()
    return "No panda available."

@app.route('/')
def serve_next_url():
    next_url = get_next_url()
    if next_url:
        # Use the Bootstrap template
        return render_template('url.html', next_url=next_url)
    else:
        sad_panda = get_sad_panda()
        return render_template_string(f'<pre>{sad_panda}</pre><h1>No more URLs :(</h1>')

if __name__ == '__main__':
    app.run(debug=True,host='0.0.0.0')
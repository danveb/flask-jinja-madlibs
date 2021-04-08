# import Flask, request, render_template
# import DebugToolbarExtension
# import story from stories(.py) 

from flask import Flask, request, render_template 
from flask_debugtoolbar import DebugToolbarExtension
from stories import story 

app = Flask(__name__) 
app.config['SECRET_KEY'] = 'oh-so-secret' 
debug = DebugToolbarExtension(app) 

# route 
@app.route('/') 
# view function
def home_page():
    return render_template('home.html') 

# route
@app.route('/form')
# view function
def show_form():
    # story.prompts 
    generate_text = story.prompts 
    return render_template('form.html', prompts=generate_text) 

# route
@app.route('/story')
def show_story():
    # s.generate -> request.args (query string)
    story_text = story.generate(request.args)
    return render_template('story.html', text=story_text) 
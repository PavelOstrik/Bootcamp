from flask import Flask, render_template


app = Flask(__name__)


@app.route('/')
def main():
    return render_template('base.html', title='Главная страница')
                                          
@app.route('/projects')
def projects():    
    return render_template('projects.html', title='projects-tasks')   

@app.route('/about_me')
def about_me():    
    return render_template('about_me.html', title='about_me-tasks')                                       

if __name__ == '__main__':
    app.run()
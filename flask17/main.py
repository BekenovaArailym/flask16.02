from flask import Flask, render_template, redirect, request, url_for
import functions as f
import random

app = Flask(__name__, static_url_path='/static')

@app.route('/')
def index():
    profiles = f.get_profiles()
    return render_template("index.html", profiles=profiles)

@app.route("/details/<int:id>")
def details(id):
    profiles = f.get_profiles()
    for profile in profiles:
        if profile.get("id") == id:
            return render_template("details.html", profile=profile)
    return redirect("error")

@app.route('/update/<int:id>', methods=['GET', 'POST'])
def update(id):
    profiles = f.get_profiles()
    
    for profile in profiles:
        if profile.get("id") == id:
            if request.method == 'POST':
                
                profile['login'] = request.form['login']
                profile['cash'] = request.form['cash']
                profile['nationality'] = request.form['nationality']
                profile['country'] = request.form['country']
                profile['language'] = request.form['language']

                f.set_profiles(profiles)
                return redirect(url_for('details', id=id))
            else:
                return render_template("update.html", profile=profile)

    return redirect(url_for('error'))

@app.route('/delete/<int:id>', methods=['GET', 'POST'])
def delete(id):
    profiles = f.get_profiles()
    for profile in profiles:
        if profile.get("id") == id:
            if request.method == 'POST':

                profiles.remove(profile)
                f.set_profiles(profiles)
                return redirect(url_for('index'))
            else:
                return render_template("delete.html", profile=profile)
    return redirect("error")

@app.route('/create', methods=['GET', 'POST'])
def create():
    if request.method == 'POST':
        
        new_profile = {
            "id": random.randrange(99,99999),  
            'login': request.form['login'],
            'cash': request.form['cash'],
            'nationality': request.form['nationality'],
            'country': request.form['country'],
            'language': request.form['language']
        }

        
        profiles = f.get_profiles()
        profiles.append(new_profile)

        
        f.set_profiles(profiles)

       
        return redirect(url_for('index'))
    else:
        return render_template("create.html", id=None)  


@app.route("/error")
def error():
    return render_template("error.html")

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=81, debug=True)

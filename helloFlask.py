from flask import Flask, render_template

app = Flask(__name__)

heroes = [{
    'name': 'Luke Skywalker',
    'home': 'Tatooine',
    'weapon': 'Lightsaber'
},

    {
        'name': 'Chewbacca',
        'home': 'Kashyyyk',
        'weapon': 'Bowcaster'
    },

    {
        'name': 'Han Solo',
        'home': 'Corellia',
        'weapon': 'DL-44 Heavy Blaster Pistol'
    }]

@app.route('/')
def get_html():
    return render_template("index.html", heroes=heroes)


if __name__ == '__main__':
    app.run()

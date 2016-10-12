from flask import Flask, render_template

app = Flask(__name__)

heroes = [{
    'name': 'Luke Skywalker',
    'home': 'Tatooine',
    'weapon': 'Lightsaber',
    'url':'http://starwars.wikia.com/wiki/Luke_Skywalker',
    'img':'http://vignette3.wikia.nocookie.net/starwars/images/1/15/Luke_Skywalker_Ep_7_SWCT.png'
},

    {
        'name': 'Chewbacca',
        'home': 'Kashyyyk',
        'weapon': 'Bowcaster',
        'url':'http://starwars.wikia.com/wiki/Chewbacca',
        'img':'http://vignette4.wikia.nocookie.net/starwars/images/4/4f/Chewbacca-TFA.png'
    },

    {
        'name': 'Han Solo',
        'home': 'Corellia',
        'weapon': 'DL-44 Heavy Blaster Pistol',
        'url': 'http://starwars.wikia.com/wiki/Han_solo',
        'img':'http://vignette2.wikia.nocookie.net/starwars/images/e/e2/TFAHanSolo.png'

    }]

@app.route('/')
def get_html():
    return render_template("index.html", heroes=heroes)


if __name__ == '__main__':
    app.run()

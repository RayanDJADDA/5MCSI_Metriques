from flask import Flask, render_template_string, render_template, jsonify
from flask import render_template
from flask import json
from datetime import datetime
from urllib.request import urlopen
import sqlite3
                                                                                                                                       
app = Flask(__name__)  


@app.route("/contact/")
def MaPremiereAPI():
    return render_template('contact.html')

@app.route('/tawarano/')
def meteo():
    response = urlopen('https://samples.openweathermap.org/data/2.5/forecast?lat=0&lon=0&appid=xxx')
    raw_content = response.read()
    json_content = json.loads(raw_content.decode('utf-8'))
    results = []
    for list_element in json_content.get('list', []):
        dt_value = list_element.get('dt')
        temp_day_value = list_element.get('main', {}).get('temp') - 273.15 # Conversion de Kelvin en °c 
        results.append({'Jour': dt_value, 'temp': temp_day_value})
    return jsonify(results=results)

@app.route("/rapport/")
def mongraphique():
    return render_template("graphique.html")
  
@app.route('/histogramme/')
def mon_histogramme():
    return render_template('histogramme.html')

import requests
from flask import jsonify, render_template
from datetime import datetime

@app.route('/commits/')
def get_commits():
    # Appel à l'API GitHub pour obtenir les commits
    response = requests.get('https://api.github.com/repos/OpenRSI/5MCSI_Metriques/commits')
    commits = response.json()

    # Liste des minutes pour chaque commit
    commit_minutes = []

    # Extraire les minutes de chaque commit
    for commit in commits:
        commit_date = commit['commit']['author']['date']
        date_object = datetime.strptime(commit_date, '%Y-%m-%dT%H:%M:%SZ')
        commit_minutes.append(date_object.minute)

    # Préparer les données pour le graphique
    return jsonify(commit_minutes=commit_minutes)

@app.route('/commits-page/')
def commits_page():
    return render_template('commits.html')

                                                                                                                                       
@app.route('/')
def hello_world():
    return render_template('hello.html') #comm2
  
if __name__ == "__main__":
  app.run(debug=True)

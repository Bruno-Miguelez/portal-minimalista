from flask import Flask, render_template
from threading import Thread

app = Flask('')

@app.route('/')
def home():
  return "I'm alive"

@app.route('/portal-minimalista/')
def portal():
  return render_template('portal.html')

@app.route('/portal-minimalista/1-ano')
def portal1():
  return render_template('portal1.html')

@app.route('/portal-minimalista/2-ano')
def portal2():
  return render_template('portal2.html')

@app.route('/portal-minimalista/3-ano')
def portal3():
  return render_template('portal3.html')

def run():
  app.run(host='0.0.0.0',port=80)

def keep_alive():
    t = Thread(target=run)
    t.start()
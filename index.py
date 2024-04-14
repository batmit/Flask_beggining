from flask import Flask, render_template

app = Flask(__name__, template_folder='site')

@app.route('/index', methods=['GET', 'POST'])
def Home():
  return render_template('index.html')

if __name__ == '__main__':
  app.run(debug=True)

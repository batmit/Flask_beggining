from flask import Flask, render_template, request



app = Flask(__name__, template_folder='site')

@app.route('/index', methods=['GET', 'POST'])
def Home():
  return render_template('formulario.html')


@app.route('/processar', methods=['POST'])
def processar():
    banco_de_dados_ler = open("dados.txt", "r")
    sim = 0
    nome = request.form['nome']
    email = request.form['email']
    for c in banco_de_dados_ler.readlines():
       if c == f"{nome}-{email}\n":
          sim = 1
          break
    banco_de_dados_ler.close()
    banco_de_dados_escrever = open("dados.txt", 'a')
    if sim == 0:
       banco_de_dados_escrever.write(nome)
       banco_de_dados_escrever.write("-")
       banco_de_dados_escrever.write(email)
       banco_de_dados_escrever.write("\n")
    return render_template('index.html')


if __name__ == '__main__':
  app.run(debug=True)
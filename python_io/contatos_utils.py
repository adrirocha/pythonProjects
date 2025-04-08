import csv, pickle, json
from contato import Contato

def csv_para_contatos(caminho, encoding='latin_1'):
    contatos = []

    with open(caminho, encoding=encoding) as arquivo:
        leitor = csv.reader(arquivo)
        for linha in leitor:
            id, nome, email = linha
            contato = Contato(id, nome, email)
            contatos.append(contato)


    return contatos

def contatos_para_pickle(contatos, caminho):
    with open(caminho, mode='wb') as arquivo:   #wb indica que é pra abrir um arquivo binário(b) no modo de escrita(w)
        pickle.dump(contatos, arquivo) #Salvar dados em um arquivo/pasta
def pickle_para_contatos(caminho):
    with open(caminho, mode='rb') as arquivo: #rb indica que é pra ler(r) um arquibo binário(b)
        contatos = pickle.load(arquivo)
    return contatos


def contatos_para_json(contatos, caminho):
    with open(caminho, mode='w') as arquivo:
        json.dump(contatos, arquivo, default=_contato_para_json) #Salvar dados(contatos) em um arquivo
        # código omitido
        #json.dump(contatos, arquivo, default=lambda contato: contato.__dict__)

def _contato_para_json(contato):
    return contato.__dict__

def json_para_contatos(caminho):
    contatos = []
    with open(caminho) as arquivo:
       contatos_json = json.load(arquivo)

       for contato in contatos_json:
           c = Contato(**contato) #Desempacotar
           contatos.append(c)
    
    return contatos
           
        


from flask import Flask, render_template, request
import nltk
from nltk import CFG

cfg_grammar = CFG.fromstring("""
    S  -> 'd' A
    A  -> 'a' B | 'e' C | 'o' D
    B  -> 'd' 'u' | 'g' E | 'u' 'n'
    E  -> 'i' 'n' 'g'
    C  -> 'b' 'u'
    D  -> 'm' 'b' 'a'
""")

parser = nltk.ChartParser(cfg_grammar)

# Fungsi untuk memeriksa apakah kata diterima oleh grammar
def parse_word(word):
    try:
        # Memecah kata menjadi list karakter
        word = list(word)
        # Melakukan parsing
        parses = list(parser.parse(word))
        if parses:
            return True
        else:
            False
    except ValueError:
        False

app = Flask(__name__)

@app.route('/')
def home():
    word = request.args.get('word')
    isAccepted = False

    if word:
        isAccepted = parse_word(word=word)
         
    return render_template('index.html', word=word, isAccepted=isAccepted)

if __name__ == '__main__':
    app.run(debug=True)

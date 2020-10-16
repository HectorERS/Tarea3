from Crypto.Cipher import CAST
from Crypto import Random
from flask import Flask, render_template


#la llave  tiene un tamaño maximo de 16 caracteres
key = b'1234567890123456'
cipher = CAST.new(key, CAST.MODE_CBC)
plaintext = b'sona si latine loqueris '
msg = cipher.encrypt(plaintext)


app= Flask(__name__)


@app.route('/')

def index():
    id = msg
    return render_template("home.html", id=msg)

if __name__ == "__main__":
    app.run()


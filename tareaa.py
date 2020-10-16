from Crypto.Cipher import CAST
from Crypto import Random
from flask import Flask, render_template


#la llave  tiene un tamaño maximo de 16 caracteres
key = b'1234567890123456'
iv = Random.new().read(CAST.block_size)
cipher = CAST.new(key, CAST.MODE_OPENPGP, iv)
plaintext = b'R1R1R1R1R1R1R1R1R1R1R2R3'
msg = cipher.encrypt(plaintext)

print (cipher.encrypt(plaintext))

app= Flask(__name__)


@app.route('/')

def index():
    id = msg
    return render_template("home.html", id=msg)



if __name__ == "__main__":
    app.run()

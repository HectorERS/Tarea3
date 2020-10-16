from Crypto.Cipher import CAST
from Crypto import Random
from flask import Flask, render_template
from base64 import b64encode

#i = rondas realizadas, para i<10, 12 rondas, i>10 son 16 rondas
i=0
#la llave  tiene un tamaño maximo de 16 caracteres y minimo de 5 caracteres
key = b'12345'
iv = Random.new().read(CAST.block_size)
cipher = CAST.new(key, CAST.MODE_CFB)
msg= b'mensaje a descifrar con el algoritmo CAST128'
if len(key)<10:
    while i != 12:
        msg = cipher.encrypt(msg)
        i=i+1
if len(key)>10:
    while i != 16:
        msg = cipher.encrypt(msg)
        i=i+1
msg= b64encode(msg).decode('utf-8')
print(len(key))
print(i)
app= Flask(__name__)


@app.route('/')

def index():
    id = msg
    return render_template("home.html", id=msg)


if __name__ == "__main__":
    app.run()

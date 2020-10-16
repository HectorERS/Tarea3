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

eiv = msg[:CAST.block_size+2]
ciphertext = msg[CAST.block_size+2:]
cipher = CAST.new(key, CAST.MODE_OPENPGP, eiv)

print (cipher.decrypt(ciphertext))


app= Flask(__name__)


@app.route('/')
def index():
    try:
        id= cipher.decrypt(ciphertext)

        return f"""<html>
        <body bgcolor="blue" ><body>
        <head>
           <title>Hola Mundo</title>
           <p>Este sitio contiene un mensaje secreto</p>
           <div class="algorithm" id={id}></div>
        </head>
        </html>"""
    except Excpetion as e:
        return str(e)



if __name__ == "__main__":
    app.run()

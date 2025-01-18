from flask import Flask, request, render_template

app = Flask(__name__)

def caesar_cipher_encrypt(text, shift):
    """
    Mengenkripsi teks menggunakan Caesar Cipher.

    :param text: Teks yang akan dienkripsi
    :param shift: Jumlah pergeseran huruf
    :return: Teks terenkripsi
    """
    encrypted_text = ""
    for char in text:
        if char.isalpha():
            # Memeriksa apakah karakter adalah huruf
            start = ord('A') if char.isupper() else ord('a')
            encrypted_text += chr((ord(char) - start + shift) % 26 + start)
        else:
            # Jika bukan huruf, tambahkan karakter apa adanya
            encrypted_text += char
    return encrypted_text

def caesar_cipher_decrypt(text, shift):
    """
    Mendekripsi teks yang dienkripsi dengan Caesar Cipher.

    :param text: Teks yang akan didekripsi
    :param shift: Jumlah pergeseran huruf (sama dengan yang digunakan saat enkripsi)
    :return: Teks asli
    """
    return caesar_cipher_encrypt(text, -shift)

@app.route("/", methods=["GET", "POST"])
def index():
    result = ""
    if request.method == "POST":
        text = request.form.get("text")
        shift = int(request.form.get("shift"))
        action = request.form.get("action")

        if action == "encrypt":
            result = caesar_cipher_encrypt(text, shift)
        elif action == "decrypt":
            result = caesar_cipher_decrypt(text, shift)

    return render_template("index.html", result=result)

if __name__ == "__main__":
    app.run(debug=True)

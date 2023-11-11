from Crypto.Cipher import DES
from Crypto.Util.Padding import pad, unpad
from PIL import Image
import cv2
import numpy as np


def encrypt_image(image_path, output_path, key, num_iterations=16):
    # Carregando imagem da Lenna e convertendo para array.
    img = Image.open(image_path)
    img_array = np.array(img)

    # Convertendo array para bytes.
    img_bytes = img_array.tobytes()

    # Criando um Objeto DES com a chave passada por argumento.
    cipher = DES.new(key, DES.MODE_ECB)

    # Iterando conforme o número de iterações passadas por argumento.
    for _ in range(num_iterations):
        img_bytes = cipher.encrypt(img_bytes)

    # Convertendo bytes para array novamente.
    img_array = np.frombuffer(img_bytes, dtype=np.uint8).reshape(img_array.shape)

    # Criando uma nova imagem a partir do array criptografado
    encrypted_img = Image.fromarray(img_array)

    # Salvando Imagem criptografada
    encrypted_img.save(output_path)


if __name__ == "__main__":
    # Caminho da imagem de Lenna
    image_path = "img/Lenna.png"

    # Parte (a): Usando DES completo com chave manual
    key_a = b"\x01\x23\x45\x67\x89\xAB\xCD\xEF"
    encrypt_image(image_path, "img_encrypted/encrypted_Lenna_a.png", key_a)

    # Parte (b): Usando DES sem nenhuma iteração com chave manual
    key_b = b"\x01\x23\x45\x67\x89\xAB\xCD\xEF"
    encrypt_image(
        image_path, "img_encrypted/encrypted_Lenna_b.png", key_b, num_iterations=0
    )

    # Parte (c): Usando DES com uma iteração com chave manual
    key_c = b"\x01\x23\x45\x67\x89\xAB\xCD\xEF"
    encrypt_image(
        image_path, "img_encrypted/encrypted_Lenna_c.png", key_c, num_iterations=1
    )

    # Parte (d): Usando DES com todas as chaves iguais a zero
    key_d = bytes([0] * 8)
    encrypt_image(image_path, "img_encrypted/encrypted_Lenna_d.png", key_d)

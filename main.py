#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys
import json
import base64
import hashlib
import os
from datetime import datetime
from urllib.request import urlopen
from Crypto.Cipher import AES
from Crypto.Util.Padding import unpad

from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.uix.scrollview import ScrollView

URL = "https://raw.githubusercontent.com/Fenix1998x/GEN-SERVIDORES-NUEVO-24-08-2027/refs/heads/main/Fenix"
CRYPTO_PASSWORD = "🔥🔥🔥vpnfenix⭐️⭐️⭐️"
ACCESS_PASSWORD = "JT"
NAJU = "FenxM22_07!89Dev" 
HEADER = b"WakkoDev"
SALT_LEN = 8

KEY_MAP = {
    "p0PgL3l0d89mnssz7ImPJA==": "sName",
    "66P9ZUEM1ju4WGhv856BSg==": "sInfo",
    "ACqWMY4zuZWzSEs8cZMXIw==": "sFlag",
    "U7V8DoP4cYkXJjCnpqW6nQ==": "ServerIP",
    "p9ZPlMv9V7gDszRoUaNaJw==": "ServerPort",
    "maGFM5lWW4YSDpfPQBmdRA==": "ServerSSL",
    "SbDP19AbQur0YtkkyRlVMA==": "ProxyIp",
    "vXfVafVdyaCRTDj6uBT6lg==": "ProxyPort",
    "PFFSWRJKZmOcNLTZxFwgjQ==": "Payload",
    "tmSbWiCK1hvytJ9f3gflkQ==": "SNI",
    "mtw364P3ZslP2CZYuHTCHQ==": "ServerUser",
    "Fo3TT4oONvv69IQIMg1aLg==": "ServerPass",
    "UxdyIntdYykCdV76crKnwg==": "Slowchave",
    "l7MIgkbuXMmGaaQGd54F2w==": "Nameserver",
    "QSln2zKCBJvqH9qV4M0ifg==": "Slowdns",
    "ITkWvEHp29BmMaLMEGUFcw==": "udpserver",
    "2kDKELRmSE143VdcX3FPzw==": "udpport",
    "iW1aO5DgThVAeo23xTsXSw==": "udpObfs",
    "b3MPypEFR83rzFKUa4UbCw==": "udpauth",
    "MkRXl4D9vpREVCJ0w4qrgg==": "udpdown",
    "B5jcTSGuJUFbTtH5O1IaBg==": "udpup",
    "asmRO4zXsRjhDYX42dbNuw==": "udpbuffer",
    "oAqgFKE3WywLRvSvKffLOA==": "V2rayAddress",
    "b6stZNVaFUjLCw88dn03Ng==": "V2rayPort",
    "BWTPMwR0iRu1N9twHCpbAg==": "V2rayHost",
    "EtNSBhechjWxm2t50NyB9Q==": "v2rayid",
    "aH2nzD4eDLxPSxIAlVivdg==": "v2raypath",
    "W4CbS1nMWo6Y2noeUFHmXQ==": "v2rayJson",
    "MIgkNbuX29MmGatZNVaFUj==": "OtrasConfigs",
}

def evp_bytes_to_key(password, salt, key_len, iv_len):
    total = key_len + iv_len
    derived = b""
    prev = b""
    while len(derived) < total:
        md5 = hashlib.md5()
        md5.update(prev)
        md5.update(password)
        md5.update(salt)
        prev = md5.digest()
        derived += prev
    return derived[:total]

def decrypt_wakko(b64_text, password):
    raw = base64.b64decode(b64_text)
    if not raw.startswith(HEADER):
        raise ValueError("Encabezado incorrecto")
    salt = raw[len(HEADER):len(HEADER) + SALT_LEN]
    ciphertext = raw[len(HEADER) + SALT_LEN:]
    key_iv = evp_bytes_to_key(password.encode("utf-8"), salt, 32, 16)
    key, iv = key_iv[:32], key_iv[32:48]
    cipher = AES.new(key, AES.MODE_CBC, iv)
    padded = cipher.decrypt(ciphertext)
    plain = unpad(padded, 16)
    return plain.decode("utf-8")

def aesed_decrypt(encrypted_text, secret):
    if not encrypted_text or len(encrypted_text) < 24:
        return None
    try:
        missing = -len(encrypted_text) % 4
        raw = base64.urlsafe_b64decode(encrypted_text + '=' * missing)
    except Exception:
        return None
    if len(raw) <= 16:
        return None
    iv = raw[:16]
    ciphertext = raw[16:]
    secret_bytes = secret.encode("utf-8")
    key = bytearray(32)
    copy_len = min(len(secret_bytes), 32)
    key[:copy_len] = secret_bytes[:copy_len]
    key = bytes(key)
    try:
        cipher = AES.new(key, AES.MODE_CBC, iv)
        padded = cipher.decrypt(ciphertext)
        plain = unpad(padded, 16)
        return plain.decode("utf-8")
    except Exception:
        return None

def encoder_cesar(txt, d):
    result = []
    for ch in txt:
        if ch.isalpha():
            base = ord('A') if ch.isupper() else ord('a')
            result.append(chr((ord(ch) + d - base) % 26 + base))
        else:
            result.append(ch)
    return ''.join(result)

def decoder_cesar(texto, d):
    return encoder_cesar(texto, 26 - d)

def decrypt_value(val, secret):
    paso1 = aesed_decrypt(val, secret)
    if paso1 is None:
        return val
    return decoder_cesar(paso1, 5)

def remap_keys(obj):
    if isinstance(obj, dict):
        new_dict = {}
        for k, v in obj.items():
            new_key = KEY_MAP.get(k, k)
            new_dict[new_key] = remap_keys(v)
        return new_dict
    elif isinstance(obj, list):
        return [remap_keys(item) for item in obj]
    else:
        return obj

class FenixApp(App):
    def build(self):
        self.title = "Fenix Decryptor"
        self.layout = BoxLayout(orientation='vertical', padding=15, spacing=10)
        
        self.layout.add_widget(Label(text='🔐 Fenix Decryptor', font_size=24, size_hint_y=0.15))
        
        self.pw_input = TextInput(password=True, hint_text='Escribe la contraseña...', size_hint_y=0.15)
        self.layout.add_widget(self.pw_input)
        
        self.btn = Button(text='✅ Descifrar y Guardar', background_color=(0.2, 0.7, 0.3, 1), size_hint_y=0.15)
        self.btn.bind(on_press=self.procesar)
        self.layout.add_widget(self.btn)
        
        self.resultado = Label(text='Esperando contraseña...', font_size=14, text_size=(350, None))
        self.scroll = ScrollView(size_hint_y=0.5)
        self.scroll.add_widget(self.resultado)
        self.layout.add_widget(self.scroll)
        
        return self.layout

    def procesar(self, instance):
        entrada_pw = self.pw_input.text.strip()
        if entrada_pw != ACCESS_PASSWORD:
            self.resultado.text = "❌ Contraseña incorrecta"
            return

        try:
            self.resultado.text = "🔄 Descargando datos..."
            with urlopen(URL) as resp:
                b64_data = resp.read().decode("utf-8").strip()

            self.resultado.text = "🔓 Descifrando datos..."
            texto_descifrado = decrypt_wakko(b64_data, CRYPTO_PASSWORD)
            data = json.loads(texto_descifrado)

            if "Servers" in data and len(data["Servers"]) > 0:
                for server in data["Servers"]:
                    for key in list(server.keys()):
                        valor = server[key]
                        if isinstance(valor, str) and valor:
                            server[key] = decrypt_value(valor, NAJU)

            data = remap_keys(data)

            try:
                from kivy.utils import platform
                if platform == 'android':
                    from android.storage import primary_external_storage_path
                    DOWNLOAD_DIR = primary_external_storage_path()
                    ruta_salida = os.path.join(DOWNLOAD_DIR, "Download", "fenix_decrypted.json")
                    os.makedirs(os.path.dirname(ruta_salida), exist_ok=True)
                else:
                    DOWNLOAD_DIR = os.path.expanduser("~")
                    ruta_salida = os.path.join(DOWNLOAD_DIR, "fenix_decrypted.json")
            except:
                ruta_salida = "fenix_decrypted.json"

            with open(ruta_salida, "w", encoding="utf-8") as f:
                json.dump(data, f, indent=2, ensure_ascii=False)

            self.resultado.text = f"""✅ ¡Éxito! 🎉

Guardado en:
{ruta_salida}
"""
        except Exception as e:
            self.resultado.text = f"❌ Error: {str(e)}"

if __name__ == "__main__":
    FenixApp().run()

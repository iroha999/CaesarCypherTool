import flet as ft

def caesar_encrypt(text, shift):
    result = ""
    for char in text:
        if char.isalpha():
            offset = ord('a') if char.islower() else ord('A')
            result += chr((ord(char) - offset + shift) %  26 + offset)
        else:
            result += char
    return result

def caesar_decrypt(text, shift):
    return caesar_encrypt(text, -shift)

def main(page: ft.Page):
    page.title = "シーザー暗号ツール"
    page.vertical_alignment = ft.MainAxisAlignment.START

    title = ft.Text(value="Caesar Cipher Tool", italic=True, selectable=False, style='displayLarge')
    page.add(title)

    txt_input = ft.TextField(hint_text="変換する値を入力してください", width=300)
    txt_shift_encrypt = ft.TextField(hint_text="シフト数を入力してください", width=300)
    txt_shift_decrypt = ft.TextField(hint_text="シフト数を入力してください", width=300)
    txt_output_encrypted = ft.TextField(hint_text="暗号文:", width=300)
    txt_output_decrypted = ft.TextField(hint_text="平文:", width=300)
    
    def process_encrypt(e):
        text = txt_input.value
        shift = int(txt_shift_encrypt.value)
        encrypted = caesar_encrypt(text, shift)
        txt_output_encrypted.value = encrypted
        page.update()

    def process_decrypt(e):
        text = txt_input.value
        shift = int(txt_shift_decrypt.value)
        decrypted = caesar_decrypt(text, shift)
        txt_output_decrypted.value = decrypted
        page.update()

    btn_encrypt = ft.ElevatedButton("Encrypt", on_click=process_encrypt)
    btn_decrypt = ft.ElevatedButton("Decrypt", on_click=process_decrypt)

    page.add(
        ft.Column(
            [
                txt_input,
                txt_shift_encrypt,
                btn_encrypt,
                txt_output_encrypted,
                txt_shift_decrypt,
                btn_decrypt,
                txt_output_decrypted
            ],
            alignment=ft.MainAxisAlignment.CENTER,
        )
    )

ft.app(target=main)
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.label import Label
from urllib.request import urlopen

class FenixApp(App):
    def build(self):
        layout = BoxLayout(orientation='vertical', padding=30, spacing=15)
        
        self.status_label = Label(text="=== Fenix APK ===", font_size=20)
        layout.add_widget(self.status_label)
        
        self.pass_input = TextInput(hint_text="Escribe la contraseña aquí", password=True, multiline=False)
        layout.add_widget(self.pass_input)
        
        btn = Button(text="INGRESAR Y DESCIFRAR", background_color=(0.1, 0.7, 0.1, 1), font_size=18)
        btn.bind(on_press=self.ejecutar)
        layout.add_widget(btn)
        
        return layout

    def ejecutar(self, instance):
        if self.pass_input.text == "JT":
            self.status_label.text = "Clave correcta. Descargando servidores..."
            try:
                url = "https://githubusercontent.com"
                response = urlopen(url)
                self.status_label.text = "¡Logrado! Servidores descargados con éxito."
            except Exception as e:
                self.status_label.text = "Error al conectar con internet."
        else:
            self.status_label.text = "Contraseña Incorrecta. Intenta de nuevo."

if __name__ == '__main__':
    FenixApp().run()

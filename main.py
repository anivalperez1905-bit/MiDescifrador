from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.label import Label
from urllib.request import urlopen

class FenixApp(App):
    def build(self):
        layout = BoxLayout(orientation='vertical')

        self.status_label = Label(text="=== Fenix App ===")
        layout.add_widget(self.status_label)

        self.pass_input = TextInput(hint_text="Escribe la clave aquí")
        layout.add_widget(self.pass_input)

        btn = Button(text="INGRESAR Y DESCIFRAR")
        btn.bind(on_press=self.ejecutar)
        layout.add_widget(btn)

        return layout

    def ejecutar(self, instance):
        if self.pass_input.text == "JT":
            self.status_label.text = "Clave correcta"
            try:
                url = "https://githubusercontent.com"
                response = urlopen(url)
                self.status_label.text = "¡Logrado con éxito!"
            except Exception as e:
                self.status_label.text = "Error al conectar"
        else:
            self.status_label.text = "Clave incorrecta"

if __name__ == "__main__":
    FenixApp().run()

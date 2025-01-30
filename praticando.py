from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.boxlayout import BoxLayout
from datetime import datetime

class IdadeApp(App):

    def build(self):
        self.layout = BoxLayout(orientation='vertical')

        self.label = Label(text="Informe seu nome:")
        self.layout.add_widget(self.label)

        self.nome_input = TextInput(multiline=False)
        self.layout.add_widget(self.nome_input)

        self.label_ano = Label(text="Informe seu ano de nascimento:")
        self.layout.add_widget(self.label_ano)

        self.ano_input = TextInput(multiline=False, input_filter='int')
        self.layout.add_widget(self.ano_input)

        self.result_label = Label(text="")
        self.layout.add_widget(self.result_label)

        self.submit_button = Button(text="Calcular Idade")
        self.submit_button.bind(on_press=self.calcular_idade)
        self.layout.add_widget(self.submit_button)

        return self.layout

    def calcular_idade(self, instance):
        nome = self.nome_input.text
        ano_nascimento = int(self.ano_input.text)
        
        ano_atual = datetime.now().year
        idade = ano_atual - ano_nascimento

        resultado = f'Olá {nome}, neste ano de {ano_atual} você completa {idade} anos de idade.\n'

        if 30 <= idade < 65:
            resultado += f'{nome} está no momento maduro e no auge da sua vida.'
        elif 18 <= idade < 30:
            resultado += f'{nome} está na fase jovem da vida.'
        elif idade >= 65:
            resultado += f'{nome} é uma pessoa idosa.'
        else:
            resultado += f'{nome} é menor de idade!'

        self.result_label.text = resultado


if __name__ == '__main__':
    IdadeApp().run()


'''from time import sleep
import tkinter as tk
from tkinter import messagebox
from datetime import datetime

messagebox.showinfo("Informe!", "A seguir informe seu nome e ano de nascimento e verifique em qual faixa etária você se encontra!")

nome = input('Informe seu nome: ')
ano_nascimento = int(input('Infome o ano do seu nascimento: '))

ano_atual = datetime.now().year

idade = ano_atual - ano_nascimento

print(f'Olá {nome}, neste ano de {ano_atual} você completa {idade} anos de idade.')

if idade >= 30 and idade < 65:
    print(f'{nome} esta no momento maduro e no auge da sua vida')
if idade < 30 and idade >= 18:
    print(f'{nome} está na fase jovem da vida')
if idade >= 65:
    print(f'{nome} é uma pessoa idosa.')
elif idade < 18:
    print(f'{nome} é menor de idade!')
sleep(30)'''
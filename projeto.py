import base64
import PySimpleGUI as sg
import perguntas
import sys

pergunta_atual = 0

#função pra retornar a imagem no formato base64
def retornarBase64(image):
    with open(f"imagens\\{image}.png", "rb") as image_file:
        return base64.b64encode(image_file.read())

# Define uma cor e texto
pontos = 0
sg.theme('DarkBlue16')
sizetxt = 65
pergunta = perguntas.perguntas

# Botão de próximo e sair:
proximo = retornarBase64('prox')
sair = retornarBase64('cancel')

# Tudo que tiver dentro da janela

layout =[   
            [[sg.Text(perguntas.perguntas[pergunta_atual]['pergunta'], font=('Consolas', 20), text_color='white', size=(sizetxt, 5)), sg.Text(f'Pergunta de número {pergunta_atual+1} / 30', text_color='white')]],
            [sg.Canvas(size=(1100,2), background_color='white')],
            [sg.Canvas(size=(0,10))],
            [sg.Radio(f"A) {perguntas.perguntas[pergunta_atual]['opcoes'][0]}", font=('Calibri', 15), group_id='fala', size=(sizetxt, None))],
            [sg.Radio(f"B) {perguntas.perguntas[pergunta_atual]['opcoes'][1]}", font=('Calibri', 15), group_id='fala', size=(sizetxt, None))],
            [sg.Radio(f"C) {perguntas.perguntas[pergunta_atual]['opcoes'][2]}", font=('Calibri', 15), group_id='fala', size=(sizetxt, None))],
            [sg.Radio(f"D) {perguntas.perguntas[pergunta_atual]['opcoes'][3]}", font=('Calibri', 15), group_id='fala', size=(sizetxt, None))],
            [sg.Canvas(size=(0,70))],
            [[sg.Button('', image_data=proximo, button_color=(sg.theme_background_color(),sg.theme_background_color()), border_width=0, key='Proximo'),
            sg.Canvas(size=(900,2)), sg.Button('', image_data=sair, button_color=(sg.theme_background_color(),sg.theme_background_color()), border_width=0, key='Cancelar')]]
        ]

# Cria a Janela
janela = sg.Window('Prova do DETRAN', layout, size=(1280,500),finalize=True)

# Loop pra processar os "eventos" e pegar os valores inseridos na janela
while True:
    event, values = janela.read()
    #se o usuário fechar ou cancelar
    if event == sg.WIN_CLOSED or event == 'Cancelar':
        sys.exit()
        break


    if event == 'Proximo':

        value_insert = any(values.values())

        if value_insert:
            for i in values:
                if values[i]:
                    if pergunta[pergunta_atual]['resp'] == pergunta[pergunta_atual]['opcoes'][i]:
                        pontos+= 1
        else:
            sg.popup('Escolha ao menos uma alternativa!')
            continue

        pergunta_atual += 1

        if pergunta_atual == len(perguntas.perguntas):
            sg.popup('Você chegou no fim do teste. Carregando resultados...', font=('Calibri', 15))
            break


        layout2 =[
            [[sg.Text(perguntas.perguntas[pergunta_atual]['pergunta'], font=('Consolas', 20), text_color='white', size=(sizetxt, 5)), sg.Text(f'Pergunta de número {pergunta_atual+1} / 30', text_color='white')]],
            [sg.Canvas(size=(1100,2), background_color='white')],
            [sg.Canvas(size=(0,10))],
            [sg.Radio(f"A) {perguntas.perguntas[pergunta_atual]['opcoes'][0]}", font=('Calibri', 15), group_id='fala', size=(sizetxt, None))],
            [sg.Radio(f"B) {perguntas.perguntas[pergunta_atual]['opcoes'][1]}", font=('Calibri', 15), group_id='fala', size=(sizetxt, None))],
            [sg.Radio(f"C) {perguntas.perguntas[pergunta_atual]['opcoes'][2]}", font=('Calibri', 15), group_id='fala', size=(sizetxt, None))],
            [sg.Radio(f"D) {perguntas.perguntas[pergunta_atual]['opcoes'][3]}", font=('Calibri', 15), group_id='fala', size=(sizetxt, None))],
            [sg.Canvas(size=(0,70))],
            [[sg.Button('', image_data=proximo, button_color=(sg.theme_background_color(),sg.theme_background_color()), border_width=0, key='Proximo'),
            sg.Canvas(size=(900,2)), sg.Button('', image_data=sair, button_color=(sg.theme_background_color(),sg.theme_background_color()), border_width=0, key='Cancelar')]]
            ]
        janela.close()
        janela = sg.Window('Prova do DETRAN', layout2, size=(1280,500))
        
        continue

janela.close()

if pontos > 20:
    layoutResultado = [
        [[sg.Canvas(size=(100,2), background_color=None), sg.Text('Parabéns! Você foi aprovado', font=('Consolas', 20), text_color='white', size=(sizetxt, 5))]],
        [[sg.Canvas(size=(170,2), background_color=None), sg.Text(f'Sua pontuação foi de: ', font=('Consolas', 20), text_color='white')]],
        [[sg.Canvas(size=(220,2), background_color=None), sg.Text(f'{int(pontos/30*100)}%', font=('Consolas', 50), text_color='green')]],
        [sg.Canvas(size=(0,80), background_color=None)],
        [[sg.Canvas(size=(230,2)), sg.Button('', image_data=sair, button_color=(sg.theme_background_color(),sg.theme_background_color()), border_width=0, key='Cancelar')]]
]
else:
    layoutResultado = [
        [[sg.Canvas(size=(100,2), background_color=None), sg.Text('Infelizmente você foi reprovado!', font=('Consolas', 20), text_color='white', size=(sizetxt, 5))]],
        [[sg.Canvas(size=(170,2), background_color=None), sg.Text(f'Sua pontuação foi de: ', font=('Consolas', 20), text_color='white')]],
        [[sg.Canvas(size=(220,2), background_color=None), sg.Text(f'{int(pontos/30*100)}%', font=('Consolas', 50), text_color='red')]],
        [sg.Canvas(size=(0,80), background_color=None)],
        [[sg.Canvas(size=(230,2)), sg.Button('', image_data=sair, button_color=(sg.theme_background_color(),sg.theme_background_color()), border_width=0, key='Cancelar')]]
]

janela2 = sg.Window('RESULTADO', layoutResultado, size=(700,500))

while True:
    event, values = janela2.read()
    #se o usuário fechar ou cancelar
    if event == sg.WIN_CLOSED or event == 'Cancelar':
        break
janela2.close()

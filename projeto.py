import PySimpleGUI as sg
import perguntas


# Define uma cor
pontos = 0
sg.theme('DarkAmber')
sizetxt = 50

pergunta_atual = 0
# Tudo que tiver dentro da janela
layout =[   
            [sg.Text(perguntas.perguntas[pergunta_atual]['pergunta'],   font='Consolas', text_color='white', size=(50, None))],
            [sg.Radio(f"A) {perguntas.perguntas[pergunta_atual]['opcoes'][0]}", group_id='fala', size=(sizetxt, None))],
            [sg.Radio(f"B) {perguntas.perguntas[pergunta_atual]['opcoes'][1]}", group_id='fala', size=(sizetxt, None))],
            [sg.Radio(f"C) {perguntas.perguntas[pergunta_atual]['opcoes'][2]}", group_id='fala', size=(sizetxt, None))],
            [sg.Radio(f"D) {perguntas.perguntas[pergunta_atual]['opcoes'][3]}", group_id='fala', size=(sizetxt, None))],
            [sg.Text('', key='msg')],
            [sg.Button('Proximo'), sg.Button('Cancelar')]
        ]

# Cria a Janela
janela = sg.Window('Janela teste', layout)

# Loop pra processar os "eventos" e pegar os valores inseridos na janela
while True:
    event, values = janela.read()
    #se o usuário fechar ou cancelar
    if event == sg.WIN_CLOSED or event == 'Cancelar':
        break

    if event == 'Proximo':
        if values[0]:
            if perguntas.perguntas[pergunta_atual]['resp'] != perguntas.perguntas[pergunta_atual]['opcoes'][0]:
                sg.popup(f'Resposta incorreta. A resposta correta era: {perguntas.perguntas[pergunta_atual]["resp"]}')
            else:
                sg.popup('Resposta correta!')
                pontos += 1

            
        elif values[1]:
            if perguntas.perguntas[pergunta_atual]['resp'] != perguntas.perguntas[pergunta_atual]['opcoes'][1]:
                sg.popup(f'Resposta incorreta. A resposta correta era: {perguntas.perguntas[pergunta_atual]["resp"]}')
            else:
                sg.popup('Resposta correta!')
                pontos += 1

        elif values[2]:
            if perguntas.perguntas[pergunta_atual]['resp'] != perguntas.perguntas[pergunta_atual]['opcoes'][2]:
                sg.popup(f'Resposta incorreta. A resposta correta era: {perguntas.perguntas[pergunta_atual]["resp"]}')
            else:
                sg.popup('Resposta correta!')
                pontos += 1
        
        elif values[3]:
            if perguntas.perguntas[pergunta_atual]['resp'] != perguntas.perguntas[pergunta_atual]['opcoes'][3]:
                sg.popup(f'Resposta incorreta. A resposta correta era: {perguntas.perguntas[pergunta_atual]["resp"]}')
            else:
                sg.popup('Resposta correta!')
                pontos += 1

        pergunta_atual += 1

        if pergunta_atual == len(perguntas.perguntas):
                sg.popup('Fim do jogo!')
                break

        layout =[   
            [sg.Text(perguntas.perguntas[pergunta_atual]['pergunta'],   font='Consolas', text_color='white', size=(50, None))],
            [sg.Radio(f"A) {perguntas.perguntas[pergunta_atual]['opcoes'][0]}", group_id='fala', size=(sizetxt, None))],
            [sg.Radio(f"B) {perguntas.perguntas[pergunta_atual]['opcoes'][1]}", group_id='fala', size=(sizetxt, None))],
            [sg.Radio(f"C) {perguntas.perguntas[pergunta_atual]['opcoes'][2]}", group_id='fala', size=(sizetxt, None))],
            [sg.Radio(f"D) {perguntas.perguntas[pergunta_atual]['opcoes'][3]}", group_id='fala', size=(sizetxt, None))],
            [sg.Text('', key='msg')],
            [sg.Button('Proximo'), sg.Button('Cancelar')]
        ]
        janela.close()
        janela = sg.Window('Janela teste', layout)
        
        continue

janela.close()
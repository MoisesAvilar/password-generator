import PySimpleGUI as gui
from functions.save_password import save_password


def save_password_window(password):
    layout = [
        [gui.Text('Nome do site ou usuário', size=20),
            gui.Input(size=10, key='conta')],
        [gui.Text(size=30, key='dialog', justification='c', font=20)],
        [gui.Text(size=10), gui.Button('Salvar', size=10, font=20),
            gui.Text(size=10)]
    ]

    window = gui.Window('Salvar Senha', layout, modal=True)

    while True:
        event, values = window.read()
        if event == gui.WINDOW_CLOSED:
            break
        elif event == 'Salvar':
            conta = values['conta']
            save_password(password, conta)
            window['dialog'].update('Senha salva com sucesso')

    window.close()

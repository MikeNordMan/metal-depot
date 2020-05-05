import PySimpleGUI as sg

sg.ChangeLookAndFeel('GreenTan')

# ------ Menu Definition ------ #
menu_def = [['File', ['Open', 'Save', 'Exit', 'Properties']],
            ['Edit', ['Paste', ['Special', 'Normal', ], 'Undo'], ],
            ['Help', 'About...'], ]

# ------ Column Definition ------ #
column1 = [[sg.Text('Column 1', background_color='#F7F3EC', justification='center', size=(10, 1))],
            [sg.Spin(values=('Spin Box 1', '2', '3'), initial_value='Spin Box 1')],
            [sg.Spin(values=('Spin Box 1', '2', '3'), initial_value='Spin Box 2')],
            [sg.Spin(values=('Spin Box 1', '2', '3'), initial_value='Spin Box 3')]]

layout = [







    [sg.Listbox(values=('Listbox 1', 'Listbox 2', 'Listbox 3'), size=(30, 3)),
        sg.Frame('Labelled Group',[[
        sg.Slider(range=(1, 100), orientation='v', size=(5, 20), default_value=25),
        sg.Slider(range=(1, 100), orientation='v', size=(5, 20), default_value=75),
        sg.Slider(range=(1, 100), orientation='v', size=(5, 20), default_value=10),
        sg.Column(column1, background_color='#F7F3EC')]])],
    [sg.Text('_'  * 80)],

    [sg.Text('Your Folder', size=(15, 1), auto_size_text=False, justification='right'),
        sg.InputText('Default Folder'), sg.FolderBrowse()],
    [sg.Submit(tooltip='Click to submit this window'), sg.Cancel()]
]


window = sg.Window('Everything bagel', layout, default_element_size=(40, 1), grab_anywhere=False)

event, values = window.read()

window.close()

sg.popup('Title',
            'The results of the window.',
            'The button clicked was "{}"'.format(event),
            'The values are', values)
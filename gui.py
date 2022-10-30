import PySimpleGUI as sg
import os.path

events = {
    'window_closed': sg.WIN_CLOSED,
}

right_click_menu = ['', ['Copy', 'Paste', 'Select All', 'Cut']]
INSERT = sg.tk.INSERT

layout = [
    [
        sg.Column([[
            sg.Text("Pobieranko"),
            sg.In(enable_events=True, key="download-path"),
            sg.FolderBrowse(),
        ], [
            sg.Multiline(size=(48, 10), enable_events=True, key="urls", right_click_menu=right_click_menu),
        ], [
            sg.Multiline(size=(48, 4), disabled=True, key="logs", background_color='#6F295B', text_color='#EBC106'),
        ]]),
        sg.VSeparator(),
        sg.Column([
            [
                sg.Button("Wyczyść", key='clear')
            ],
            [
                sg.Button("Poibierz", key='download')
            ],
            [
                sg.Button("Anuluj", key="stop", disabled=True)
            ]
        ])
    ]
]


def create_window():
    return sg.Window("Demo", layout)

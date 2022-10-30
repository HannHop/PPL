import threading

from gui import events, create_window, INSERT
from download import download_urls, abort_downloads

window = create_window()
mline = window['urls']


# Create an event loop
while True:
    event, values = window.read()
    # End program if user closes window or
    # presses the OK button
    if event == "OK" or event == events['window_closed']:
        break

    if event == 'download':
        window['logs'].update('')

        threading.Thread(
            name='threadzix',
            target=download_urls,
            args=(values['urls'].splitlines(), values['download-path'], lambda text: window['logs'].update(values['logs'] + '\n' + text)),
            daemon=True
        ).start()

        window['download'].update(disabled=True)
        window['stop'].update(disabled=False)

    if event == 'clear':
        window['urls'].update('')
        window['logs'].update('')
        window['download'].update(disabled=False)
        window['stop'].update(disabled=True)

    if event == 'stop':
        abort_downloads()
        window['download'].update(disabled=False)
        window['stop'].update(disabled=True)

    if event == 'Select All':
        mline.Widget.selection_clear()
        mline.Widget.tag_add('sel', '1.0', 'end')
    elif event == 'Copy':
        try:
            text = mline.Widget.selection_get()
            window.TKroot.clipboard_clear()
            window.TKroot.clipboard_append(text)
        except:
            print('Nothing selected')
    elif event == 'Paste':
        mline.Widget.insert(INSERT, window.TKroot.clipboard_get())
    elif event == 'Cut':
        try:
            text = mline.Widget.selection_get()
            window.TKroot.clipboard_clear()
            window.TKroot.clipboard_append(text)
            mline.update('')
        except:
            print('Nothing selected')


window.close()

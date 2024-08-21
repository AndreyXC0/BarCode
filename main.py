import webview

webview.create_window(
    title='Stickers',
    url='http://127.0.0.1:5500/index.html',
    width=920, height=600,
    min_size=[920, 600]
)
webview.start()
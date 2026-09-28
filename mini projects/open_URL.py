import webbrowser

def decorator(func):
    def wrapper(url):
        if "https://" in url and "." in url:
            func(url)
        else:
            print("неверный url")
    return wrapper

@decorator
def open_url(url):
    webbrowser.open(url)

open_url("https://github.com")




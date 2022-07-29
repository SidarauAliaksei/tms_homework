class BasePage:
    def __init__(self, driver, url):
        self.chrome = driver
        self.url = url

    def open(self):
        self.chrome.get(self.url)

class BasePage:

    def __init__(self, page):
        self.page = page

    def navigate(self, url):
        self.page.goto(url)

    def click(self, locator):
        self.page.locator(locator).click()

    def type(self, locator, text):
        self.page.locator(locator).fill(text)

    def get_text(self, locator):
        return self.page.locator(locator).inner_text()

    def wait_for_element(self, locator):
        self.page.locator(locator).wait_for()

    def is_visible(self, locator):
        return self.page.locator(locator).is_visible()
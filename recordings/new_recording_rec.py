from seleniumbase import BaseCase
BaseCase.main(__name__, __file__, "--uc")


class RecorderTest(BaseCase):
    def test_recording(self):
        self.activate_cdp_mode()
        self.open("https://canada.newark.com/w/search/prl/results?brand=general-devices&st=GENERAL-DEVICES")
        self.click("div#main > div:nth-of-type(2) > div:nth-of-type(2) > div > div:nth-of-type(2) > div:nth-of-type(2) > div > div:nth-of-type(2) > div:nth-of-type(2)")
        self.click("div#main > div:nth-of-type(2) > div:nth-of-type(2) > div > div:nth-of-type(2) > div:nth-of-type(2) > div > div:nth-of-type(2) > div:nth-of-type(2)")
        self.click('svg[aria-label="Next Page"]')
        self.click('div[data-testid="catalog.listerTable.table-cell__information-label"]')
        self.click('svg[aria-label="Next Page"] path')
        self.click('button:contains("Next Page")')

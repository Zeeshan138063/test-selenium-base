from seleniumbase import BaseCase
BaseCase.main(__name__, __file__, "--uc")


class RecorderTest(BaseCase):
    def test_recording(self):
        self.activate_cdp_mode()
        self.open("https://www.amazon.com/Blood-Pressure-Monitors/b?ie=UTF8&node=3777151")
        self.click("div.glow-toaster-footer span span input")
        self.click("span#glow-ingress-line2")
        self.press_keys("input#GLUXZipUpdateInput", "03051")
        self.click('span[data-action="GLUXPostalUpdateAction"] input')
        self.click("input#GLUXConfirmClose")
        self.click('a[href="/gp/goldbox?ref_=nav_cs_gb"]')
        self.open_if_not_url("https://www.amazon.com/gp/goldbox?ref_=nav_cs_gb")
        self.click('a[href="/Sony-WH-1000XM5-Canceling-Headphones-Hands-Free/dp/B09XS7JWHH?pd_rd_w=iBqHr&content-id=amzn1.sym.a817f217-0aba-4384-a44b-e8744053e726&pf_rd_p=a817f217-0aba-4384-a44b-e8744053e726&pf_rd_r=X2WYMF22TRW4XJTKSVT7&pd_rd_wg=hv5Bh&pd_rd_r=24e7248a-3d54-4fc1-bf26-3e730188e02b&pd_rd_i=B09XS7JWHH"] div')
        self.open_if_not_url("https://www.amazon.com/Sony-WH-1000XM5-Canceling-Headphones-Hands-Free/dp/B09XS7JWHH?pd_rd_w=iBqHr&content-id=amzn1.sym.a817f217-0aba-4384-a44b-e8744053e726&pf_rd_p=a817f217-0aba-4384-a44b-e8744053e726&pf_rd_r=X2WYMF22TRW4XJTKSVT7&pd_rd_wg=hv5Bh&pd_rd_r=24e7248a-3d54-4fc1-bf26-3e730188e02b&pd_rd_i=B09XS7JWHH")
        self.click("span#a-autoid-0-announce span")

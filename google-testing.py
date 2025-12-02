from seleniumbase import SB

# with SB( ad_block=True, locale_code="en") as sb:
#     sb.open("https://google.com/ncr")
#     sb.headless=True
#     sb.type('[title="Search"]', "https://www.amazon.com/Pressure-Monitors-Accurate-Automatic-Charging/dp/B0D8KN7Q59/\n")
#     sb.click('[href*="github.com/seleniumbase/SeleniumBase"]')
#     sb.save_screenshot_to_logs()  # (See ./latest_logs folder)
#     print(sb.get_page_title())



with SB(uc=True) as sb:
    url="gitlab.com/users/sign_in"
    sb.activate_cdp_mode(url)
    sb.sleep(2)
    sb.uc_gui_click_captcha()
    sb.post_message('hahahaha')
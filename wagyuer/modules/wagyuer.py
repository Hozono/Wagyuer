from PIL import Image
import re
import pyocr
import pyocr.builders
import chromedriver_binary
from selenium import webdriver
from selenium.webdriver.chrome.options import Options  # オプションを使うために必要

from django.conf import settings

from logging import getLogger, DEBUG, StreamHandler


# logger = getLogger(__name__)
# handler = StreamHandler()
# handler.setLevel(DEBUG)
# logger.addHandler(handler)

# logger.setLevel(DEBUG)
# logger.debug("execute wagyuer...")
class Wagyuer:
    def __init__(self, img_path: str) -> None:
        self.img_path = img_path
        self.wagyu_site_url = settings.WAGYU_SITE_URL

    def get_individual_id(self, img_path: str) -> str:
        # setting pyocr
        tools = pyocr.get_available_tools()
        tool = tools[0]

        # text detection
        txt = tool.image_to_string(
            Image.open(img_path),
            lang="jpn",
            builder=pyocr.builders.TextBuilder(tesseract_layout=6),
        )

        # get wagyu id
        regex = re.compile("\d{10}")
        match = regex.findall(txt)
        if match:
            individual_id = match[0]

        return individual_id

    def get_wagyu_infomation(self, individual_id: str, url: str):
        # setting chrome
        option = Options()
        option.add_argument("--headless")
        driver_path = "wagyuer/modules/chromedriver"
        driver = webdriver.Chrome(executable_path=driver_path, options=option)

        wagyu_infomation = {}
        # get wagyu info
        try:
            driver.get(url)

            # 「個体識別番号の検索」ボタンのクリック
            driver.find_element_by_class_name("nlbc_button_search").click()
            for window in driver.window_handles:
                driver.switch_to.window(window)
                if driver.title == "nlbcstyle":
                    break

            # 「同意する」ボタンのクリック
            driver.find_element_by_xpath(
                "/html/body/div/table[1]/tbody/tr[3]/td[2]/table/tbody/tr[2]/td[2]/table/tbody/tr[4]/td[2]/div/div[2]/table/tbody/tr/td[1]/input"
            ).click()

            # 「個体識別番号」の入力
            driver.find_element_by_name("txtIDNO").send_keys(individual_id)

            # 「検索」ボタンのクリック
            driver.find_element_by_xpath(
                "/html/body/div/table[1]/tbody/tr[3]/td[2]/table/tbody/tr[2]/td[2]/table/tbody/tr[1]/td[3]/form/table/tbody/tr[2]/td/input[2]"
            ).click()

            # 「個体情報」の取得
            indiviual_table = driver.find_element_by_xpath(
                "/html/body/div/table[1]/tbody/tr[3]/td[2]/table/tbody/tr[2]/td[2]/table/tbody/tr[3]/td[2]/table/tbody/tr/td/span/table[1]"
            )
            ths = indiviual_table.find_elements_by_tag_name("th")
            tds = indiviual_table.find_elements_by_tag_name("td")

            for th, td in zip(ths, tds):
                if th.text == "個体識別番号":
                    wagyu_infomation["individual_id"] = td.text
                elif th.text == "雌雄の別":
                    wagyu_infomation["sex"] = td.text
                elif th.text == "種別":
                    wagyu_infomation["kind"] = td.text

            # 「異動情報」の取得
            moving_info = driver.find_element_by_xpath(
                "/html/body/div/table[1]/tbody/tr[3]/td[2]/table/tbody/tr[2]/td[2]/table/tbody/tr[3]/td[2]/table/tbody/tr/td/span/table[2]"
            )
            trs = moving_info.find_elements_by_tag_name("tr")
            for tr in trs:
                tds = tr.find_elements_by_tag_name("td")
                for id, td in enumerate(tds):
                    if td.text == "出生":
                        birth_date = tds[id + 1].text
                        wagyu_infomation["birth_date"] = birth_date
                        birth_place = tds[id + 2].text + tds[id + 3].text
                        wagyu_infomation["birth_place"] = birth_place
                    elif td.text == "と畜":
                        slaughter_date = tds[id + 1].text
                        wagyu_infomation["slaughter_date"] = slaughter_date
                        slaughter_place = tds[id + 2].text + tds[id + 3].text
                        wagyu_infomation["slaughter_place"] = slaughter_place

        finally:
            driver.quit()

        return wagyu_infomation

    def main(self):
        individual_id = self.get_individual_id(img_path=self.img_path)
        wagyu_infomation = self.get_wagyu_infomation(individual_id, self.wagyu_site_url)

        return wagyu_infomation

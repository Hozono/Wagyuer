from PIL import Image
import sys
import re
import pyocr
import pyocr.builders
import requests
import chromedriver_binary
from selenium import webdriver
from selenium.webdriver.chrome.options import Options  # オプションを使うために必要


img_path = "/Users/Chihiro/Personal/10_Projects/Wagyuer/Images/20200523_151941.jpg"
tools = pyocr.get_available_tools()
tool = tools[0]


# text detection
txt = tool.image_to_string(
    Image.open(img_path),
    lang="jpn",
    builder=pyocr.builders.TextBuilder(tesseract_layout=6),
)

# get indiviual id
regex = re.compile("\d{10}")
match = regex.findall(txt)
if match:
    indiviual_id = match[0]

# get wagyu info
option = Options()  # オプションを用意
option.add_argument("--headless")  # ヘッドレスモードの設定を付与
driver_path = "./modules/chromedriver"
# driver = webdriver.Chrome(executable_path=driver_path, options=option)
driver = webdriver.Chrome(executable_path=driver_path)

url = "https://www.id.nlbc.go.jp/top.html?pc"

try:
    driver.get(url)
    driver.find_element_by_class_name("nlbc_button_search").click()
    for window in driver.window_handles:
        driver.switch_to.window(window)
        if driver.title == "nlbcstyle":
            break
    driver.find_element_by_xpath(
        "/html/body/div/table[1]/tbody/tr[3]/td[2]/table/tbody/tr[2]/td[2]/table/tbody/tr[4]/td[2]/div/div[2]/table/tbody/tr/td[1]/input"
    ).click()
    driver.find_element_by_name("txtIDNO").send_keys(indiviual_id)
    driver.find_element_by_xpath(
        "/html/body/div/table[1]/tbody/tr[3]/td[2]/table/tbody/tr[2]/td[2]/table/tbody/tr[1]/td[3]/form/table/tbody/tr[2]/td/input[2]"
    ).click()

    indiviual_table = driver.find_element_by_xpath(
        "/html/body/div/table[1]/tbody/tr[3]/td[2]/table/tbody/tr[2]/td[2]/table/tbody/tr[3]/td[2]/table/tbody/tr/td/span/table[1]"
    )
    ths = indiviual_table.find_elements_by_tag_name("th")
    tds = indiviual_table.find_elements_by_tag_name("td")
    for th, td in zip(ths, tds):
        print(th.text, td.text)

    moving_info = driver.find_element_by_xpath(
        "/html/body/div/table[1]/tbody/tr[3]/td[2]/table/tbody/tr[2]/td[2]/table/tbody/tr[3]/td[2]/table/tbody/tr/td/span/table[2]"
    )
    trs = moving_info.find_elements_by_tag_name("tr")
    for tr in trs:
        tds = tr.find_elements_by_tag_name("td")
        for td in tds:
            print(td.text)
finally:
    driver.quit()

from django.shortcuts import render

from setting import settings
import os


def index_template(request):
    f = request.FILES.get("file")
    if f:
        data = f.read()

        # with open(os.path.join(settings.MEDIA_ROOT, f.name), "wb+") as dest:
        #     for chunk in f.chunks():
        #         dest.write(chunk)
        indiviual_id = get_indiviual_id(data)
        context = {"indiviual_id": indiviual_id}
        print(indiviual_id)

        get_wagyu_data(indiviual_id)

        f = None
    return render(request, "index.html", context)


from io import BytesIO
from PIL import Image, ImageOps
import sys
import re
import pyocr
import pyocr.builders
import requests
import chromedriver_binary
from selenium import webdriver
from selenium.webdriver.chrome.options import Options  # オプションを使うために必要
from pathlib import Path


def get_indiviual_id(data):

    # img_path = "/Users/Chihiro/Personal/10_Projects/Waguyer/Images/20200523_151941.jpg"

    tools = pyocr.get_available_tools()
    tool = tools[0]

    # text detection
    txt = tool.image_to_string(
        Image.open(BytesIO(data)),
        lang="jpn",
        builder=pyocr.builders.TextBuilder(tesseract_layout=6),
    )

    # get indiviual id
    regex = re.compile("\d{10}")
    match = regex.findall(txt)
    if match:
        indiviual_id = match[0]

    return indiviual_id


def get_wagyu_data(indiviual_id):
    # get wagyu info
    option = Options()  # オプションを用意
    option.add_argument("--headless")  # ヘッドレスモードの設定を付与
    driver_path = "./modules/chromedriver"
    driver = webdriver.Chrome(executable_path=driver_path, options=option)
    # driver = webdriver.Chrome(executable_path=driver_path)

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

        table = driver.find_element_by_xpath(
            "/html/body/div/table[1]/tbody/tr[3]/td[2]/table/tbody/tr[2]/td[2]/table/tbody/tr[3]/td[2]/table/tbody/tr/td/span/table[1]"
        )
        trs = table.find_elements_by_tag_name("td")
        for td in trs:
            print(td.text)
    finally:
        driver.quit()

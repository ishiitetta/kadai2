import os
from selenium.webdriver import Chrome, ChromeOptions

### Chromeを起動する関数
def set_driver(driver_path,headless_flg):
    # Chromeドライバーの読み込み
    options = ChromeOptions()

    # ヘッドレスモード（画面非表示モード）をの設定
    if headless_flg == True:
        options.add_argument('--headless')

    # 起動オプションの設定
    options.add_argument('--user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36')
    #options.add_argument('log-level=3')
    options.add_argument('--ignore-certificate-errors')
    options.add_argument('--ignore-ssl-errors')
    options.add_argument('--incognito')          # シークレットモードの設定を付与

    # ChromeのWebDriverオブジェクトを作成する。
    return Chrome(executable_path=os.getcwd() + "\\" + driver_path,options=options)

def main():
    driver = set_driver("chromedriver",False)
    driver.get(
        "https://tenshoku.mynavi.jp/list/kw%E5%AF%8C%E5%A3%AB%E9%80%9A/?jobsearchType=14&search")
    name_list = driver.find_elements_by_class_name("cassetteRecruit__name")
    copy_list = driver.find_elements_by_class_name("cassetteRecruit__copy")

    for name,copy in zip(name_list,copy_list):
        print(name.text)
        print(copy.text)








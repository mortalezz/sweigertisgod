import os, glob, json
from PyPDF2 import PdfFileMerger
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

chrome_options = webdriver.ChromeOptions()

prefs = {
    "recentDestinations": [{"id": "Save as PDF", "origin": "local", "account": ""}],
    "selectedDestinationId": "Save as PDF",
    "version": 2,
    "isHeaderFooterEnabled": False,
}

path = os.getcwd()

prefs = {
    "printing.print_preview_sticky_settings.appState": json.dumps(prefs),
    "savefile.default_directory": "%s" % path,
}

chrome_options.add_experimental_option("prefs", prefs)
chrome_options.add_argument("--kiosk-printing")
# chrome_options.add_argument('--headless')

browser = webdriver.Chrome(r"chromedriver", options=chrome_options)
browser.get("https://automatetheboringstuff.com/2e/chapter0/")

for i in range(24):
    if i == 0:
        xpath = "/html/body/div[3]/div[1]/center/a[2]/img"
    else:
        xpath = "/html/body/div[3]/div[1]/center/a[3]/img"

    browser.execute_script("window.print();")
    if i == 23:
        break
    else:
        nextButton = browser.find_element_by_xpath(xpath)
        nextButton.click()

browser.close()


print("Now merging...")

# x = [a for a in sorted(os.listdir()) if a.endswith('.pdf')]
# merger = PdfFileMerger()

# for pdf in x:
#    merger.append(open(pdf, 'rb'))

# with open('sweigert.pdf;, 'wb') as fout:
#    merger.write(fout)

# for f in glob.glob('automate*.pdf'):
#    os.remove(f)

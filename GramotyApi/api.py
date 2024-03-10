import requests as req
from bs4 import BeautifulSoup

from search import Search



class Birchmark:
  def __init__(self, text, translate):
    self.text = text.strip() # birchmark.text
    self.translate = translate.strip() # birchmark.translate


class Api:
  def __init__(self):
    self.cities = {
      "1": "novgorod",
      "2": "vitebsk",
      "3": "zvenigorod",
      "4": "moscow",
      "5": "mstislavl",
      "6": "pskov",
      "7": "staraya-ryazan",
      "9": "smolensk",
      "10": "staraya-russa",
      "11": "tver",
      "12": "torzhok",
      "13": "vologda",
      "14": "pereyaslavl-ryazansky"
    }

  def get(self, search: Search, split: bool):
    split_list = {"True": "original-text-wrapper with-spaces", "False": "original-text-wrapper without-spaces"}
    link = f'http://gramoty.ru/birchbark/document/show/{self.cities[str(search["city"])]}/{search["number"]}/'
    # получить оригинальный текстъ берестяной грамоты
    soup = BeautifulSoup(req.get(link).text, 'html.parser')
    element = soup.find_all('div', class_=split_list[str(split)])
    elem_soup = BeautifulSoup(str(element[0]), 'html.parser')
    text = elem_soup.find_all('div')[0].text

    # получить переводъ
    element = soup.find_all('div', class_="translated-text-wrapper")
    elem_soup = BeautifulSoup(str(element[0]), 'html.parser')
    translate = elem_soup.find_all('div')[0].text

    return Birchmark(text, translate)

  def list(self, city: int):
    link = f'http://gramoty.ru/birchbark/document/list/?requestId=&number=&conventionalDateInitialYear=1020&conventionalDateFinalYear=1500&town%5B%5D={self.cities[str(city)]}&text=&translation='

  def get_font(self):
    return 'http://gramoty.ru/build/fonts/novgorod-unicode-2012/novgorod-unicode-2012.ttf'

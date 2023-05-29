import bs4
import pandas as pd


class addHTML:
    def __init__(self, txt_to_add:str):
        with open("C:/Users/kevlu/OneDrive/Desktop/Baseball/Kevin-Lucey.github.io/index.html") as f:
            txt = f.read()
            soup = bs4.BeautifulSoup(txt, "html.parser")
        print(soup.text)
        new_tag = soup.new_tag("div", attrs={"id":"test"})
        new_tag.string = txt_to_add
        print(new_tag.text)

        soup.html.body.append(new_tag)

        with open("C:/Users/kevlu/OneDrive/Desktop/Baseball/Kevin-Lucey.github.io/index.html", "w") as outf:
            outf.write(str(soup))






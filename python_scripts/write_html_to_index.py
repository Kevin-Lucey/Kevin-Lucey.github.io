import pandas as pd
from csv_to_html import csv_to_html


class html_writter:
    
    def __init__(self):
        self.start = "<!DOCTYPE html> <html>"
        self.body_s = "<body>"
        self.body_e = "</body>"
        self.end = "</html>"
        return None
    
    def get_head(self):
        return '<head><title>SCSU Baseball</title>    <link rel="stylesheet" type="text/css" href="styles.css">    <meta name="viewport" content="width=device-width, initial-scale=1">    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0-alpha3/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-KK94CHFLLe+nY2dmCWGMq91rCGa5gtU4mk92HdvYe+M/SXH301p5ILy+dN9+nJOZ" crossorigin="anonymous">    <meta http-equiv="cache-control" content="no-cache">     <meta http-equiv="expires" content="0">     <meta http-equiv="pragma" content="no-cache"></head>'

    
    def get_banner(self):
        return '<div class="container bg-white text-black" style="float: left;"><div id="header" class="container"><img id="logo" src="images/Owl_Head_Only.jpg"><h1 id="header2">NE10 Baseball</h1></div>'

    def get_main(self):
        return '<div id="content">2023 Season</div>'

    def get_string(self):
        try:
            string = self.start + self.body_s + self.get_head() + self.get_banner() + self.get_main() + self.add_table() + self.body_e + self.end
        except:
            string = self.start + self.body_s + self.get_head() + self.get_banner() + self.get_main() + self.body_e + self.end
        return string
    
    def add_table(self):
        table = csv_to_html("NE10_OPSadjusted.csv")
        return "<div>"+table+"</div>"
    
    def write_to_html(self):
        f = open("index2.html", "w")
        f.write(self.get_string())
        f.close()
    
html_writter().write_to_html()
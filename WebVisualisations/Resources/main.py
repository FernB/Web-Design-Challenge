import pandas as pd


df = pd.read_csv("cities.csv")

html = df.to_html()

html_file = open("index.html","w")
html_file.write(html)
html_file.close()
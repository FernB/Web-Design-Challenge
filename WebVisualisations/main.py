import pandas as pd


df = pd.read_csv("WebVisualisations\cities.csv")

html = df.to_html(index=False)

html_file = open("WebVisualisations\df.html","w")
html_file.write(html)
html_file.close()
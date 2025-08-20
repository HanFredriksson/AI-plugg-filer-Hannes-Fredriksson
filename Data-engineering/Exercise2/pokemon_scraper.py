import pandas as pd

URL = "https://sv.wikipedia.org/wiki/Lista_%C3%B6ver_Pok%C3%A9mon"
tabel = pd.read_html(URL)

df = tabel[0]

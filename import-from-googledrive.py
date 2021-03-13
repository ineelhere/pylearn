import pandas as pd
url = "<enter the url for the desired file copied from google drive here>"
path = 'https://drive.google.com/uc?export=download&id='+url.split('/')[-2]
df = pd.read_csv(path)

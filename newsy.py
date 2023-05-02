url1 = "https://www.mnb.mn"
url2 = "https://www.bloomberg.com"
from newsplease import NewsPlease
article = NewsPlease.from_url(url2)
print(vars(article))
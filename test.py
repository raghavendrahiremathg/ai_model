import ntlk 
ntlk.download('stopwords')
from ntlk.corpus import stopwords

en_stopwords = stopwords.words('english')
print(en_stopwords)
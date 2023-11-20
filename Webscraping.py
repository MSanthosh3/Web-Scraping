import requests
from bs4 import BeautifulSoup as bs 
import re 


#regular expression
import nltk #natural language toolkit
#pip install nltk
nltk.download('stopwords') #procedure 1 to install stopwords
from nltk.corpus import stopwords #procedure 2 to install stopwords


url ="https://www.amazon.in/Apple-iPhone-Pro-Deep-Purple/product-reviews/B0BDK64JGN/ref=cm_cr_dp_d_show_all_btm?ie=UTF8&reviewerType=all_reviews"
response = requests.get(url)
soup = bs(response.content,"html.parser")
reviews = soup.findAll("span",attrs={"data-hook":"review-body"}) 


amazon_reviews=[]
for i in range(len(reviews)):
    amazon_reviews.append(reviews[i].get_text())  
    
    
# writing reviews in a text file 
with open(r"F:/Machine Learning/amazon_review.txt","w",encoding='utf8') as output:
    output.write(str(amazon_reviews)) 
        
  
#utf -> unique code text format. for encoding purpose

# Joinining all the reviews into single paragraph 


ip_rev_string = " ".join(amazon_reviews)


# Removing unwanted symbols incase if exists
ip_rev_string = re.sub("[^A-Za-z" "]+"," ",ip_rev_string).lower()
ip_rev_string = re.sub("[0-9" "]+"," ",ip_rev_string)
ip_rev_string


# covert the paragraph into single word
#used to know how many words or repeated or to find stopping words.

ip_reviews_words = ip_rev_string.split(" ")
ip_reviews_words


#here we are going to eliminate the stoping words
ip_reviews_words =[w for w in ip_reviews_words if not w in
                   set(stopwords.words('english'))]
# Join all the reviews into single paragraph 
ip_rev_string = " ".join(ip_reviews_words)
# WordCloud can be performed on the string inputs.
#That is the reason we have combined entire reviews into
# single paragraph
import matplotlib.pyplot as plt
import wordcloud
#pip install wordcloud
from wordcloud import WordCloud,STOPWORDS#3
wordcloud_ip = WordCloud(
                      background_color='white',
                      width=1920,
                      height=1080
                     ).generate(ip_rev_string)
plt.figure(dpi=400)
plt.imshow(wordcloud_ip)#imageshow

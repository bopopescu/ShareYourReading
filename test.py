
from lxml  import etree
import requests
import  xml.dom.minidom

url = "https://www.goodreads.com/book/show.xml"
keyword = "Harry Potter"
params = {"key":"swpFwgtISW6ufbWB5ffFug",
          "id": 2}

res = requests.get(url=url,params=params)
# print(res.content)

data = etree.XML(res.content)


for B in data.iter('book'):
    title = B.find('title').text
    url = B.find('image_url').text
    pub_yr = B.find('publication_year').text
    publisher = B.find('publisher')
    # descrip = B.find('description').innerXML

    # author = B.find('author').find('name').text
    # for T in B.iter('authors'):
    #     author = T.find('name').text
    #     authors.append(author)


print(title)
print(pub_yr)
print(url)
print(publisher)
# num=0
# ratings = []
# titles = []
# book_ids = []
# authors = []
# urls = []
# for a in data.iter('work'):
#
#     book_rating = a.find('average_rating').text
#     ratings.append(book_rating)
#
#     book_title = a.find('best_book').find('title').text
#     titles.append(book_title)
#
#     book_id = a.find('best_book').find('id').text
#     book_ids.append(book_id)
#
#     author = a.find('best_book').find('author').find('name').text
#     authors.append(author)
#
#     image_url = a.find('best_book').find('image_url').text
#     urls.append(image_url)
#
#     num = num+1

# for i in range(num):
#     print('%d' % (i+1))
#     print('Rating: %s' % ratings[i])
#     print('Title: %s' % titles[i])
#     print('Id: %s' % book_ids[i])
#     print('author: %s' % authors[i])
#     print('Image url: %s' % urls[i])










#print(data.find('title').text)


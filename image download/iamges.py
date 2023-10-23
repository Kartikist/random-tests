import requests

response = requests.get(url='https://th.bing.com/th/id/R.4be8a04fed0ec1f5d148598d107ad647?rik=SWIGHOff%2ftjfKA&riu=http%3a%2f%2fupload.wikimedia.org%2fwikipedia%2fcommons%2f6%2f68%2fOrange_tabby_cat_sitting_on_fallen_leaves-Hisashi-01A.jpg&ehk=0Q3OweHLh0H%2bNUvty2TEIaCTXgMt1Th98C%2fSbzoBTlQ%3d&risl=1&pid=ImgRaw&r=0')

response.content

with open("image.jpg", 'wb') as iamge:
    iamge.write(response.content)
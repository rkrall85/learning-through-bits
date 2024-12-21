import requests
import bs4

#res = requests.get('https://en.wikipedia.org/wiki/Room_641A')
res = requests.get('http://www.brooksrunning.com/en_us/adrenaline-gts-17-mens-running-shoes/110241.html')

#print(res.text)

soup = bs4.BeautifulSoup(res.text,'lxml')
'''
soup.select('div')          All elements with the <div> tag
soup.select('#some_id')     The HTML element containing the id attribute of some_id
soup.select('.notice')      All the HTML elements with the CSS class named notice
soup.select('div span')     Any elements named <span> that are within an element named <div>
soup.select('div > span')   Any elements named <span> that are directly within an element named <div>, with no other element in between
'''


#print(soup.select('.product--meta__price'))
item_price = ''

#grabbing all prices
for item in soup.select('.product--meta__price'):
    item_price = item.text

#getting the prices in a list
prices = item_price.split(' ')

#getting just the price int instead of the having he $ sign in the text
current_prices = []
for i in range(len(prices)):
    current_price = prices[i]
    current_prices.append(int(current_price[1:])) #remove $ sign and cast to int

min_price = min(current_prices) #finding the min price if there are multi prices




import requests
import bs4
from pyquery import PyQuery

class ItemPrice():
    def __init__(self,db_connection, item_id = 0):
        self.db_connection          = db_connection
        self.item_id                = item_id

    def CreateDailyPrice(self):
        #create special logic for all or one item
        sql = "EXEC [dbo].[usp_GetTrackItems]{}".format(self.item_id)
        self.db_connection.execute(sql)
        list_items = self.db_connection.fetchall()#[0] #fetchone will only return first result
        #loop through all stores for an item
        for i in (list_items):
            item_id = i[0]
            store_id = i[1]
            item_url = i[2]
            item_div_class = i[3]
            item_span_class = i[4]
            web_scrap = i[5]
            if web_scrap.lower() == 'y':
                self.WebScrap(item_id,store_id, item_url, item_div_class,item_span_class)

        self.db_connection.commit()#need this to commit transaction

    def WebScrap(self,item_id, store_id, item_url, item_div_class,item_span_class):
        #setting up for web scrap using BeautifulSoup
        #error handling incase the handshake to the website failed
        try:
            res = requests.get(item_url)
        except:
            print("error web scrapping {}".format(item_url))
            return ("error")

        #soup = bs4.BeautifulSoup(res.text,'lxml')
        soup = bs4.BeautifulSoup(res.text,'html.parser')

        print("finding price at {}".format(item_url))
        #finding the price based on the div and span class of the website
        store_price = soup.find("div", class_=item_div_class).find("span", class_=item_span_class)
        current_price = float(0)
        #remove $sign if its there and casting to a int

        if store_price != None:
            current_price = store_price.text
            if current_price[0] == '$':
                current_price = float(current_price[1:])
            else:
                current_price = float(current_price)
            print("Price found: {}".format(current_price))

        if current_price != float(0):
            self.InsertDailyPrice(item_id, store_id, current_price) #Calling function to insert rows into db

    #Place holder for API function grab

    def InsertDailyPrice(self,item_id, store_id, current_price):
        sql = "EXEC [dbo].[usp_CreateItemPriceHistory] {},{},{}".format(item_id,store_id,current_price)
        self.db_connection.execute(sql)#, params) #executing sproc
        self.db_connection.commit()#need this to commit transaction

    def GetDailyPrice(self, store_id, user_id):
        sql = "EXEC [dbo].[usp_GetUserCurrentPriceItem] {},{},{}".format(self.item_id,store_id, user_id)
        self.db_connection.execute(sql)#, params) #executing sproc
        list_item_price = db_connection.fetchall()#[0] #fetchone will only return first result
        labels = ['item id','item name','store id','store name','purchase price','purchase date','latest recorded date','latest recorded price']
        df = pd.DataFrame.from_records(list_item_price, columns=labels) #create dataframe from list
        print (df) #output dataframe
        db_connection.commit()#need this to commit transaction

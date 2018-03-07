


import requests
import bs4

class ItemPrice():
    def __init__(self,db_connection, item_id = 0):
        self.db_connection          = db_connection
        self.item_id                = item_id

    def CreateDailyPrice(self):
        #create special logic for all or one item
        sql = "EXEC [dbo].[usp_GetTrackItems]{}".format(self.item_id)
        self.db_connection.execute(sql)
        list_items = self.db_connection.fetchall()#[0] #fetchone will only return first result
        self.db_connection.commit()#need this to commit transaction

        for i in (list_items):
            item_id = i[0]
            store_id = i[1]
            item_url = i[2]
            item_web_class = i[3]
            web_scrap = i[4]
            if web_scrap.lower() == 'y':
                self.WebScrap(item_id,store_id, item_url, item_web_class)

    def WebScrap(self,item_id, store_id, item_url, item_web_class):
        #setting up for web scrap using BeautifulSoup
        res = requests.get(item_url)
        soup = bs4.BeautifulSoup(res.text,'lxml')
        store_item_price = ''

        #grabbing all prices
        for item in soup.select(item_web_class):
            store_item_price = item.text

        #Incase more than one price is given
        prices = store_item_price.split(' ')
        current_prices = []
        for i in range(len(prices)):
                current_price = prices[i]
                current_prices.append(int(current_price[1:])) #remove $ sign and cast to int

        current_store_price = min(current_prices) #finding the min price if there are multi prices
        self.InsertDailyPrice(item_id, store_id, current_store_price) #Calling function to insert rows into db

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

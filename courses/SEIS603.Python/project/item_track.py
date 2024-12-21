

#this script is for tracking items for a user.
def GetCurrentTracking(db_connection,pd,user_id):
    #function to grab all items a user is tracking
    sql = "EXEC [dbo].[usp_GetCurrentTracking] {}".format(user_id)
    db_connection.execute(sql)#, params) #executing sproc
    list_items = db_connection.fetchall()#[0] #fetchone will only return first result
    #df = pd.Series(list_items)
    labels = ['item id','item name']
    df = pd.DataFrame.from_records(list_items, columns=labels) #create dataframe from list
    print (df) #output dataframe
    db_connection.commit()#need this to commit transaction


def CreateUserItemTrack(db_connection, user_id, item_id):
    #Create user item track record
    sql = "EXEC [dbo].[usp_CreateUserItemTrack] {},{}".format(user_id, item_id)
    db_connection.execute(sql)#, params) #executing sproc
    db_connection.commit()#need this to commit transaction


def GetuserTrackItem(db_connection, user_id, item_id, store_id):
    #grab all items they are tracking
    sql =  """\
            DECLARE	@user_id INT,
                       @item_id INT,
                       @store_id int,
                       @web_scrap char(1),
                       @item_url varchar(500),
                       @item_web_class VARCHAR(50);
            exec [dbo].[usp_GetUserTrackItem] @u_id = ?,
                                         @i_id = ?,
                                         @s_id = ?,
                                         @web_scrap_out = @web_scrap OUTPUT,
                                         @item_url_out = @item_url OUTPUT,
                                         @item_web_class_out = @item_web_class OUTPUT
                                         ;
            Select @web_scrap,@item_url,@item_web_class;
        """
    params = (user_id,item_id,store_id,) #creating parms
    db_connection.execute(sql, params) #executing sproc
    data = db_connection.fetchone() #putting results into row class
    web_scrap = data[0]
    item_url = data[1]
    item_web_class = data[2]
    db_connection.commit()
    return web_scrap,item_url,item_web_class


#Getting an items pricing listing
def GetUserItemTrackPrices(db_connection, pd, user_id, item_id):
    sql = "EXEC [dbo].[usp_GetUserItemTrackPrices] {},{}".format(user_id,item_id)
    db_connection.execute(sql) #executing sproc
    price_lists = db_connection.fetchall()#[0] #fetchone will only return first result
    labels = ['item id','item name','store id','store name','current price']
    df_current_price = pd.DataFrame.from_records(price_lists, columns=labels) #create dataframe from list
    #pivot data so its easier to read to compare prices between stores.
    pvt_current_prices =  df_current_price.pivot(index='store name',columns='item name',values = 'current price' ).fillna(0)
    print(pvt_current_prices)

'''
def GetUserCurrentPriceItem(db_connection,pd, item_id, store_id, user_id):
    #Get item
    sql =  """\
            exec [dbo].[usp_GetUserCurrentPriceItem] @item_id = ?,
                                         @store_id = ?,
                                         @user_id = ?
                                         ;

        """
    params = (item_id,store_id,user_id,) #creating parms
    db_connection.execute(sql, params) #executing sproc
    price_lists = db_connection.fetchall()#[0] #fetchone will only return first result
    labels = ['item id','item name','store id','store name','purchase price','purchase date','latest recorded date','latest recorded price']
    df_current_price = pd.DataFrame.from_records(price_lists, columns=labels) #create dataframe from list
    print (df_current_price) #output dataframe
    db_connection.commit()#need this to commit transaction
'''

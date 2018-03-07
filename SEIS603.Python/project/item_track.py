

class Item():
    def __init__(self,dt, db_connection,user_id, store_id,store_name,item_id,web_scrap):
        self.dt                     = dt
        self.db_connection          = db_connection
        self.user_id                = user_id
        self.store_id               = store_id
        self.store_name             = store_name
        self.item_id                = item_id
        self.web_scrap              = web_scrap

    def TrackInput(self):
        i_price = input("What price did you pay?")
        i_purchase_date = input("When did you purchase the item (mm/dd/yyyy)?")
        month, day, year = map(int, i_purchase_date.split('/'))
        i_p_date = self.dt.date(year, month, day)
        i_url = input("What is the URL of the item from {}:".format(self.store_name))
        i_web_class = input("What is the web class for item you want to track (for example: .product--meta__price )?")
        self.StoreItem(i_url,i_web_class)
        self.UserTrackItem(i_price,i_p_date)


    def StoreItem(self,item_url,item_web_class):
        sql = "EXEC [dbo].[usp_CreateStoreItem] {},{},'{}','{}'".format(self.store_id,self.item_id,item_url, item_web_class)
        self.db_connection.execute(sql)#, params) #executing sproc
        self.db_connection.commit()#need this to commit transaction

    def UserTrackItem(self,item_price,item_purschase_date):
        sql =  """\
                DECLARE	@user_id INT,
                           @item_id INT,
                           @store_id int,
                           @price DEC(8,2),
                           @purchase_date DATE,
                           @message VARCHAR(50);
                exec [dbo].[usp_CreateUserItemTrack] @user_id = ?,
                                             @item_id = ?,
                                             @store_id = ?,
                                             @price = ? ,
                                             @purchase_date = ?,
                                             @message = @message OUTPUT;
                Select @message;
            """
        params = (self.user_id,self.item_id,self.store_id,item_price,item_purschase_date,) #creating parms
        self.db_connection.execute(sql, params) #executing sproc
        data = self.db_connection.fetchone() #putting results into row class
        message = data[0]
        self.db_connection.commit()#need this to commit transaction



def GetuserTrackItem(db_connection, user_id, item_id, store_id):
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



#s_id = 100
#u_id = 100


class Item():
    def __init__(self,db_connection,pd):
        self.db_connection          = db_connection
        self.pd                     = pd

    def CreateItem(self):
        #user user all Items
        input_name = "Please enter the name of product: "
        input_brand = "Please enter the brand of the product: "
        input_model = "Please enter the model number: " #not required
        input_description = "Plese enter the description of product: "
        input_upc = "Please enter the upc: "
        active = False
        while not(active):
            name = str(input(input_name))
            brand = str(input(input_brand))
            model = int(input(input_model))
            description = str(input(input_description))
            upc = str(input(input_upc))
            if len(name)== 0 or len(brand) == 0 or len(description) == 0 or len(upc) == 0:
                print("Please enter all required fields; name, brand, description, and upc")
                active = False
            else:
                active = True

        #call proc to insert value into table
        new_item_id = 0
        sql =  """\
                DECLARE	@new_item_id int;
                exec [dbo].[usp_CreateItem] @item_brand = ?,
                                             @item_name = ?,
                                             @item_model = ?,
                                             @item_description = ?,
                                             @item_upc = ?,
                                             @item_id = @new_item_id OUTPUT;
                Select @new_item_id;
            """
        params = (name,brand,model,description,upc) #creating parms
        self.db_connection.execute(sql, params) #executing sproc
        data = self.db_connection.fetchone() #putting results into row class
        new_item_id = data[0] #getting id
        self.db_connection.commit()#need this to commit transaction
        return new_item_id


def GetItems(db_connection,pd):
    sql = "EXEC [dbo].[usp_GetItems];"
    db_connection.execute(sql)
    list_items = db_connection.fetchall()
    labels = ['ID','Brand','Name','Model','Description','UPC'] #might drop UPC
    df = pd.DataFrame.from_records(list_items, columns=labels) #create dataframe from list
    print (df) #output dataframe
    db_connection.commit()#need this to commit transaction



#def GetItemInfo(db_connect, item_id):

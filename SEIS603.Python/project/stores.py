#this script will get all the stores we support
#Would like to add insert and update functionality later

import db_connection as d
crsr = d.database_connection()


def GetStores():
    sql = "EXEC [dbo].[usp_GetStores];"
    crsr.execute(sql)
    return crsr.fetchall()#[0] #fetchone will only return first result


def GetStoreName(s_id):
    sql = """\
            exec [dbo].[usp_GetStoreInfo] @s_id = ?;
            
        """
    params = (s_id,) #creating parms
    crsr.execute(sql, params) #executing sproc
    data = crsr.fetchone() #putting results into row class
    store_name = data[0] #getting id
    return store_name

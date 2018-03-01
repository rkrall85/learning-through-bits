

#s_id = 100
#u_id = 100


def GetItems(db_connection):
    sql = "EXEC [dbo].[usp_GetItems];"
    db_connection.execute(sql)
    return db_connection.fetchall()#[0] #fetchone will only return first result

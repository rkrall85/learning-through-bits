SET QUOTED_IDENTIFIER ON
GO
SET ANSI_NULLS ON
GO
-- =============================================
-- Author:		Robert Krall
-- Create date: 03/02/2018
-- Description:	Get all valid store items to grab the price.
-- =============================================
CREATE PROCEDURE [dbo].[usp_GetStoreItems]
-- Add the parameters for the stored procedure here
	@store_id INT = 0
AS
    BEGIN
        /*
	@item_id INT OUT, 
	@store_id INT OUT, 
	@item_url VARCHAR(500) out,
	@item_web_class VARCHAR(50) out,
	@web_scrap	CHAR(1) OUT
*/


        -- SET NOCOUNT ON added to prevent extra result sets from
        -- interfering with SELECT statements.
        --SET NOCOUNT ON;
	DECLARE @Sql AS VARCHAR(5000)
	SET @Sql = '
			SELECT     i.i_id
				     , i.i_name
			FROM       dbo.Item AS i
			INNER JOIN dbo.StoreItem AS si
	            ON i.i_id = si.i_id
		    INNER JOIN dbo.Store AS s
			    ON si.s_id = s.s_id
			where 1= 1'
	IF not(@store_id  = 0) SET @Sql = @Sql + ' and s.s_id = ' + CAST(@store_id AS VARCHAR)
	
	exec(@Sql)            
				



    END;
GO

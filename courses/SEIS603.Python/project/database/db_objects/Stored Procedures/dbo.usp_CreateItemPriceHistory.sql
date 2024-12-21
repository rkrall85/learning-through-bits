SET QUOTED_IDENTIFIER ON
GO
SET ANSI_NULLS ON
GO
-- =============================================
-- Author:		Robert Krall
-- Create date: 03/02/2018
-- Description:	Get all valid store items to grab the price.
-- =============================================
CREATE PROCEDURE [dbo].[usp_CreateItemPriceHistory]
-- Add the parameters for the stored procedure here
	@item_id INT,
	@store_id INT,
	@item_price DEC(9,2)


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
		IF EXISTS (SELECT 1 
					FROM dbo.ItemPriceHistory AS iph
						WHERE iph.i_id = @item_id
						AND iph.s_id = @store_id
						AND iph.i_date =  CONVERT(date, GETDATE())
		)
			BEGIN
				UPDATE dbo.ItemPriceHistory
				SET ItemPriceHistory.i_price = @item_price
				WHERE i_id = @item_id
						AND s_id = @store_id
						AND i_date = CONVERT(date, GETDATE())
			END
		ELSE
			BEGIN
            
        		INSERT INTO dbo.ItemPriceHistory (
					                             i_id
						                       , s_id
							                   , i_date
								               , i_price
		                                 )
				VALUES ( @item_id         -- i_id - int
						, @store_id         -- s_id - int
						, GETDATE() -- date - date
						, @item_price      -- i_price - decimal(9, 2)
					)
			END
                
			


    END;
GO

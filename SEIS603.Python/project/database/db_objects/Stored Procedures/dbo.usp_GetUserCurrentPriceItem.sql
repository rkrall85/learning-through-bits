SET QUOTED_IDENTIFIER ON
GO
SET ANSI_NULLS ON
GO
-- =============================================
-- Author:		<Author,,Name>
-- Create date: <Create Date,,>
-- Description:	<Description,,>
-- =============================================
create PROCEDURE [dbo].[usp_GetUserCurrentPriceItem]
	-- Add the parameters for the stored procedure here
	@item_id INT,
	@store_id INT,
	@user_id INT
    
AS
BEGIN
	-- SET NOCOUNT ON added to prevent extra result sets from
	-- interfering with SELECT statements.
	SET NOCOUNT ON;

    -- Insert statements for procedure here
	

WITH cte_current_items AS 
(
SELECT uit.i_id
	 , i.i_name
     , uit.s_id
	 , s.s_name
     , uit.price AS purchased_price
     , uit.purchase_date
FROM dbo.UserItemTracking AS uit
inner JOIN dbo.Store AS s ON uit.s_id = s.s_id
inner JOIN dbo.Item AS i ON uit.i_id = i.i_id
WHERE uit.u_id = @user_id
		AND s.s_id = @store_id
		AND i.i_id = @item_id
)
,cte_current_item_price AS (
SELECT  iph.i_id,
		c.s_id,
		MAX(iph.i_date) AS latest_recorded_date,
		iph.i_price AS latest_recorded_price
FROM dbo.ItemPriceHistory AS iph
LEFT JOIN cte_current_items c ON iph.i_id = c.i_id and  iph.s_id = c.s_id
GROUP BY iph.i_id
       , c.s_id
       , iph.i_price
)
SELECT c1.i_id
     , c1.i_name
     , c1.s_id
     , c1.s_name
     , c1.purchased_price
     , c1.purchase_date
	 , c2.latest_recorded_date
	 , c2.latest_recorded_price
FROM cte_current_items c1
LEFT JOIN cte_current_item_price c2 ON c1.i_id = c2.i_id AND c1.s_id = c2.s_id

END
GO

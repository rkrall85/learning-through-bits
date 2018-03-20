SET QUOTED_IDENTIFIER ON
GO
SET ANSI_NULLS ON
GO
--WITH cte_track_items AS 
CREATE PROCEDURE [dbo].[usp_GetUserItemTrackPrices]
	-- Add the parameters for the stored procedure here
	@user_id INT,
	@item_id INT = null
AS
BEGIN

/*
Create By: Robert Krall
Created On: 03/09/0218
Purpose: Return items a user is trackign by store with prices.

*/
WITH cte_data AS (
SELECT uit.i_id
		,i.i_name
		,s.s_id
		,s.s_name
		,iph.i_price AS Current_Price
		,iph.i_date AS Lastest_Date
		, ROW_NUMBER() OVER ( PARTITION BY uit.i_id
                                          , i.i_name
                                          , s.s_id
                                          , s.s_name
                               ORDER BY uit.i_id
                                      , i.i_name
                                      , s.s_id
                                      , s.s_name
                                      , iph.i_date DESC
                             ) AS row_num
FROM dbo.UserItemTracking AS uit
INNER JOIN dbo.ItemPriceHistory AS iph ON uit.i_id = iph.i_id
INNER JOIN dbo.Store AS s ON iph.s_id = s.s_id
INNER JOIN dbo.Item AS i ON uit.i_id = i.i_id
WHERE uit.u_id=@user_id
	AND ISNULL(@item_id,0) = 
				CASE
					WHEN @item_id != 0 THEN i.i_id 
					ELSE 0
				END
)
SELECT cte_data.i_id
     , cte_data.i_name
     , cte_data.s_id
     , cte_data.s_name
     , cte_data.Current_Price 
FROM cte_data
WHERE row_num = 1
ORDER BY i_name asc, Current_Price asc
	   ;

END

GO

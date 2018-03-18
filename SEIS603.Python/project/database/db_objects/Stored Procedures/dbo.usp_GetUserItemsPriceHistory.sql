SET QUOTED_IDENTIFIER ON
GO
SET ANSI_NULLS ON
GO
-- =============================================
-- Author:		Robert Krall
-- Create date: 3/31/2018
-- Description:	get a list of all user items bring tracked with their price history
-- =============================================
CREATE PROCEDURE [dbo].[usp_GetUserItemsPriceHistory]
	-- Add the parameters for the stored procedure here
	@user_id int
AS
BEGIN
	-- SET NOCOUNT ON added to prevent extra result sets from
	-- interfering with SELECT statements.
	SET NOCOUNT ON;


	SELECT  i.i_id AS ItemID,
			i.i_name AS ItemName,
			i.i_brand AS Brand,
			iph.s_id AS StoreID,
			s.s_name AS StoreName,
			iph.i_price AS ItemPrice, 
			iph.i_date AS ItemDate
	FROM dbo.UserItemTracking AS uit
	INNER JOIN dbo.Item AS i ON uit.i_id = i.i_id
	INNER JOIN dbo.StoreItem AS si ON i.i_id = si.i_id AND uit.i_id = si.i_id
	INNER JOIN dbo.Store AS s ON si.s_id = s.s_id
	INNER JOIN dbo.ItemPriceHistory AS iph ON si.i_id = iph.i_id AND si.s_id = iph.s_id
	WHERE uit.u_id = @user_id
	ORDER BY i.i_id, s.s_id, iph.i_date

END
GO

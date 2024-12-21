SET QUOTED_IDENTIFIER ON
GO
SET ANSI_NULLS ON
GO
-- =============================================
-- Author:		Robert Krall
-- Create date: 03/01/2018
-- Description:	Create New Items in db
-- =============================================
CREATE PROCEDURE [dbo].[usp_CreateItem]
	-- Add the parameters for the stored procedure here
	@item_brand varchar(50),
	@item_name VARCHAR(50),
	@item_model INT,
	@item_description VARCHAR(50),
	@item_upc VARCHAR(50),
	@item_id INT OUTPUT
AS
BEGIN
	-- SET NOCOUNT ON added to prevent extra result sets from
	-- interfering with SELECT statements.
	SET NOCOUNT ON;

	IF EXISTS (
				SELECT 1 
				FROM dbo.Item AS iph
				WHERE iph.i_upc = @item_upc
				)
		BEGIN
				UPDATE dbo.Item
				SET Item.i_brand = @item_brand,
					Item.i_name = @item_name,
					Item.i_model = @item_model,
					Item.i_description = @item_description
				WHERE i_upc = @item_upc

		END
		ELSE
			BEGIN
				INSERT INTO dbo.Item (
		                         i_brand
		                       , i_name
		                       , i_model
		                       , i_description
		                       , i_upc
		                     )
				VALUES ( 
							@item_brand -- i_brand - varchar(50)
							, @item_name -- i_name - varchar(50)
							, @item_model  -- i_model - int
							, @item_description -- i_description - varchar(50)
							, @item_upc -- i_upc - varchar(50)
						)
			SELECT @item_id = @@IDENTITY

		END
	


END
GO

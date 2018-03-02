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
	@item_id INT OUTPUT,
	@message VARCHAR(50) output
AS
BEGIN
	-- SET NOCOUNT ON added to prevent extra result sets from
	-- interfering with SELECT statements.
	SET NOCOUNT ON;

	IF (@item_name IS NULL
		AND @item_description IS NULL
        --AND @item_upc IS NULL
		)
       SELECT @message = 'You need to need all input values'
	ELSE
		INSERT INTO dbo.Item (
		                         i_brand
		                       , i_name
		                       , i_model
		                       , i_description
		                       , i_upc
		                     )
		VALUES ( @item_brand -- i_brand - varchar(50)
		       , @item_name -- i_name - varchar(50)
		       , @item_model  -- i_model - int
		       , @item_description -- i_description - varchar(50)
		       , @item_upc -- i_upc - varchar(50)
		    )
    
		SELECT @item_id = @@IDENTITY, @message = 'You have successfully saved an item'
	

END
GO

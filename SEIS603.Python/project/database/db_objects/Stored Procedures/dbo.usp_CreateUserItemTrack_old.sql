SET QUOTED_IDENTIFIER ON
GO
SET ANSI_NULLS ON
GO
-- =============================================
-- Author:		Robert Krall
-- Create date: 2/28/2017
-- Description:	This sp will create a new item tracker for a user
-- =============================================
create PROCEDURE [dbo].[usp_CreateUserItemTrack_old]
	-- Add the parameters for the stored procedure here
	@user_id INT,
	@item_id INT,
	@store_id int,
	@price DEC(8,2),
	@purchase_date DATE,
	@message VARCHAR(50) output
AS
BEGIN
	-- SET NOCOUNT ON added to prevent extra result sets from
	-- interfering with SELECT statements.
	SET NOCOUNT ON;



   
   --making sure all values are filled out
	IF NOT EXISTS (SELECT 1 FROM dbo.UserPriceProtection AS uit 
						WHERE uit.u_id = @user_id
							AND uit.i_id = @item_id
							AND uit.s_id = @store_id
					)
		INSERT INTO dbo.UserPriceProtection (
				                                     u_id
				                                   , i_id
				                                   , s_id
				                                   , price
				                                   , purchase_date
				                                   , tracking_end_date
				                                 )
				VALUES ( @user_id         -- u_id - int
				       , @item_id         -- i_id - int
				       , @store_id         -- s_id - int
				       , @price      -- price - decimal(8, 2)
				       , @purchase_date-- purchase_date - date
				       , DATEADD(d,90,@purchase_date) -- tracking_end_date - date --maybe pass the days to add in the proce?
				    )
				;
				SELECT @message = 'Success';
		
END

GO

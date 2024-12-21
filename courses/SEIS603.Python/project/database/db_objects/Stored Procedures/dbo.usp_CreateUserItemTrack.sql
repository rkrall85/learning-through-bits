SET QUOTED_IDENTIFIER ON
GO
SET ANSI_NULLS ON
GO
-- =============================================
-- Author:		Robert Krall
-- Create date: 2/28/2017
-- Description:	This proc will create a new entry fo a user to track a product
-- =============================================
CREATE PROCEDURE [dbo].[usp_CreateUserItemTrack]
	-- Add the parameters for the stored procedure here
	@user_id INT,
	@item_id INT
AS
BEGIN
	-- SET NOCOUNT ON added to prevent extra result sets from
	-- interfering with SELECT statements.
	SET NOCOUNT ON;



   
   --making sure all values are filled out
	IF NOT EXISTS (SELECT 1 FROM dbo.UserItemTracking AS uit 
						WHERE uit.u_id = @user_id
							AND uit.i_id = @item_id
					)
		INSERT INTO dbo.UserItemTracking (
		                                     u_id
		                                   , i_id
		                                 )
		VALUES ( @user_id -- u_id - int
		       , @item_id -- i_id - int
		    )


END

GO
GRANT EXECUTE ON  [dbo].[usp_CreateUserItemTrack] TO [python_dev]
GO

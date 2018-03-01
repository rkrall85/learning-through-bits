SET QUOTED_IDENTIFIER ON
GO
SET ANSI_NULLS ON
GO
-- =============================================
-- Author:		Robert Krall
-- Create date: 2/28/2017
-- Description:	This sp will check to see if a user is in the db.
-- =============================================
CREATE PROCEDURE [dbo].[usp_GetUser]
	-- Add the parameters for the stored procedure here
	@user_name VARCHAR(50),
	@user_id INT OUTPUT,
	@first_name VARCHAR(50) OUTput, 
	@last_name VARCHAR(50) OUTput, 
	@email VARCHAR(50) OUTPUT,
	@message VARCHAR(50) output
AS
BEGIN
	-- SET NOCOUNT ON added to prevent extra result sets from
	-- interfering with SELECT statements.
	SET NOCOUNT ON;

   
   IF (SELECT COUNT(*) 
		FROM dbo.[User] AS p
		WHERE p.u_name = @user_name
		)=1
		SELECT @user_id = u_id ,
				@first_name= f_name,
				@last_name = l_name,
				@email = email,
				@message = 'Success'  
		FROM dbo.[User] AS p
		WHERE p.u_name = @user_name
	ELSE 
		SELECT @user_id = 0 , 
				@first_name= NULL,
				@last_name = NULL,
				@email = NULL,
				@message = 'Could not find user'
		
END
GO
GRANT VIEW DEFINITION ON  [dbo].[usp_GetUser] TO [python_dev]
GO
GRANT EXECUTE ON  [dbo].[usp_GetUser] TO [python_dev]
GO

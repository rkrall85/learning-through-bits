SET QUOTED_IDENTIFIER ON
GO
SET ANSI_NULLS ON
GO
-- =============================================
-- Author:		Robert Krall
-- Create date: 2/28/2017
-- Description:	This sp will create a new person in the db.
-- =============================================
CREATE PROCEDURE [dbo].[usp_CreateUser]
	-- Add the parameters for the stored procedure here
	@first_name VARCHAR(50),
	@last_name VARCHAR(50),
	@user_name VARCHAR(50),
	@email VARCHAR(50),
	@user_id INT OUTPUT,
	@message VARCHAR(50) output
AS
BEGIN
	-- SET NOCOUNT ON added to prevent extra result sets from
	-- interfering with SELECT statements.
	SET NOCOUNT ON;

   
   --making sure all values are filled out
   IF	(	@first_name IS NULL
			AND @last_name IS NULL
			AND @user_name IS NULL
			AND @email IS NULL
		)
		SELECT @user_id = 0, @message ='You need to enter all fields'	
	ELSE
		IF NOT EXISTS (SELECT 1 FROM dbo.[User] WHERE [User].u_name= @user_name)
			begin
				INSERT INTO dbo.[User] (
									f_name
									, l_name
									, u_name
									, email
								)
				VALUES ( @first_name -- f_name - varchar(50)
						, @last_name -- l_name - varchar(50)
						, @user_name -- u_name - varchar(50)
						, @email -- email - varchar(200)
						)
				
				SELECT @user_id = @@IDENTITY, @message = 'Success'
			END
         ELSE 
			IF EXISTS (SELECT 1 FROM dbo.[User] WHERE [User].u_name= @user_name)
				begin
					SELECT @user_id = u.u_id , @message = 'Success' 
					FROM dbo.[User] AS u WHERE u.u_name= @user_name
				end
			ELSE 
				BEGIN 
					SELECT @user_id = 0, @message = 'Failure'
				END 
				   
		
END
GO

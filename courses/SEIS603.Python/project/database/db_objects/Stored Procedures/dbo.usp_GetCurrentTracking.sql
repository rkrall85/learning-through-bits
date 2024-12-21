SET QUOTED_IDENTIFIER ON
GO
SET ANSI_NULLS ON
GO
-- =============================================
-- Author:		Robert Krall
-- Create date: 3/9/2018
-- Description:	Show current items tracked by person
-- =============================================
create PROCEDURE [dbo].[usp_GetCurrentTracking]
	-- Add the parameters for the stored procedure here
	@user_id int
AS
BEGIN
	-- SET NOCOUNT ON added to prevent extra result sets from
	-- interfering with SELECT statements.
	SET NOCOUNT ON;
	
	SELECT i.i_id
		 , i.i_name
	FROM dbo.UserItemTracking AS uit
	INNER JOIN dbo.Item AS i ON uit.i_id = i.i_id
	WHERE uit.u_id = @user_id

END
GO

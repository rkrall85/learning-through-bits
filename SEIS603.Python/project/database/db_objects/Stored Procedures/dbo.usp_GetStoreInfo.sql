SET QUOTED_IDENTIFIER ON
GO
SET ANSI_NULLS ON
GO
-- =============================================
-- Author:		Robert Krall
-- Create date: 03/01/2018
-- Description:	Get the store name and info
-- =============================================
CREATE PROCEDURE [dbo].[usp_GetStoreInfo]
	-- Add the parameters for the stored procedure here
	@s_id int
AS
BEGIN
	-- SET NOCOUNT ON added to prevent extra result sets from
	-- interfering with SELECT statements.
	SET NOCOUNT ON;

    -- Insert statements for procedure here
	SELECT s_name
	FROM dbo.Store AS s
	WHERE s.s_id = @s_id;
END
GO

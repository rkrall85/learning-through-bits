SET QUOTED_IDENTIFIER ON
GO
SET ANSI_NULLS ON
GO
-- =============================================
-- Author:		Robert Krall
-- Create date: 03/01/2018
-- Description:	Get a store listing
-- =============================================
CREATE PROCEDURE [dbo].[usp_GetSupportedStores]
	-- Add the parameters for the stored procedure here
AS
BEGIN
	-- SET NOCOUNT ON added to prevent extra result sets from
	-- interfering with SELECT statements.
	SET NOCOUNT ON;

	SELECT s.s_id
         , s.s_name 
	FROM dbo.Store AS s


END
GO

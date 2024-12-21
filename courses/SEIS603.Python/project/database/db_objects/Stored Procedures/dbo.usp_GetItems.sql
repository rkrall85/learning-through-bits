SET QUOTED_IDENTIFIER ON
GO
SET ANSI_NULLS ON
GO
-- =============================================
-- Author:		Robert Krall
-- Create date: 03/01/2018
-- Description:	Get a list of all items
-- =============================================
CREATE PROCEDURE [dbo].[usp_GetItems]
	-- Add the parameters for the stored procedure here
AS
BEGIN
	-- SET NOCOUNT ON added to prevent extra result sets from
	-- interfering with SELECT statements.
	SET NOCOUNT ON;

    -- Insert statements for procedure here
	SELECT i.i_id
         , i.i_brand
         , i.i_name
         , i.i_model
         , i.i_description
         , i.i_upc 
	FROM dbo.Item AS i

END
GO

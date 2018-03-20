SET QUOTED_IDENTIFIER ON
GO
SET ANSI_NULLS ON
GO
-- =============================================
-- Author:		Robert Krall
-- Create date: 03/02/2018
-- Description:	Get all valid store items to grab the price.
-- =============================================
create PROCEDURE [dbo].[usp_GetMissingStoreItems]
-- Add the parameters for the stored procedure here
	@item_id INT = 0
AS
    BEGIN
  

        -- SET NOCOUNT ON added to prevent extra result sets from
        -- interfering with SELECT statements.
        --SET NOCOUNT ON;
	WITH current_items 
			AS(
				SELECT     s.s_id
				FROM       dbo.Store AS s
				INNER JOIN dbo.StoreItem	AS si ON s.s_id = si.s_id
				INNER JOIN dbo.Item			AS i  ON si.i_id = i.i_id
				WHERE 1= 1 AND i.i_id = @item_id
			)
			SELECT s_id, s.s_name 
			FROM dbo.Store AS s
			WHERE s.enabled='y'
			AND s.s_id NOT IN (SELECT s_id FROM current_items)

				



    END;
GO

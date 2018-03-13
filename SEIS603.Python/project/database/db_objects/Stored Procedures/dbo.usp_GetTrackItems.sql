SET QUOTED_IDENTIFIER ON
GO
SET ANSI_NULLS ON
GO
-- =============================================
-- Author:		Robert Krall
-- Create date: 03/02/2018
-- Description:	Get all valid store items to grab the price.
-- =============================================
CREATE PROCEDURE [dbo].[usp_GetTrackItems]
-- Add the parameters for the stored procedure here
	@item_id int

AS
    BEGIN
        /*
	@item_id INT OUT, 
	@store_id INT OUT, 
	@item_url VARCHAR(500) out,
	@item_web_class VARCHAR(50) out,
	@web_scrap	CHAR(1) OUT
*/


        -- SET NOCOUNT ON added to prevent extra result sets from
        -- interfering with SELECT statements.
        --SET NOCOUNT ON;
	SELECT     i.i_id
				     , si.s_id
					 , si.i_url
					, si.i_div_class
					, si.i_span_class
					, s.web_scrap
			FROM       dbo.Item AS i
			INNER JOIN dbo.StoreItem AS si
	            ON i.i_id = si.i_id
		    INNER JOIN dbo.Store AS s
			    ON si.s_id = s.s_id
			WHERE s.enabled='y' ---grabbing only valid stores
			AND ISNULL(@item_id,0) = 
				CASE
					WHEN @item_id != 0 THEN @item_id 
					ELSE 0
				END

    END;
GO

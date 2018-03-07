SET QUOTED_IDENTIFIER ON
GO
SET ANSI_NULLS ON
GO
-- =============================================
-- Author:		Robert Krall
-- Create date: 03/02/2018
-- Description:	Insert new store item listing
-- =============================================
CREATE PROCEDURE [dbo].[usp_GetUserTrackItem]
	-- Add the parameters for the stored procedure here
	@u_id			int,
	@i_id			INT,
	@s_id			INT,
	@web_scrap_out	CHAR(1) OUTPUT,
	@item_url_out	VARCHAR(500) OUTPUT,
	@item_web_class_out VARCHAR(50) output
	
	--@message_out	VARCHAR(500) output

	


AS
BEGIN
	-- SET NOCOUNT ON added to prevent extra result sets from
	-- interfering with SELECT statements.
	--SET NOCOUNT ON;


    -- Insert statements for procedure here
	IF NOT EXISTS (	SELECT 1 
					FROM       dbo.Item AS i
					INNER JOIN dbo.StoreItem AS si	ON i.i_id = si.i_id
					INNER JOIN dbo.Store AS s		ON si.s_id = s.s_id
					INNER JOIN dbo.UserItemTracking AS uit
										ON i.i_id = uit.i_id
											AND s.s_id = uit.s_id
											AND si.i_id = uit.i_id
					WHERE uit.tracking_end_date <= GETDATE()	   
						AND uit.u_id = @u_id
						AND i.i_id = @i_id
						AND s.s_id = @s_id
						
						
		) 
		BEGIN 
			SELECT    -- i.i_id
					--, si.s_id
					--,
					@item_url_out = si.i_url
					, @item_web_class_out = si.i_web_class
					--, s.s_name
					,@web_scrap_out =  s.web_scrap
					--, uit.price AS UserPrice
		FROM       dbo.Item AS i
		INNER JOIN dbo.StoreItem AS si	ON i.i_id = si.i_id
		INNER JOIN dbo.Store AS s		ON si.s_id = s.s_id
		INNER JOIN dbo.UserItemTracking AS uit
										ON i.i_id = uit.i_id
											AND s.s_id = uit.s_id
											AND si.i_id = uit.i_id
		WHERE uit.tracking_end_date <= GETDATE()	   
			AND uit.u_id = @u_id
			AND s.s_id = @s_id
			AND i.i_id = @i_id
			;
		END 
	
        

END
GO

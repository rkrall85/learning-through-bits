SET QUOTED_IDENTIFIER ON
GO
SET ANSI_NULLS ON
GO
-- =============================================
-- Author:		Robert Krall
-- Create date: 03/02/2018
-- Description:	Insert new store item listing
-- =============================================
CREATE PROCEDURE [dbo].[usp_CreateStoreItem]
	-- Add the parameters for the stored procedure here
	@s_id			INT,
	@i_id			INT,
	@i_url			VARCHAR(500),
	@i_web_class	VARCHAR(50)
	--@message_out	VARCHAR(500) output

	


AS
BEGIN
	-- SET NOCOUNT ON added to prevent extra result sets from
	-- interfering with SELECT statements.
	--SET NOCOUNT ON;


    -- Insert statements for procedure here
	IF NOT EXISTS (	SELECT 1 
					FROM dbo.StoreItem AS si
					WHERE si.s_id = @s_id
						AND si.i_id =@i_id						
		) 
		BEGIN 
			INSERT INTO dbo.StoreItem (
	                              s_id
	                            , i_id
	                            , i_url
								, i_div_class
	                          )
			VALUES ( @s_id  -- s_id - int
				   , @i_id -- i_id - int
					, rtrim(LTRIM(@i_url)) -- i_url - varchar(500)
					, rtrim(LTRIM(@i_web_class))

				)
			;
			--SELECT @message_out = 'Successful'
		END 
	
        

END
GO

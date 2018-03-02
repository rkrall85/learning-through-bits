CREATE TABLE [dbo].[UserItemTracking]
(
[u_id] [int] NOT NULL,
[i_id] [int] NOT NULL,
[s_id] [int] NOT NULL,
[price] [decimal] (8, 2) NOT NULL,
[purchase_date] [date] NOT NULL,
[tracking_end_date] [date] NOT NULL
) ON [PRIMARY]
GO
ALTER TABLE [dbo].[UserItemTracking] ADD CONSTRAINT [PK_UserItemTracking] PRIMARY KEY CLUSTERED  ([u_id], [i_id], [s_id]) ON [PRIMARY]
GO
ALTER TABLE [dbo].[UserItemTracking] ADD CONSTRAINT [FK_UserItemTracking_Item] FOREIGN KEY ([i_id]) REFERENCES [dbo].[Item] ([i_id])
GO
ALTER TABLE [dbo].[UserItemTracking] ADD CONSTRAINT [FK_UserItemTracking_Store] FOREIGN KEY ([s_id]) REFERENCES [dbo].[Store] ([s_id])
GO
ALTER TABLE [dbo].[UserItemTracking] ADD CONSTRAINT [FK_UserItemTracking_User] FOREIGN KEY ([u_id]) REFERENCES [dbo].[User] ([u_id])
GO

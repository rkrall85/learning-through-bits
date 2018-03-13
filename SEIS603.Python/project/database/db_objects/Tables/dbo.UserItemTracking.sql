CREATE TABLE [dbo].[UserItemTracking]
(
[u_id] [int] NOT NULL,
[i_id] [int] NOT NULL
) ON [PRIMARY]
GO
ALTER TABLE [dbo].[UserItemTracking] ADD CONSTRAINT [PK_UserItemTracking_1] PRIMARY KEY CLUSTERED  ([u_id], [i_id]) ON [PRIMARY]
GO
ALTER TABLE [dbo].[UserItemTracking] ADD CONSTRAINT [FK_UserItemTracking_Item1] FOREIGN KEY ([i_id]) REFERENCES [dbo].[Item] ([i_id])
GO
ALTER TABLE [dbo].[UserItemTracking] ADD CONSTRAINT [FK_UserItemTracking_User1] FOREIGN KEY ([u_id]) REFERENCES [dbo].[User] ([u_id])
GO

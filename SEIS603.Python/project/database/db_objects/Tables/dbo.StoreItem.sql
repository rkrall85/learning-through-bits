CREATE TABLE [dbo].[StoreItem]
(
[s_id] [int] NOT NULL,
[i_id] [int] NOT NULL,
[i_url] [varchar] (500) COLLATE SQL_Latin1_General_CP1_CI_AS NULL
) ON [PRIMARY]
GO
ALTER TABLE [dbo].[StoreItem] ADD CONSTRAINT [PK_StoreItem] PRIMARY KEY CLUSTERED  ([s_id], [i_id]) ON [PRIMARY]
GO
ALTER TABLE [dbo].[StoreItem] ADD CONSTRAINT [FK_StoreItem_Item] FOREIGN KEY ([i_id]) REFERENCES [dbo].[Item] ([i_id])
GO
ALTER TABLE [dbo].[StoreItem] ADD CONSTRAINT [FK_StoreItem_Store] FOREIGN KEY ([s_id]) REFERENCES [dbo].[Store] ([s_id])
GO

CREATE TABLE [dbo].[StoreItem]
(
[i_id] [int] NOT NULL,
[s_id] [int] NOT NULL,
[i_url] [varchar] (500) COLLATE SQL_Latin1_General_CP1_CI_AS NULL,
[i_web_class] [varchar] (50) COLLATE SQL_Latin1_General_CP1_CI_AS NULL
) ON [PRIMARY]
GO
ALTER TABLE [dbo].[StoreItem] ADD CONSTRAINT [PK_StoreItem] PRIMARY KEY CLUSTERED  ([i_id], [s_id]) ON [PRIMARY]
GO
ALTER TABLE [dbo].[StoreItem] ADD CONSTRAINT [FK_StoreItem_Item] FOREIGN KEY ([i_id]) REFERENCES [dbo].[Item] ([i_id])
GO
ALTER TABLE [dbo].[StoreItem] ADD CONSTRAINT [FK_StoreItem_Store] FOREIGN KEY ([s_id]) REFERENCES [dbo].[Store] ([s_id])
GO

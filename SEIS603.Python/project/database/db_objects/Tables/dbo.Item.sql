CREATE TABLE [dbo].[Item]
(
[i_id] [int] NOT NULL IDENTITY(100, 1),
[i_name] [varchar] (50) COLLATE SQL_Latin1_General_CP1_CI_AS NOT NULL,
[i_description] [varchar] (50) COLLATE SQL_Latin1_General_CP1_CI_AS NOT NULL,
[i_upc] [varchar] (50) COLLATE SQL_Latin1_General_CP1_CI_AS NOT NULL
) ON [PRIMARY]
GO
ALTER TABLE [dbo].[Item] ADD CONSTRAINT [PK_Item] PRIMARY KEY CLUSTERED  ([i_id]) ON [PRIMARY]
GO
CREATE UNIQUE NONCLUSTERED INDEX [IX_Item_Name] ON [dbo].[Item] ([i_name]) ON [PRIMARY]
GO

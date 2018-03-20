CREATE TABLE [dbo].[Item]
(
[i_id] [int] NOT NULL IDENTITY(100, 1),
[i_brand] [varchar] (50) COLLATE SQL_Latin1_General_CP1_CI_AS NOT NULL,
[i_name] [varchar] (50) COLLATE SQL_Latin1_General_CP1_CI_AS NOT NULL,
[i_model] [int] NULL CONSTRAINT [DF_Item_i_model] DEFAULT ((0)),
[i_description] [varchar] (50) COLLATE SQL_Latin1_General_CP1_CI_AS NOT NULL,
[i_upc] [varchar] (50) COLLATE SQL_Latin1_General_CP1_CI_AS NOT NULL
) ON [PRIMARY]
GO
ALTER TABLE [dbo].[Item] ADD CONSTRAINT [PK_Item] PRIMARY KEY CLUSTERED  ([i_id]) ON [PRIMARY]
GO
CREATE UNIQUE NONCLUSTERED INDEX [IX_Item_Upc] ON [dbo].[Item] ([i_upc]) ON [PRIMARY]
GO

CREATE TABLE [dbo].[ItemPriceHistory]
(
[i_id] [int] NOT NULL,
[s_id] [int] NOT NULL,
[i_date] [date] NOT NULL,
[i_price] [decimal] (9, 2) NULL CONSTRAINT [DF_ItemPriceHistory_i_price] DEFAULT ((0))
) ON [PRIMARY]
GO
ALTER TABLE [dbo].[ItemPriceHistory] ADD CONSTRAINT [PK_ItemPriceHistory] PRIMARY KEY CLUSTERED  ([i_id], [s_id], [i_date]) ON [PRIMARY]
GO
ALTER TABLE [dbo].[ItemPriceHistory] ADD CONSTRAINT [FK_ItemPriceHistory_Item] FOREIGN KEY ([i_id]) REFERENCES [dbo].[Item] ([i_id])
GO
ALTER TABLE [dbo].[ItemPriceHistory] ADD CONSTRAINT [FK_ItemPriceHistory_Store] FOREIGN KEY ([s_id]) REFERENCES [dbo].[Store] ([s_id])
GO

CREATE TABLE [dbo].[Store]
(
[s_id] [int] NOT NULL IDENTITY(100, 1),
[s_name] [varchar] (50) COLLATE SQL_Latin1_General_CP1_CI_AS NOT NULL,
[web_scrap] [char] (1) COLLATE SQL_Latin1_General_CP1_CI_AS NOT NULL CONSTRAINT [DF_Store_web_scrap] DEFAULT ('n'),
[enabled] [char] (1) COLLATE SQL_Latin1_General_CP1_CI_AS NULL CONSTRAINT [DF_Store_enabled] DEFAULT ('n')
) ON [PRIMARY]
GO
ALTER TABLE [dbo].[Store] ADD CONSTRAINT [PK_Store] PRIMARY KEY CLUSTERED  ([s_id]) ON [PRIMARY]
GO

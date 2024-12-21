CREATE TABLE [dbo].[User]
(
[u_id] [int] NOT NULL IDENTITY(100, 1),
[f_name] [varchar] (50) COLLATE SQL_Latin1_General_CP1_CI_AS NULL,
[l_name] [varchar] (50) COLLATE SQL_Latin1_General_CP1_CI_AS NULL,
[u_name] [varchar] (50) COLLATE SQL_Latin1_General_CP1_CI_AS NOT NULL,
[email] [varchar] (200) COLLATE SQL_Latin1_General_CP1_CI_AS NOT NULL
) ON [PRIMARY]
GO
ALTER TABLE [dbo].[User] ADD CONSTRAINT [PK_Person_pid] PRIMARY KEY CLUSTERED  ([u_id]) ON [PRIMARY]
GO
ALTER TABLE [dbo].[User] ADD CONSTRAINT [UIX_Person_pname] UNIQUE NONCLUSTERED  ([u_name]) ON [PRIMARY]
GO
EXEC sp_addextendedproperty N'MS_Description', N'naming sure all user names are unique', 'SCHEMA', N'dbo', 'TABLE', N'User', 'CONSTRAINT', N'UIX_Person_pname'
GO

IF NOT EXISTS (SELECT * FROM master.dbo.syslogins WHERE loginname = N'python_dev')
CREATE LOGIN [python_dev] WITH PASSWORD = 'p@ssw0rd'
GO
CREATE USER [python_dev] FOR LOGIN [python_dev]
GO

/* ========================================== gerar o Banco de dados =============================================*/

USE [master]
GO

/****** Object:  Database [techcd]    Script Date: 12/20/2016 14:41:31 ******/
CREATE DATABASE [techcd] ON  PRIMARY 
( NAME = N'techcd_Data', FILENAME = N'C:\Program Files\Microsoft SQL Server\MSSQL10_50.MSSQLSERVER\MSSQL\DATA\techcd.MDF' , SIZE = 2921920KB , MAXSIZE = UNLIMITED, FILEGROWTH = 10%)
 LOG ON 
( NAME = N'techcd_Log', FILENAME = N'C:\Program Files\Microsoft SQL Server\MSSQL10_50.MSSQLSERVER\MSSQL\DATA\techcd.ldf' , SIZE = 136064KB , MAXSIZE = UNLIMITED, FILEGROWTH = 10%)
GO

ALTER DATABASE [techcd] SET COMPATIBILITY_LEVEL = 80
GO

IF (1 = FULLTEXTSERVICEPROPERTY('IsFullTextInstalled'))
begin
EXEC [techcd].[dbo].[sp_fulltext_database] @action = 'disable'
end
GO

ALTER DATABASE [techcd] SET ANSI_NULL_DEFAULT OFF 
GO

ALTER DATABASE [techcd] SET ANSI_NULLS OFF 
GO

ALTER DATABASE [techcd] SET ANSI_PADDING OFF 
GO

ALTER DATABASE [techcd] SET ANSI_WARNINGS OFF 
GO

ALTER DATABASE [techcd] SET ARITHABORT OFF 
GO

ALTER DATABASE [techcd] SET AUTO_CLOSE OFF 
GO

ALTER DATABASE [techcd] SET AUTO_CREATE_STATISTICS ON 
GO

ALTER DATABASE [techcd] SET AUTO_SHRINK OFF 
GO

ALTER DATABASE [techcd] SET AUTO_UPDATE_STATISTICS ON 
GO

ALTER DATABASE [techcd] SET CURSOR_CLOSE_ON_COMMIT OFF 
GO

ALTER DATABASE [techcd] SET CURSOR_DEFAULT  GLOBAL 
GO

ALTER DATABASE [techcd] SET CONCAT_NULL_YIELDS_NULL OFF 
GO

ALTER DATABASE [techcd] SET NUMERIC_ROUNDABORT OFF 
GO

ALTER DATABASE [techcd] SET QUOTED_IDENTIFIER OFF 
GO

ALTER DATABASE [techcd] SET RECURSIVE_TRIGGERS OFF 
GO

ALTER DATABASE [techcd] SET  DISABLE_BROKER 
GO

ALTER DATABASE [techcd] SET AUTO_UPDATE_STATISTICS_ASYNC OFF 
GO

ALTER DATABASE [techcd] SET DATE_CORRELATION_OPTIMIZATION OFF 
GO

ALTER DATABASE [techcd] SET TRUSTWORTHY OFF 
GO

ALTER DATABASE [techcd] SET ALLOW_SNAPSHOT_ISOLATION OFF 
GO

ALTER DATABASE [techcd] SET PARAMETERIZATION SIMPLE 
GO

ALTER DATABASE [techcd] SET READ_COMMITTED_SNAPSHOT OFF 
GO

ALTER DATABASE [techcd] SET HONOR_BROKER_PRIORITY OFF 
GO

ALTER DATABASE [techcd] SET  READ_WRITE 
GO

ALTER DATABASE [techcd] SET RECOVERY FULL 
GO

ALTER DATABASE [techcd] SET  MULTI_USER 
GO

ALTER DATABASE [techcd] SET PAGE_VERIFY NONE  
GO

ALTER DATABASE [techcd] SET DB_CHAINING OFF 
GO

/*====================================== cria a tabela de usuarios =================================================*/

USE [techcd]
GO

/****** Object:  Table [dbo].[USUARIOS]    Script Date: 12/20/2016 14:42:36 ******/
SET ANSI_NULLS ON
GO

SET QUOTED_IDENTIFIER ON
GO

SET ANSI_PADDING ON
GO

CREATE TABLE [dbo].[USUARIOS](
	[NOME_USER] [nvarchar](30) NOT NULL,
	[SENHA_USER] [nvarchar](10) NULL,
	[COD_NIV] [bigint] NOT NULL,
	[IP_HOST] [char](13) NULL,
	[APELIDO_USER] [char](20) NULL,
	[COD_GRUPO] [bigint] NULL,
	[APELIDO_SKYPE] [nchar](40) NULL,
 CONSTRAINT [PK_USUARIOS] PRIMARY KEY CLUSTERED 
(
	[NOME_USER] ASC
)WITH (PAD_INDEX  = OFF, STATISTICS_NORECOMPUTE  = OFF, IGNORE_DUP_KEY = OFF, ALLOW_ROW_LOCKS  = ON, ALLOW_PAGE_LOCKS  = ON, FILLFACTOR = 90) ON [PRIMARY]
) ON [PRIMARY]

GO

SET ANSI_PADDING OFF
GO

ALTER TABLE [dbo].[USUARIOS]  WITH CHECK ADD  CONSTRAINT [FK_USUARIOS_NIVEIS] FOREIGN KEY([COD_NIV])
REFERENCES [dbo].[NIVEIS] ([COD_NIV])
ON UPDATE CASCADE
ON DELETE CASCADE
GO

ALTER TABLE [dbo].[USUARIOS] CHECK CONSTRAINT [FK_USUARIOS_NIVEIS]
GO

/*================================== cria o tabela de grupos de usuario ==========================================*/
USE [techcd]
GO

/****** Object:  Table [dbo].[GRUPO_USUARIOS]    Script Date: 12/20/2016 14:46:20 ******/
SET ANSI_NULLS ON
GO

SET QUOTED_IDENTIFIER ON
GO

SET ANSI_PADDING ON
GO

CREATE TABLE [dbo].[GRUPO_USUARIOS](
	[cod_grupo] [bigint] NULL,
	[desc_grupo] [char](20) NULL
) ON [PRIMARY]

GO

SET ANSI_PADDING OFF
GO


/*======================================================== insert do grupo =======================*/
INSERT INTO [techcd].[dbo].[GRUPO_USUARIOS]
           ([cod_grupo]
           ,[desc_grupo])
     VALUES
           (1, 'SISTEMAS')
GO

/*======================================================== insert do USUARIO =======================*/

INSERT INTO [techcd].[dbo].[USUARIOS]
           ([NOME_USER]
           ,[SENHA_USER]
           ,[COD_NIV]
           ,[IP_HOST]
           ,[APELIDO_USER]
           ,[COD_GRUPO]
           ,[APELIDO_SKYPE])
     VALUES
           ('thiagooliveira', 'mmnhbn', 
           '192.168.0.14',
           'thiago', 1 , 'oliveiravicente,net')
GO





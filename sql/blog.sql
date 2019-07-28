-- phpMyAdmin SQL Dump
-- version 4.6.4
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: 2019-07-28 11:05:56
-- 服务器版本： 5.7.14
-- PHP Version: 5.6.25

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `blog`
--

-- --------------------------------------------------------

--
-- 表的结构 `article`
--

CREATE TABLE `article` (
  `id` int(10) NOT NULL COMMENT '文章id',
  `user_id` int(10) NOT NULL COMMENT '操作该文章的用户id',
  `class_id` int(10) NOT NULL COMMENT '该文章的分类id',
  `label_id` int(10) NOT NULL COMMENT '标签id',
  `title` varchar(128) COLLATE utf8_unicode_ci NOT NULL COMMENT '文章标题',
  `content` text COLLATE utf8_unicode_ci NOT NULL COMMENT '文章内容',
  `status` int(2) NOT NULL DEFAULT '0' COMMENT '0待修改，1已发表，2已删除，3隐藏',
  `read` int(10) NOT NULL DEFAULT '0' COMMENT '文章阅读量',
  `create_time` datetime NOT NULL DEFAULT CURRENT_TIMESTAMP COMMENT '创建时间',
  `update_time` datetime NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP COMMENT '更新时间'
) ENGINE=MyISAM DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci COMMENT='存储文章信息';

-- --------------------------------------------------------

--
-- 表的结构 `class`
--

CREATE TABLE `class` (
  `id` int(10) NOT NULL COMMENT '分类id',
  `name` varchar(64) COLLATE utf8_unicode_ci NOT NULL COMMENT '分类名称',
  `status` int(2) NOT NULL DEFAULT '0' COMMENT '0正常，1停用',
  `create_time` datetime NOT NULL DEFAULT CURRENT_TIMESTAMP COMMENT '创建时间',
  `update_time` datetime NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP COMMENT '更新时间'
) ENGINE=MyISAM DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci COMMENT='存储博客分类数据';

-- --------------------------------------------------------

--
-- 表的结构 `label`
--

CREATE TABLE `label` (
  `id` int(10) NOT NULL COMMENT '标签id',
  `name` varchar(64) COLLATE utf8_unicode_ci NOT NULL COMMENT '标签名',
  `status` int(2) NOT NULL DEFAULT '0' COMMENT '0正常，1停用',
  `create_time` datetime NOT NULL DEFAULT CURRENT_TIMESTAMP COMMENT '创建时间',
  `update_time` datetime NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP COMMENT '更新时间'
) ENGINE=MyISAM DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci COMMENT='存储标签信息';

-- --------------------------------------------------------

--
-- 表的结构 `user`
--

CREATE TABLE `user` (
  `id` int(10) NOT NULL COMMENT '用户id',
  `passwd` varchar(128) COLLATE utf8_unicode_ci NOT NULL COMMENT '用户密码',
  `name` varchar(64) COLLATE utf8_unicode_ci NOT NULL COMMENT '用户名',
  `email` varchar(128) COLLATE utf8_unicode_ci DEFAULT NULL COMMENT 'email',
  `phone` varchar(20) COLLATE utf8_unicode_ci NOT NULL COMMENT '用户电话',
  `status` int(2) NOT NULL DEFAULT '0' COMMENT '0正常，1注销，2冻结',
  `create_time` datetime NOT NULL DEFAULT CURRENT_TIMESTAMP COMMENT '创建时间',
  `update_time` datetime NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP COMMENT '更新时间'
) ENGINE=MyISAM DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci COMMENT='存储用户信息';

--
-- Indexes for dumped tables
--

--
-- Indexes for table `article`
--
ALTER TABLE `article`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `class`
--
ALTER TABLE `class`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `label`
--
ALTER TABLE `label`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `user`
--
ALTER TABLE `user`
  ADD PRIMARY KEY (`id`);

--
-- 在导出的表使用AUTO_INCREMENT
--

--
-- 使用表AUTO_INCREMENT `article`
--
ALTER TABLE `article`
  MODIFY `id` int(10) NOT NULL AUTO_INCREMENT COMMENT '文章id', AUTO_INCREMENT=20;
--
-- 使用表AUTO_INCREMENT `class`
--
ALTER TABLE `class`
  MODIFY `id` int(10) NOT NULL AUTO_INCREMENT COMMENT '分类id', AUTO_INCREMENT=2;
--
-- 使用表AUTO_INCREMENT `label`
--
ALTER TABLE `label`
  MODIFY `id` int(10) NOT NULL AUTO_INCREMENT COMMENT '标签id', AUTO_INCREMENT=2;
--
-- 使用表AUTO_INCREMENT `user`
--
ALTER TABLE `user`
  MODIFY `id` int(10) NOT NULL AUTO_INCREMENT COMMENT '用户id', AUTO_INCREMENT=26;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;

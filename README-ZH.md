
# PJIP

![Python](https://img.shields.io/badge/python-3.12%2B-blue)
![License](https://img.shields.io/badge/license-GPLv3-pink)
![Stars](https://img.shields.io/github/stars/Eystudio/PJIP?style=social)
![Last Update](https://img.shields.io/github/last-commit/Eystudio/PJIP)

[English Documentation](README.md) | [中文文档](README-ZH.md)

一个基于 `Python` 的极域课堂管理辅助工具。。

---

## 项目简介

`PJIP` 是一个使用 `Python` 编写的极域课堂管理辅助软件，提供杀死、挂起、密码解析等功能，并配备简洁直观的图形界面，方便用户快速操作极域进程。

## 功能特色

- **杀死极域**: 一键杀死正在运行的极域进程
- **挂起极域**: 挂起运行中的极域进程, 支持恢复
- **获取极域密码**: 尝试获取极域密码
- **界面友好**: 基于 `Pyside6` 构建, 操作简单直观

## 安装依赖

本项目基于 `Python 3.x` 运行。

在开始之前, 建议先准备好 `Python` 环境并克隆仓库: 
```bash
git clone https://github.com/Eystudio/PJIP.git
cd PJIP
```

如果你使用虚拟环境(推荐): 

```bash
python -m venv venv
source venv/bin/activate  # Windows 使用 venv\Scripts\activate
```

然后根据项目配置文件安装依赖: 

```bash
pip install .
```
如果你更习惯使用 requirements.txt, 也可以: 

```bash
pip install -r requirements.txt
```

## 开发者公告

来自开发者的话:

> 由于个人时间有限, 本项目将暂时进入维护模式, 后续更新将以不定期为主。
> 
> 同时, 在开发过程中 Python 与 PySide6 的诸多限制逐渐显现, 项目推进已基本停滞, 未来也不会再进行较大规模的功能更新。
> 
> 敬请期待基于全新语言 和 UI 框架打造的下一代极域管理工具。

## 贡献

欢迎提供建议或改进代码!
欢迎提交 Issue 或 Pull Request 来改进本项目。
如有建议或问题, 请联系作者或在 GitHub 上留言。

Copyright (C) 2025 Errorsia, Yusulif
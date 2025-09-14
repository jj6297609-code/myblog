# Django 博客系统

一个基于 **Django 框架** 开发的仿 CSDN 博客网站，支持用户注册登录、文章发布与搜索、评论互动以及个人资料管理。  

---

## ✨ 功能特性
- **博客首页**：展示所有博客文章，支持分页浏览  
- **用户系统**：用户注册、登录、退出功能  
- **文章管理**：用户可发布博客文章，支持富文本展示  
- **搜索功能**：支持按关键字搜索文章  
- **评论功能**：登录用户可对文章发表评论  
- **个人主页**：查看用户简介、所在地和个人网站  
- **资料编辑**：用户可修改自己的简介信息  

---

## 🛠 技术栈
- **后端**：Django 4.x  
- **数据库**：SQLite（可扩展为 MySQL/PostgreSQL）  
- **前端**：Bootstrap 5 + HTML + CSS + JavaScript  
- **其他**：Django 模板引擎、静态文件管理、表单验证  

---

## 📂 项目结构
```
myblog/
│
├── myblog/                # 项目配置文件
├── blog/                  # 博客应用（文章、评论相关）
├── blogauth/              # 用户与个人资料管理应用
├── templates/             # 模板文件
├── static/                # 静态资源
├── media/                 # 用户上传文件
├── manage.py              # Django 管理入口
└── requirements.txt       # 项目依赖
```

---

## 🚀 快速开始

### 1. 克隆项目
```bash
git clone https://github.com/jj6297609-code/myblog.git
cd myblog
```

### 2. 创建虚拟环境并安装依赖
```bash
python -m venv venv
source venv/bin/activate   # Linux / macOS
venv\Scripts\activate      # Windows

pip install -r requirements.txt
```

### 3. 数据库迁移
```bash
python manage.py makemigrations
python manage.py migrate
```

### 4. 创建超级用户（用于后台管理）
```bash
python manage.py createsuperuser
```

### 5. 启动项目
```bash
python manage.py runserver
```

打开浏览器访问 `http://127.0.0.1:8000/`

---

## 📸 页面展示
- 博客首页  
- 博客详情与评论区  
- 用户个人主页  
- 编辑个人资料  

（你可以补充几张截图）  

---

## 🔮 后续优化
- 支持文章标签与分类  
- 评论区支持楼中楼回复  
- 用户头像上传与展示  
- 部署到云服务器，支持公网访问  

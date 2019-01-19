# Django2博客网站

基于`python3.7`和`Django2.1`的博客。 
![Python](https://img.shields.io/badge/Python-3.x-519dd9.svg)
![Django](https://img.shields.io/badge/Django-2.x-519dd9.svg)

## 主要功能：
- 文章，分页，分类目录，标签的添加，删除。编辑采用ckeditor，支持图片上传。
- 简单的评论功能，评论采用富文本评论，支持评论数显示。
- 最热文章，今天热门，昨天热门，7天热门。
- 支持账户注册，登录，注册用户可评论博客。
- 支持数据库缓存。
- 前端模板采用bootstrap框架，响应式特性。
- 数据库采用MySQL。

## 安装
使用pip安装：  
`pip install -r requirements.txt`

## 运行
 修改`DjangoBlog/setting.py` 修改数据库配置，如下所示：

     DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.mysql',
            'NAME': 'mysite',
            'USER': 'root',
            'PASSWORD': 'password',
            'HOST': 'host',
            'PORT': 3306,
        }
    }

## 创建数据库
mysql数据库中执行:
```sql
CREATE DATABASE `mysite` /*!40100 DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci */;
```
 然后终端下执行:

    ./manage.py makemigrations
    ./manage.py migrate

## 创建缓存表
执行命令：```python manage.py createcachetable``` 创建缓存表。

## 创建超级用户
 终端下执行:

    ./manage.py createsuperuser
    
## 启动本地服务
进入项目根目录，执行命令：```python manage.py runserver```

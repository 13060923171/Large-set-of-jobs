# 首先先去创建自己的数据库

## 然后再去settings里面修改如下内容

```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'studentmanager',#这个数据库的名字
        'USER': 'root',#账户
        'PASSWORD': 'root'#密码
    }
}
```

修改完成后

再进入文件目录下面运行如下命令

```
python manage.py makemigrations
python manage.py migrate
```

导入好数据库之后，再去对应的数据表里面创建管理用户去到student表里

插入对应的数据即可

```mysql
insert into studentmanager.student(
	id,
    stu_id,
    username,
    password
    )
values(
	1,
    '1',
    'admin',
    'admin'
);
```

插入成功之后

![image-20210719215551869](https://cdn.jsdelivr.net/gh/13060923171/images@main/img/image-20210719215551869.png)

然后再运行该程序

python manage.py runserver

再登录网站

http://127.0.0.1:8000/student/logout/

![image-20210719215728892](https://cdn.jsdelivr.net/gh/13060923171/images@main/img/image-20210719215728892.png)

登录成功之后就是这样

![image-20210719215752828](https://cdn.jsdelivr.net/gh/13060923171/images@main/img/image-20210719215752828.png)

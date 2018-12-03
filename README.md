基于flask框架的一个生产就绪模板。



## 重要的话说三遍



### 强烈推荐使用flask，因为django版本升级迭代的太快，api调用给第三方库带来非常多的麻烦。



### 强烈推荐使用flask，因为django版本升级迭代的太快，api调用给第三方库带来非常多的麻烦。



### 强烈推荐使用flask，因为django版本升级迭代的太快，api调用给第三方库带来非常多的麻烦。





# 部署
使用了supervisor作为进程监控。



依赖安装命令：pip install -r reuqirement.txt即可把相关依赖装上，如果出现依赖无法安装



请自行[百度](www.baidu.com)解决



supervisor配置文件的名字：flask_project.conf



ubuntu下，请使用```ln -s /root/flask_project/conf/flask_project.conf /ect/supervisor/conf.d/flask_project.conf``` 



**注意**，其中**/root/flask_project/conf/flask_project.conf**替换成自己的配置文件的位置。



# 项目框架以及依赖



flask(主框架)

flask-mongoengine(orm)

flask-socketio(实时模块)



其他功能，请自行集成。
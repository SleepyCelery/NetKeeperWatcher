#  适用于中国医科大学校园网+TPLINK路由器的掉线自动重连脚本

##  docker部署（推荐）

将dockerfile中的ENV修改为您所在环境的值，然后将所有文件上传到服务器，使用docker build构建镜像，运行即可

##  Windows部署

将constants.py文件中的os.name.lower() == "nt"代码块下的内容修改为所在环境的值，然后运行daemon.py即可


FROM python:3.8

WORKDIR /usr/src/DormitoryNetWatcher

COPY requirements.txt ./
RUN pip config set global.index-url https://pypi.tuna.tsinghua.edu.cn/simple &&\
 pip install --no-cache-dir -r requirements.txt &&\
/bin/cp /usr/share/zoneinfo/Asia/Shanghai /etc/localtime &&\
echo 'Asia/Shanghai' >/etc/timezone &&\
wget https://nodejs.org/dist/v10.15.3/node-v10.15.3-linux-x64.tar.xz &&\
 mkdir -p /usr/local/lib/nodejs &&\
 tar -xvf node-v10.15.3-linux-x64.tar.xz -C /usr/local/lib/nodejs/ &&\
 ln -s /usr/local/lib/nodejs/node-v10.15.3-linux-x64/bin/node /usr/local/bin/node &&\
 ln -s /usr/local/lib/nodejs/node-v10.15.3-linux-x64/bin/npm /usr/local/bin/npm
WORKDIR /usr/src/DormitoryNetWatcher
COPY . .
ENV PYTHONPATH /usr/src/DormitoryNetWatcher
# 路由器IP地址，一般为192.168.1.1
ENV ROUTER_HOST 192.168.1.1
# 检测在线允许超时次数
ENV MAX_RETRY_TIMES 3
# 检测在线用域名
ENV TEST_DOMAIN https://www.baidu.com/
# 路由器管理用户名，默认一般为admin
ENV TPLINK_USERNAME admin
# 路由器管理密码
ENV TPLINK_PASSWORD xxxxx
# 宽带用户名，一般为edu+学号
ENV NETKEEPER_USERNAME eduxxxxxxxxxx
# 宽带密码，一般为身份证后八位或后六位
ENV NETKEEPER_PASSWORD xxxxxxxx
# BARK消息推送地址，苹果手机可安装BARK实现重连通知
ENV BARK_URL https://xxxx.xxx/

CMD [ "python", "daemon.py" ]
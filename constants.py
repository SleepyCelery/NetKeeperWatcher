import os

if os.name.lower() == 'nt':
    HOST = '192.168.1.1'
    MAX_RETRY_TIMES = 3
    TEST_DOMAIN = 'https://www.baidu.com/'
    tplink_username = 'admin'
    tplink_password = 'xxxxxxxx'
    netkeeper_username = 'eduxxxxxxxxxx'
    netkeeper_password = 'xxxxxxxx'
    bark_url = ""
else:
    HOST = os.environ['ROUTER_HOST']
    MAX_RETRY_TIMES = int(os.environ['MAX_RETRY_TIMES'])
    TEST_DOMAIN = os.environ['TEST_DOMAIN']
    tplink_username = os.environ['TPLINK_USERNAME']
    tplink_password = os.environ['TPLINK_PASSWORD']
    netkeeper_username = os.environ['NETKEEPER_USERNAME']
    netkeeper_password = os.environ['NETKEEPER_PASSWORD']
    bark_url = os.environ['BARK_URL']
headers = {
    'Accept': 'application/json, text/javascript, */*; q=0.01',
    'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6',
    'Connection': 'keep-alive',
    'Content-Type': 'application/json; charset=UTF-8',
    'Origin': f'http://{HOST}',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36 Edg/106.0.1370.52',
    'X-Requested-With': 'XMLHttpRequest'
}
redirect_url = "http://219.148.210.33:9090/?userip={userip}&wlanacname=BPSS_BRAS_247&nasip=219.148.255.73&usermac={usermac}"

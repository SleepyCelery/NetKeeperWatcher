import requests
from base64 import b64decode
from constants import redirect_url
from loguru import logger


def log_in(username, password, userip, usermac):
    redirecturl = redirect_url.format(userip=userip, usermac=usermac)
    logger.info(f"redirect-url: {redirecturl}")
    headers = {
        'Accept': '*/*',
        'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6',
        'Connection': 'keep-alive',
        'Cookies': redirecturl,
        'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
        'Origin': 'http://219.148.210.33:9090',
        'Referer': 'http://219.148.210.33:9090/web',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.5112.102 Safari/537.36 Edg/104.0.1293.70',
        'X-Requested-With': 'XMLHttpRequest',
    }

    data = {
        'web-auth-user': username,
        'web-auth-password': password,
        'remember-credentials': 'false',
        'redirect-url': redirecturl,
    }
    response = requests.post('http://219.148.210.33:9090/web/connect', headers=headers, data=data,
                             verify=False)
    log_info = response.json()
    if 'truncated' in list(log_info.keys()) and 'session' in list(log_info.keys()):
        context_base64 = log_info['session']['context']
        context = eval(b64decode(context_base64).decode())
        logger.success('Login Success!')
        for key in context.keys():
            logger.info(f"{key}: {context[key]}")
        return True
    else:
        logger.error('Login Failed!')
        return False

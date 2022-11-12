import requests
import tplink
import netkeeper
import time
from loguru import logger
from notification import send_notifications
from constants import MAX_RETRY_TIMES, TEST_DOMAIN, tplink_username, tplink_password, netkeeper_username, \
    netkeeper_password, bark_url


def relogin():
    stok = tplink.login(tplink_username, tplink_password)
    tplink.renew_dhcp(stok)
    logger.info('Renewing DHCP info, please wait 10 seconds...')
    time.sleep(10)
    ip, mac = tplink.get_ip_and_mac(stok)
    logger.info(f"IP Address: {ip}, MAC Address: {mac}")
    return netkeeper.log_in(username=netkeeper_username, password=netkeeper_password, userip=ip,
                            usermac=mac.replace("-", ':'))


def check_connection():
    try:
        response = requests.get(url=TEST_DOMAIN, timeout=5)
        if response.status_code == 200:
            return True
        return False
    except:
        return False


if __name__ == '__main__':
    retry_times = 0
    while True:
        if not check_connection():
            retry_times += 1
            logger.error(f'Connect to {TEST_DOMAIN} failed for {retry_times} time(s)!')
            if retry_times < MAX_RETRY_TIMES:
                continue
            logger.info(f'Connect to {TEST_DOMAIN} failed times exceed the max retry times, trying to reconnect...')
            if relogin():
                if bark_url:
                    send_notifications('检测到寝室网络波动，连接现已恢复！')
                logger.success('Push notification to Bark client success!')
                retry_times = 0
        else:
            retry_times = 0
        time.sleep(5)

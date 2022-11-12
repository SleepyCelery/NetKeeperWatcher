import requests
from constants import headers, HOST
import execjs
import re


def encrypt_pwd(pwd, param1, param2):
    ctx = execjs.compile("""
           function encrypt_pwd(a, b, c) {
                var e = "", f, g, h, k, l = 187, n = 187;
                g = a.length;
                h = b.length;
                k = c.length;
                f = g > h ? g : h;
                for (var p = 0; p < f; p++)
                    n = l = 187,
                    p >= g ? n = b.charCodeAt(p) : p >= h ? l = a.charCodeAt(p) : (l = a.charCodeAt(p),
                    n = b.charCodeAt(p)),
                    e += c.charAt((l ^ n) % k);
                return e
            }
    """)
    return ctx.call("encrypt_pwd", param1, pwd, param2)


def login(username, password):
    response = requests.get(f"http://{HOST}/../web-static/dynaform/class.js", headers=headers, verify=False)
    param1, param2 = re.findall(r'this.securityEncode\(a,"(.*?)","(.*?)"\)};', response.text)[0]

    json_data = {
        'method': 'do',
        'login': {
            'username': username,
            'password': encrypt_pwd(password, param1, param2)
        }
    }

    response = requests.post(f'http://{HOST}/', headers=headers, json=json_data, verify=False)
    return response.json()['stok']


def get_wan_status(stok):
    json_data = {
        'network': {
            'name': [
                'wan_status'
            ]
        },
        'method': 'get'
    }

    response = requests.post(f'http://{HOST}/stok={stok}/ds', headers=headers,
                             json=json_data, verify=False)
    info = response.json()['network']['wan_status']
    return info


def renew_dhcp(stok):
    json_data = {
        'network': {
            'change_wan_status': {
                'proto': 'dhcp',
                'operate': 'renew'
            }
        },
        'method': 'do'
    }

    response = requests.post(f'http://{HOST}/stok={stok}/ds', headers=headers,
                             json=json_data, verify=False)
    if response.json()['error_code'] == 0:
        return True
    return False


def get_wan_protocol(stok):
    json_data = {
        'protocol': {
            'name': 'wan'
        },
        'method': 'get'
    }

    response = requests.post(f'http://{HOST}/stok={stok}/ds',
                             headers=headers, json=json_data, verify=False)
    return response.json()['protocol']['wan']


def get_ip_and_mac(stok):
    ipaddr = get_wan_status(stok)['ipaddr']
    mac = get_wan_protocol(stok)['macaddr']
    return ipaddr, mac

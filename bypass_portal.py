from requests import post, Request, get
from json import dumps
from sys import stdin
import socket

# can only hit this domain from wifi
ACCESSIBLE_DOMAIN = "myelauwit.com"
PORT = 443

#thanks SO
def get_ip_address(accessible_domain: str=ACCESSIBLE_DOMAIN, port: int=PORT):
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.connect((accessible_domain, 80))

    return s.getsockname()[0]

ip = get_ip_address()
init_url_fmt = "https://myelauwit.com/register/register_options?nag_mac=d4:ae:52:c6:cd:92&mac_address=%s&orig_url=google.com"
host = "https://myelauwit.com/register/rest/registration/grant_guest_access"
payload = {"email": "lol@lol.com",
			"site": "55920ef28ceecd3f14317587",
			"mac_address": None,
			"ip_address": ip}


def get_cookie_str(url: str) -> str:
	r = get(url)
	c_id, cookie = r.cookies.items()[0]
	cookie_str = "%s=%s" % (c_id, cookie)

	return cookie_str


def get_headers(cookie: str) -> dict:
	return {'accept': 'application/json, text/plain, */*',
			 'accept-encoding': 'gzip, deflate',
			 'accept-language': 'en-US,en;q=0.8',
			 'connection': 'keep-alive',
			 'content-length': '121',
			 'content-type': 'application/json;charset=UTF-8',
			 'cookie': cookie,
			 'host': 'myelauwit.com',
			 'origin': 'https://myelauwit.com',
			 'user-agent': 'pee pee'}


def login(host: str, payload: dict, mac: str) -> Request:
	payload['mac_address'] = mac
	return  post(host, data=dumps(payload), headers=headers)


def is_success(request: Request) -> bool:
	if request.json()['success'] is True:
		print("Logged into wireless successfully")
		exit(0)

	else:
		print("Request failed.")
		print(request.status_code, r.content)
		exit(1)


if __name__ == "__main__":
	mac = stdin.readline().strip()
	print('IP', ip, '\nMAC', mac)
	cookie = get_cookie_str(init_url_fmt % mac)
	headers = get_headers(cookie)
	request = login(host, payload, mac)
	is_success(request)

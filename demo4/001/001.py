# coding: utf-8

import base64
import sys

reload(sys)
sys.setdefaultencoding('utf8')

coupon = {
	'id': '1993',
	'goods': '0001'
}

def gen_coupon(id, goods):
	coupon['id'] = id
	coupon['goods'] = goods
	raw = '/'.join([k + ':' + v for k, v in coupon.items()])
	raw_64 = base64.urlsafe_b64encode(raw.encode('utf-8'))
	c_code = raw_64.decode()
	return c_code


def save_coupon(c_code):
	with open('coupon.txt', 'a+') as file:
		file.write(c_code+'\n')


def show_coupon(c_code):
	print r'优惠码: %s' % (c_code)


def parse_coupon(c_code):
	print r'解析优惠码: %s' % (base64.urlsafe_b64decode(c_code.encode('utf-8')))


def gen_all():
	for i in range(10):
		c_code = gen_coupon(str(i), str(int(i/2)))
		save_coupon(c_code)


if __name__ == '__main__':
	gen_all()
	# show_coupon(gen_coupon(str(2), str(int(5))))
	# parse_coupon(r'Z29vZHM6NS9pZDoy')
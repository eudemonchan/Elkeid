#!/usr/bin/python

# python 2.7.3 only

import urllib2
import re

version_list = [
    r"3.2.0",
    r"3.5.0",
    r"3.8.0",
    r"3.11.0",
]


def find_all_childs(version_list, data):
    pkgs = [each[0] for each in re.findall(
        r'<a href="(linux-headers-(' + '|'.join(version_list) + ').*_(all|amd64).deb)" title="linux-headers', data)
    ]
    return pkgs


def download(url, filename):
    with open(filename, 'wb') as f:
        f.write(urllib2.urlopen(url).read())
        f.close()


ubuntu_kernel_header_url = "https://mirrors.nju.edu.cn/ubuntu-old-releases/ubuntu/pool/main/l/linux/"

page_info = urllib2.urlopen(ubuntu_kernel_header_url).read()
all_versions = find_all_childs(version_list, page_info)
for each in all_versions:
    download(ubuntu_kernel_header_url+each, each)
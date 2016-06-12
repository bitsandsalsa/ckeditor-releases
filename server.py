#!/usr/bin/env python
import argparse
import os
import SimpleHTTPServer
import SocketServer
import subprocess


MyHandler = SimpleHTTPServer.SimpleHTTPRequestHandler


def parse_args():
    desc = 'Web server to host modified CKEditor Web app'
    parser = argparse.ArgumentParser(description=desc, formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    parser.add_argument('-s', '--host', default='10.0.3.1', help='host address to server from')
    parser.add_argument('-p', '--port', default=8000, type=int, help='TCP port to serve from')
    parser.add_argument('www_dir', default='.', help='directory to serve from')
    return parser.parse_args()


def main(args):
    browser_cmd = ['xdg-open', 'http://{}:{}/myeditor'.format(args.host, args.port)]
    try:
        os.chdir(args.www_dir)
        svrd = SocketServer.TCPServer((args.host, args.port), MyHandler)
        subprocess.call(browser_cmd)
        print 'serving on {} out of "{}"'.format((args.host, args.port), args.www_dir)
        svrd.serve_forever()
    except OSError as e:
        print e
    except KeyboardInterrupt:
        print 'shutting down'
        svrd.shutdown()


if __name__ == '__main__':
    main(parse_args())

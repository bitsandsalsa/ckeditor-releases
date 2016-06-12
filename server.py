#!/usr/bin/env python
import argparse
import os.path
import SimpleHTTPServer
import SocketServer


MyHandler = SimpleHTTPServer.SimpleHTTPRequestHandler


def parse_args():
    desc = 'Web server to host modified CKEditor Web app'
    parser = argparse.ArgumentParser(description=desc, formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    parser.add_argument('-s', '--host', default='10.0.3.1', help='host address to server from')
    parser.add_argument('-p', '--port', default=8000, type=int, help='TCP port to serve from')
    parser.add_argument('www_dir', default='.', help='directory to serve from')
    return parser.parse_args()


def main(args):
    try:
        www_dir_abs = os.path.abspath(args.www_dir)
        os.chdir(www_dir_abs)
        svrd = SocketServer.TCPServer((args.host, args.port), MyHandler)
        print 'serving on {} out of "{}"'.format((args.host, args.port), www_dir_abs)
        svrd.serve_forever()
    except OSError as e:
        print e
    except KeyboardInterrupt:
        print 'shutting down'
        svrd.shutdown()


if __name__ == '__main__':
    main(parse_args())

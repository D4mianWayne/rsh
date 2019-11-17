import socket
import sys
from urllib.parse import quote_plus, urlencode
import json

def parse_for_file(shell, lhost, lport):
    with open("core/shell.json", 'r') as f:
        data = json.load(f)
        sh = data[shell][0]
        cmd = sh.replace("[IPADDR]", lhost)
        cmd = cmd.replace("[PORT]", lport)
        offset = cmd.find("'") + 1
        cmd = cmd[offset:-2]
    return cmd

def validatePort(port):
    """Validate port number entered"""
    try:
        if 1 < int(port) < 65536:
            return True
        else:
            return False
    except ValueError:
        return False


def urlEncode(cmd):
    """urlencodes the cmd provided"""
    try:
        return urlencode(cmd, quote_via=quote_plus)
    except Exception as error:
        print('[x] Error:"{}"'.format(error))
        sys.exit(0)


def validateIP(ip):
    """validate ip provided"""
    try:
        if socket.inet_aton(ip):
            return True
    except socket.error:
        return False


def colors(string, color):
    """Make things colorfull

    Arguments:
        string {str} -- String to apply colors on
        color {int} -- value of color to apply

    """
    print("\033[%sm%s\033[0m" % (color, string))

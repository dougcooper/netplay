from scapy.all import *
from scapy.utils import *
from scapy.layers.l2 import getmacbyip
import argparse
import time

class CustomHelpFormatter(argparse.HelpFormatter):
    def __init__(self, prog):
        super().__init__(prog, max_help_position=40, width=80)
                         
    def _format_action_invocation(self, action):
        if not action.option_strings or action.nargs == 0:
            return super()._format_action_invocation(action)
        default = self._get_default_metavar_for_optional(action)
        args_string = self._format_args(action, default)
        return ', '.join(action.option_strings) + ' ' + args_string

fmt = lambda prog: CustomHelpFormatter(prog)

parser = argparse.ArgumentParser("netplay",formatter_class=fmt)
parser.add_argument('-i','--interface',required=True, help="local interface name",metavar="<iface name>")
parser.add_argument('-d','--destination',required=True, help="destination ip address",metavar='<dest ip>')
parser.add_argument('-f', '--filename', required=True,help="pcap type file",metavar="<pcap file>")
args = parser.parse_args()

from_ip=get_if_addr(args.interface)
from_mac=get_if_hwaddr(args.interface)
to_ip=args.destination
to_mac=getmacbyip(args.destination)

info = {
    'from':
        {'ip': get_if_addr(args.interface),
        'mac': get_if_hwaddr(args.interface)
        },
    'to':{
        'ip': args.destination,
        'mac':getmacbyip(args.destination)
    }
}

print(info)

pkts = rdpcap(args.filename)

print("updating packets")

for pkt in pkts:
    pkt["Ether"].src= from_mac
    pkt["Ether"].dst= to_mac
    if "IP" not in pkt:
        continue
    p = pkt["IP"]
    p.src = from_ip
    p.dst = to_ip
    del(p.chksum)
    if "UDP" in pkt:
        del(pkt["UDP"].chksum)

print("sending packets")
sendpfast(pkts,realtime=True)
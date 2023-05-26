## example rewriting a pcap file with tcpreplay package utils

tcprewrite --infile=Radio126MuLaw.pcapng --outfile=temp1.pcap --dstipmap=0.0.0.0/0:172.5.5.201 --enet-dmac=08:00:27:90:0c:ec
tcprewrite --infile=temp1.pcap --outfile=temp2.pcap --srcipmap=0.0.0.0/0:172.5.5.161 --enet-smac=08:00:27:8e:40:3e
tcprewrite --infile=temp2.pcap --outfile=final.pcap --fixcsum
sudo tcpreplay --intf1=enp0s9 final.pcap

> https://www.xmodulo.com/how-to-capture-and-replay-network-traffic-on-linux.html

## do it on the fly with netplay

python -m netplay -i enp0s9 -d 172.5.5.201 -f Radio126MuLaw.pcapng

>https://stackoverflow.com/questions/8726881/sending-packets-from-pcap-with-changed-src-dst-in-scapy

## generate udp with gstreamer

gst-launch-1.0 audiotestsrc ! udpsink host=172.5.5.201 port=50010
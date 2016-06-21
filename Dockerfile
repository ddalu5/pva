# Added many RUN command so I can build from cache (very bad connection T_T)
FROM debian:8.5
MAINTAINER Salah Osfor <osfor.salah@gmail.com>
RUN apt-get update && apt-get install -y git
RUN apt-get install -y nbtscan nmap
RUN apt-get install -y tcpdump netcat hping3
RUN apt-get install -y ngrep Tcptrace tcpreplay
RUN apt-get install -y hydra john dsniff
RUN apt-get install -y python-pip
RUN pip install -U pip
RUN pip install impacket
RUN pip install https://github.com/guelfoweb/knock/archive/knock3.zip
RUN cd && mkdir Tools
RUN git clone https://github.com/sqlmapproject/sqlmap.git /root/Tools/sqlmap
RUN git clone https://github.com/Dionach/CMSmap.git /root/Tools/cmsmap
RUN git clone https://github.com/ShawnDEvans/smbmap.git /root/Tools/smbmap

# Added many RUN commands so I can build from cache (very bad connection T_T)
FROM debian:8.5
MAINTAINER Salah Osfor <osfor.salah@gmail.com>
RUN apt-get update && apt-get install -y git
RUN apt-get install -y nbtscan nmap
RUN apt-get install -y tcpdump netcat hping3
RUN apt-get install -y ngrep Tcptrace tcpreplay
RUN apt-get install -y hydra john dsniff
RUN apt-get install -y python-pip
RUN mkdir -p /root/daril/Tools/ && mkdir -p /root/daril/projects/pentests/
RUN git clone https://github.com/sqlmapproject/sqlmap.git /root/daril/Tools/sqlmap
RUN git clone https://github.com/Dionach/CMSmap.git /root/daril/Tools/cmsmap
RUN git clone https://github.com/ShawnDEvans/smbmap.git /root/daril/Tools/smbmap
RUN pip install -U pip
RUN pip install impacket
RUN pip install argparse
RUN pip install https://github.com/guelfoweb/knock/archive/knock3.zip
WORKDIR /root/daril
ADD ./pva pva
CMD ["bash"]

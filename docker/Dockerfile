FROM centos:centos7

# 设置时区为CST
ENV TZ="Asia/Shanghai"
# 设置编码
ENV LANG en_US.utf8

RUN yum -y install wget \
    && yum -y install setup \
    && yum -y install perl \
    && yum -y groupinstall "Development tools" \
    && yum -y install zlib-devel bzip2-devel openssl-devel ncurses-devel sqlite-devel readline-devel tk-devel gdbm-devel db4-devel libpcap-devel xz-devel libffi-devel zlib1g-dev \
    && yum install zlib* -y \
    && wget https://www.python.org/ftp/python/3.8.1/Python-3.8.1.tar.xz \
    && tar -xvJf Python-3.8.1.tar.xz \
    && mkdir /usr/local/python3 \
    && cd Python-3.8.1 \
    && ./configure --prefix=/usr/local/python3 --enable-optimizations --with-ssl \
    && make && make install \
    && ln -s /usr/local/python3/bin/python3 /usr/local/bin/python3 \
    && ln -s /usr/local/python3/bin/pip3 /usr/local/bin/pip3 \
    && pip3 install --upgrade pip \
    && echo "export PYTHONIOENCODING=utf-8" >> ~/.bashrc


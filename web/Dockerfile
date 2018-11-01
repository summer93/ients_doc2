FROM daocloud.io/python:3.6

# 维护者信息
MAINTAINER summer <mcdull9393@gmial.com>

RUN mkdir -p /ients_doc/web

ADD ./requirements.txt /ients_doc/web/requirements.txt

# app 所在目录
WORKDIR /ients_doc/web

# 安装 app 所需依赖
RUN pip install -r requirements.txt




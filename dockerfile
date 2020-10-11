# FROM postgres:9.5-alpine
FROM python


# This hack is widely applied to avoid python printing issues in docker containers.
# See: https://github.com/Docker-Hub-frolvlad/docker-alpine-python3/pull/13
# ENV PYTHONUNBUFFERED=1

# RUN echo "**** install Python ****" && \
#     apk add --no-cache python3 && \
#     apk add python3-dev && \
#     apk add libffi && \
#     apk add libffi-dev &&  \
#     if [ ! -e /usr/bin/python ]; then ln -sf python3 /usr/bin/python ; fi && \
#     \
#     echo "**** install pip ****" && \
#     python3 -m ensurepip && \
#     rm -r /usr/lib/python*/ensurepip && \
#     pip3 install --no-cache --upgrade pip setuptools wheel && \
#     if [ ! -e /usr/bin/pip ]; then ln -s pip3 /usr/bin/pip ; fi

# RUN apk add zlib zlib-dev 
# RUN apk add libjpeg-turbo libjpeg-turbo-dev
# RUN python3 -m pip install --upgrade Pillow

# # Adds GCC
# RUN apk add build-base

COPY ./il2_stats /user/local/il2_stats
COPY ./fake_server_folder /user/local/fake_server_folder
WORKDIR /user/local/il2_stats/run

EXPOSE 8080
ENTRYPOINT [ "./install.sh" ]
FROM python

COPY ./il2_stats /user/local/il2_stats
WORKDIR /user/local/il2_stats/run

EXPOSE 8080
CMD [ "sh", "-c", "./install.sh && echo \"waitress...\" && ./waitress.sh" ]
# CMD [ "/bin/bash" ]
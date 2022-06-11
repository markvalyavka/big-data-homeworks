FROM cassandra:3.11

ENV LANG C.UTF-8

COPY ./cql_scripts/* /docker-entrypoint-initdb.d/

COPY entrypoint.sh /

RUN ["chmod", "+x", "/entrypoint.sh"]

# Override ENTRYPOINT, keep CMD
ENTRYPOINT ["/entrypoint.sh"]
CMD ["cassandra", "-f"]
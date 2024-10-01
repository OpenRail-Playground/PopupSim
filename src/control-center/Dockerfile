FROM db-inner-source-docker-release-local.bahnhub.tech.rz.db.de/nginx-spa:0.0.144@sha256:d6b942eb905f1daaed3522378a4749df740b80e1a29c9b9898fea7dc016aab08

HEALTHCHECK CMD /bin/true
COPY /dist /usr/share/nginx/html

EXPOSE 8080

# this is not the user the image is executed with
USER 10000

FROM teic/teidev-docker:latest

RUN mkdir /stylesheets &&\
    curl -Ls https://github.com/TEIC/Stylesheets/archive/refs/tags/v7.54.0.tar.gz |\
    tar --strip-components=1 -C /stylesheets -x -z -f -

COPY entrypoint.py /entrypoint.py

ENTRYPOINT ["/entrypoint.py"]

FROM teic/teidev-docker:latest

COPY entrypoint.py /entrypoint.py

ENTRYPOINT ["/entrypoint.py"]

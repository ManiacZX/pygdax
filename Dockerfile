FROM python:3-alpine

VOLUME ["/src", "/out"]

ENTRYPOINT ["python", "/src/main.py"]
FROM python:latest

COPY requirements.txt ./
RUN pip install -r ./requirements.txt && \
    apt-get update && \
    apt-get install -y locales && \
    apt-get install -y vim && \
    sed -i -e 's/# de_AT.UTF-8 UTF-8/de_AT.UTF-8 UTF-8/' /etc/locale.gen && \
    dpkg-reconfigure --frontend=noninteractive locales

ENV LANG de_AT.UTF-8
ENV LC_ALL de_AT.UTF-8

WORKDIR /usr/app/src

COPY . ./

EXPOSE 8000

ENTRYPOINT ["python3", "manage.py"]
CMD ["runserver", "0.0.0.0:8000"]

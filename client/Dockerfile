FROM python:3.8

RUN pip install --upgrade pip
RUN pip install pyzmq
RUN pip install pyinotify
RUN pip install pydicom

COPY client.py /

CMD [ "python", "./client.py" ]
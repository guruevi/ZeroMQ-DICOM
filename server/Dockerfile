FROM python:3.8

RUN pip install --upgrade pip
RUN pip install pyzmq
RUN pip install pyinotify

# Make directory watch
RUN mkdir /watch

# Export directory as volume
VOLUME /watch

# Expose port
EXPOSE 5555

COPY server.py /

CMD [ "python", "./server.py" ]
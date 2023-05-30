FROM python:3

#Copying files
RUN mkdir /the-app
COPY the-app the-app/
RUN chmod +x /the-app/start.sh

#Running
RUN pip install -r /the-app/requirements.txt
WORKDIR /the-app/
ENTRYPOINT [ "./start.sh" ]

EXPOSE 5000


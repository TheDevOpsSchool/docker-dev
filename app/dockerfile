FROM ubuntu:20.04

RUN apt-get update -y
RUN apt-get install python3 -y
RUN apt-get install python3-pip -y
RUN apt-get install git -y
# Set noninteractive mode
ENV DEBIAN_FRONTEND=noninteractive
RUN apt-get install cmatrix -y
RUN dpkg --add-architecture i386
RUN apt-get update -y
RUN apt-get install libwine -y 

# We had to comment this command below because we don't have the setup file.
# RUN wine PBIDesktopSetup.exe -y
# We had to comment out the command below because it was Unable to locate package daniel
# RUN apt install daniel -y

COPY . /app

WORKDIR /app

EXPOSE 8080

ENV PORT=8184

CMD ["python3", "server.py"]


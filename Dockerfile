FROM debian:latest
COPY . /app
RUN /app/ini.sh
CMD /app/run.sh

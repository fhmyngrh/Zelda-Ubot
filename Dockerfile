FROM mrismanaziz/man-userbot:buster

RUN git clone -b Zelda-Ubot https://github.com/fhmyngrh/Zelda-Ubot /home/zelda-ubot/ \
    && chmod 777 /home/Zelda-Ubot \
    && mkdir /home/Zelda-Ubot/bin/

COPY ./sample_config.env ./config.env* /home/zelda-ubot/

WORKDIR /home/zelda-ubot/

CMD ["python3", "-m", "userbot"]

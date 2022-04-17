FROM python:3.10.4-bullseye

RUN pip install --upgrade pip

WORKDIR /home/docker/code/app/

COPY . /home/docker/code/app/

RUN pip3 install -r requirements.txt

COPY . .

ENV ENV "ABC"

CMD [ "python3", "./get_api.py"]
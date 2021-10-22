FROM python:3.7

COPY requirements.txt .

RUN pip install -r requirements.txt
RUN pip install opencv-python-headless

ENV AGD_ROOT /agd
RUN mkdir $AGD_ROOT
WORKDIR /agd

COPY . .

ENTRYPOINT ["bash", "entrypoint.sh"]
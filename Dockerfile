FROM python:3.12
WORKDIR /
COPY src /src
COPY requirements.txt setup.py main.py /
RUN pip install -r requirements.txt
ENTRYPOINT python main.py

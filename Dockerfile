FROM python:3.9
WORKDIR /app
COPY requirements.txt .
RUN pip3 install -r requirements.txt
RUN dpkg-reconfigure locales
COPY . /app
CMD ["python3", "main.py"]


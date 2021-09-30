FROM python:3.9.7

WORKDIR /usr/src/app

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

CMD ["flask", "run", "-h", "0.0.0.0"]
EXPOSE 5000/tcp

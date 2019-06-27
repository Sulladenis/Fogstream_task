FROM python:3.7-alpine
RUN apk add --no-cache bash
WORKDIR /usr/src/app

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

CMD [ "./myscript" ]

FROM python:3
WORKDIR /usr/src/app
COPY ./calculator.py .
EXPOSE 7777
CMD ["python3", "./calculator.py", "127.0.0.1", "7777"]


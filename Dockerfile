FROM python:3-alpine
WORKDIR /usr/src/app/
COPY requirements.txt /usr/src/app/
RUN pip install --no-cache-dir -r /usr/src/app/requirements.txt
COPY . .
COPY serve.py /usr/src/app/
EXPOSE 5000
CMD ["python", "/usr/src/app/serve.py"]
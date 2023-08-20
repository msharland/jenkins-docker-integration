
FROM python:3.8-alpine3.18 as base
FROM base as builder
WORKDIR /app
COPY . /app
RUN pip install --no-cache-dir -r requirements.txt
EXPOSE 5000
CMD python ./app.py

#RUN mkdir /install
#WORKDIR /install
#COPY requirements.txt /requirements.txt
#RUN pip install --install-option="--prefix=/install" -r /requirements.txt
#FROM base
#COPY --from=builder /install /usr/local
#COPY src /app
#WORKDIR /app
#CMD ["gunicorn", "-w 4", "main:app"]

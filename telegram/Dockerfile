FROM python:3.8

RUN mkdir -p /usr/src/app/
WORKDIR /usr/src/app/

COPY . /usr/src/app/
RUN pip install --no-cache-dir vk_api
RUN pip install --no-cache-dir aiogram

CMD ["python", "telegram.py"]

FROM python:3.9.0

WORKDIR /home/

RUN echo 'mnbvcdserty'

RUN git clone https://github.com/surlyban-selor/kalrasu.git

WORKDIR /home/kalrasu/

RUN echo "SECRET_KEY=django-insecure-35(nb)&l9jlb%x88t=@)+^fb*2!enjth_)s5^j%u6j4e!f95lc" > .env

RUN pip install -r requirement.txt

RUN pip install gunicorn

RUN pip install mysqlclient

EXPOSE 8000

CMD ["bash", "-c", "python manage.py collectstatic --noinput --settings=kalrasu.settings.deploy && python manage.py migrate --settings=kalrasu.settings.deploy && gunicorn --env DJANGO_SETTINGS_MODULE=kalrasu.settings.deploy kalrasu.wsgi --bind 0.0.0.0:8000"]

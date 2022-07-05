FROM python:3.9.7-slim 
RUN pip install pip --upgrade 

RUN mkdir app
WORKDIR /app
COPY . /app
 
RUN pip install -r r.txt 


 

# RUN python3 manage.py migrate --noinput
# RUN python3 manage.py createsuperuser --email fb.gerami@gmail.com --noinput || true
# RUN python3 manage.py collectstatic --no-input 
EXPOSE 8000 

 
CMD ["gunicorn", "backend.wsgi:application","--bind","0.0.0.0:8000"]


#  gunicorn backend.wsgi:application --bind 0.0.0.0:7000


from python:3

WORKDIR /app

COPY loan_app /app/loan_app
COPY loanmanagement /app/loanmanagement
COPY manage.py /app/manage.py
COPY requirements.txt /app/requirements.txt

RUN pip install --no-cache-dir -r /app/requirements.txt
RUN python manage.py makemigrations
RUN python manage.py migrate
RUN python manage.py initadmin

EXPOSE 8000

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]

python3 manage.py makemigrations

python3 manage.py migrate --noinput

export PGPASSWORD=postgres
psql -h db -U postgres -d postgres -f /app/init.sql

python3 manage.py runserver 0.0.0.0:8000

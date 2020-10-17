#!/bin/bash

pip install -U virtualenv

cd ../
virtualenv .venv

.venv/bin/pip install -U wheel pip

.venv/bin/pip install -U -r requirements.txt

# read -p "Press any key to continue... "

cd src

../.venv/bin/python manage.py collectstatic --noinput
# read -p "Press any key to continue... "

echo "Starting Migrations..."
../.venv/bin/python manage.py migrate --noinput
# read -p "Press any key to continue... "
echo "Done."

echo "Starting Import CSV data..."
../.venv/bin/python manage.py import_csv_data
# read -p "Press any key to continue... "
echo "Done."

echo "Starting Creation of superuser..."
# ../.venv/bin/python manage.py createsuperuser
printf "from django.contrib.auth import get_user_model; User = get_user_model(); User.objects.create_superuser(username='admin', password='$ADMIN_PASSWORD', email='$ADMIN_EMAIL')" | ../.venv/bin/python manage.py shell

# read -p "Press any key to continue... "
echo "Done."

echo "Installation finished."

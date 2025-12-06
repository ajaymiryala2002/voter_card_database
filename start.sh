# #!/bin/bash
# python manage.py collectstatic --noinput
# python manage.py migrate --noinput
# gunicorn jango_voter_card.wsgi:application --bind 0.0.0.0:$PORT

#!/bin/bash

# Exit if any command fails
set -o errexit  

# Install dependencies
pip install -r requirements.txt

# Collect static files
python manage.py collectstatic --no-input

# Apply database migrations
python manage.py migrate

# Start server
gunicorn jango_voter_card.wsgi:application --bind 0.0.0.0:8000

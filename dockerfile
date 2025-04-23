#  Base image with Python
FROM python:3.12-slim

#  Install system-level dependencies (GDAL, PROJ, etc.)
RUN apt-get update && apt-get install -y \
    gdal-bin \
    libgdal-dev \
    binutils \
    libproj-dev \
    gcc \
    musl-dev \
    python3-dev \
    && rm -rf /var/lib/apt/lists/*

#  Set GDAL path so Django can find it
ENV GDAL_LIBRARY_PATH=/usr/lib/libgdal.so

#  Set working directory
WORKDIR /app

#  Copy project files
COPY . /app

#  Install dependencies
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

#  Collect static files (optional if you have static assets)
RUN python manage.py collectstatic --noinput

#  Start your Django app with gunicorn
CMD gunicorn CPSC471CalgaryGuidesystem.wsgi:application --bind 0.0.0.0:$PORT

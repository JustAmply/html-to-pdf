FROM python:3.9

# Install wkhtmltopdf
RUN apt-get update -y && \
    apt-get install -y wkhtmltopdf

# Create app directory
WORKDIR /usr/src/app

# Install app dependencies
COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

# Bundle app source
COPY . .

EXPOSE 5000
CMD [ "python", "./app.py" ]

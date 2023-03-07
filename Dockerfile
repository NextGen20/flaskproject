FROM python:3.8-slim-buster

# Create app directory
WORKDIR /app

# Install flask
COPY requirements.txt ./

RUN pip install --upgrade pip
RUN pip install -r requirements.txt

# Bundle app source
COPY . .

#port expose
EXPOSE 5000

#run with param
CMD ["python3.8", "app.py", "Bachar"]

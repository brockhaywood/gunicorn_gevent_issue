# gunicorn_gevent_issue

run the following in two terminals 

```
for ((i=1;i<=100;i++)); do   curl -v --header "Connection: keep-alive" "localhost:8000/date"; done
```

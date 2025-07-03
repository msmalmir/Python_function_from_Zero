# Python_function_from_Zero

[![Python application test with Github Actions](https://github.com/msmalmir/Python_function_from_Zero/actions/workflows/main.yml/badge.svg)](https://github.com/msmalmir/Python_function_from_Zero/actions/workflows/main.yml)


### To call Microservice 

something like this
```bash
curl -X 'POST' \
  'https://cuddly-guide-p5grqwjj69qf97gx-8000.app.github.dev/wiki' \
  -H 'accept: application/json' \
  -H 'Content-Type: application/json' \
  -d '{
  "name": "Facebook"
}'
```


### Build Container
`docker build .`
`docker image ls`


### Run container

somthing like this 
```
 docker run -p 127.0.0.1:8080:8080 03574d71644a
 ```

 ### Invoke POST request
run `invoke.sh`

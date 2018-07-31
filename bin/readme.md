# How to update docker repo

first login to an account that has access to the repo:

```
sudo docker login
```

In root directory for this project, where Dockerfile is:

```
sudo docker build -t gmpract .
sudo docker tag db757bf70f7a zdalihach/gmpract:alpha
sudo docker push zdalihach:gmpract
```

Once done, one can re-run the install script in gmpract/bin

```
sudo bash ./install.sh
```


# nno0obb-api

## # Local Dev

```
$ cd $(git rev-parse --show-toplevel)
$ python3 -m app.main
```

## # Deploy

```
$ fly deploy
```

## # Test

```
$ curl -L https://www.nno0obb.xyz/api/v1/ping
pong
```

# nno0obb-api

## # Local Dev

```
$ cd $(git rev-parse --show-toplevel)
$ python3 -m app.main
```

## # Deploy

### fly.io

```
$ fly deploy
$ fly status
$ curl -L https://nno0obb-api.fly.dev/api/ping
pong
```

### Cloudflare

```
$ wrangler deploy
$ wrangler deployments status
$ curl -L https://www.nno0obb.xyz/api/v1/ping
pong
```

## # Monitoring

* Cloudflare(Domain Dashboard) :: [nno0obb.xyz](https://dash.cloudflare.com/b5c8b42fab1271b4b31c32a7193ce9a7/nno0obb.xyz)
* Cloudflare(Domain Dashboard) :: [nno0obb-api.xyz](https://dash.cloudflare.com/b5c8b42fab1271b4b31c32a7193ce9a7/nno0obb-api.xyz)

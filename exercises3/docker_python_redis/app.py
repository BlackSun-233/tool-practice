import redis

# compose内部，直接用服务名redis做hostname
r = redis.Redis(host="redis", port=6379, decode_responses=True)

r.set("demo_key", "hello compose")
val = r.get("demo_key")
print(f"Redis读取结果: {val}")

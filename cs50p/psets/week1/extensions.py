fname = input("fname name: ").lower().strip().split(".")[-1]

image = ["png", "gif"]
application = ["zip", "pdf"]
plain = ["txt"]

if fname in plain:
    print("text/plain")
elif fname in application:
    print(f"application/{fname}")
elif fname == "jpg" or fname == "jpeg":
    print("image/jpeg")
elif fname in image:
    print(f"image/{fname}")
else:
    print("application/octet-stream")
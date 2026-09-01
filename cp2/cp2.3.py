status = {
    "/login": 200,
    "/usuarios": 404
}
print(
    "login" in status,
    200 in status,
    ("/login", 200) in status.items()
)
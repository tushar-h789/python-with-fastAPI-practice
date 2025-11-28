
async def app(scope, receive, send):
    assert scope["type"] == "http"

    try:
        await send({
            "type": "http.response.start",
            "status": 200,
            "headers": [
                [b"content-type", b"text-plain"]
            ]
        })
        await send({
            "type": "http.response.body",
            "body": b"<h1>Hello, World!</h1> <h2>This is a simple ASGI application.</h2>",
        })

    except:
        print("An error occurred while processing the request.")

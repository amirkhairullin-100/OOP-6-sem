from dataclasses import dataclass, field

@dataclass
class HttpRequest:
    method: str
    url: str
    headers: dict = field(default_factory=dict)
    body: str = ""
    timeout: int = 30

    def __str__(self):
        return (
            f"{self.method} {self.url}\n"
            f"Headers: {self.headers}\n"
            f"Body: {self.body[:50]}...\n"
            f"Timeout: {self.timeout}s"
        )

class HttpRequestBuilder:
    def __init__(self):
        self.reset()

    def reset(self):
        self._method = "GET"
        self._url = ""
        self._headers = {}
        self._body = ""
        self._timeout = 30
        return self

    def set_method(self, method: str):
        self._method = method.upper()
        return self

    def set_url(self, url: str):
        self._url = url
        return self

    def add_header(self, key: str, value: str):
        self._headers[key] = value
        return self

    def set_body(self, body: str):
        self._body = body
        return self

    def set_timeout(self, seconds: int):
        self._timeout = seconds
        return self

    def build(self):
        request = HttpRequest(
            method=self._method,
            url=self._url,
            headers=self._headers,
            body=self._body,
            timeout=self._timeout,
        )
        self.reset()
        return request

class Director:
    def __init__(self, builder: HttpRequestBuilder):
        self._builder = builder

    def build_json_post(self, url: str, data: dict):
        import json
        return (
            self._builder
                .set_method("POST")
                .set_url(url)
                .add_header("Content-Type", "application/json")
                .set_body(json.dumps(data))
                .build()
        )

    def build_auth_get(self, url: str, token: str):
        return (
            self._builder
                .set_method("GET")
                .set_url(url)
                .add_header("Authorization", f"Bearer {token}")
                .build()
        )

    def build_multipart_upload(self, url: str, filename: str):
    
        body_content = f"--boundary\r\nContent-Disposition: form-data; name=\"file\"; filename=\"{filename}\"\r\n\r\n<file content>\r\n--boundary--"
        return (
            self._builder
                .set_method("POST")
                .set_url(url)
                .add_header("Content-Type", "multipart/form-data; boundary=boundary")
                .set_body(body_content)
                .build()
        )

if __name__ == "__main__":
    builder = HttpRequestBuilder()
    director = Director(builder)

    request = director.build_json_post("https://api.example.com/orders", {"item": "book"})
    print(request)

    print("\n-----------------\n")

    request2 = director.build_auth_get("https://api.example.com/user", "your_token_here")
    print(request2)

    print("\n-----------------\n")

    request3 = director.build_multipart_upload("https://upload.example.com", "photo.jpg")
    print(request3)
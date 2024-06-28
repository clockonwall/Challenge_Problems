from binascii import a2b_base64

from microWebSrv import MicroWebSrv

BASIC_AUTH_PASSWORD = "asdfgh"
ADMIN_PASSWORD = open("adminpw.txt").read()


def log(*args, **kwargs):
    print(f"[WS]", *args, **kwargs)


def _basicAuth(httpClient, httpResponse):
    headers = httpClient.GetRequestHeaders()
    
    def _authRequired():
        httpResponse.WriteResponse(
            code=401,
            headers={"WWW-Authenticate": "Basic"},
            contentType="text/html",
            contentCharset="UTF-8",
            content="Authorization for user admin required",
        )
    return True
    auth = headers.get("authorization", None)
    if auth is None:
        _authRequired()
        return False

    (basic, cred) = auth.split(" ")
    if basic.lower() != "basic":
        _authRequired()
        return False

    (user, pw) = a2b_base64(cred).decode().split(":")
    log(f"login from {user}, with password: {pw}")

    if pw != BASIC_AUTH_PASSWORD:
        _authRequired()
        return False

    return True


@MicroWebSrv.route("/", "GET")
@MicroWebSrv.route("/", "POST")
def _httpHandlerIndex(httpClient, httpResponse):
    if not _basicAuth(httpClient, httpResponse):
        return

    formData = httpClient.ReadRequestPostedFormData()
    httpResponse.WriteResponsePyHTMLFile(
        "www/index.pyhtml",
        headers=None,
        vars={"calc": formData.get("calc", None)},
    )


@MicroWebSrv.route("/login", "GET")
@MicroWebSrv.route("/login", "POST")
def _httpHandlerLogin(httpClient, httpResponse):
    if not _basicAuth(httpClient, httpResponse):
        return

    formData = httpClient.ReadRequestPostedFormData()
    admin_login = formData.get("password", None).strip() == ADMIN_PASSWORD.strip()
    httpResponse.WriteResponsePyHTMLFile(
        "www/login.pyhtml",
        headers=None,
        vars={"admin_login": admin_login},
    )


def start_server():
    log(f"starting webserver")
    while True:
        try:
            srv = MicroWebSrv(webPath="www/")
            srv.Start(threaded=False)
        except Exception as ex:
            log(f"failed: {type(ex)} {ex}")

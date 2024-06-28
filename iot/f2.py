{{ py }}
  if calc is None:
    calc = "((1+2)*3-5) ** 12"
    calc_result = ""
  else:
    print(f"[CALC] running: {calc}")
    calc_result = eval(calc)
    print(f"[CALC] result: {calc_result}")
{{ end }}

<html>
    <head>
        <title>IoT Calculator</title>
        <meta charset="UTF-8"></meta>
    </head>
    <body>
        <h1>IoT Calculator</h1>
        <form action="/" method="post">
            <input
                name="calc"
                type="text"
                value="{{ calc }}">
            </input>
            <output name=result">
                {{ calc_result }}
            </output>
            <input value="Calculate" type="submit"></input>
          </form>
        <h1>Admin Login</h1>
        <form action="/login" method="post">
            <input
                name="password"
                type="text"
            </input>
            <input value="Login" type="submit"></input>
        </form>
    </body>
</html>

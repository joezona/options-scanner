# Options Scanner

aka Joe's money machine

## Setup

To configure the project locally, open up your terminal, navigate to the directory that contains this project:

```
cd /Users/you/some/folder/options-scanner
```

Then run the setup script. You will *only need to do this once*:

```
./setup.sh
```

This installs `uv`, a package manager for Python. There are other tools that do similar things, but this one is faster and easier to use. For more info on how this works, check out [the uv docs](https://docs.astral.sh/uv/getting-started/).

## Running the app

There are two ways to do this.

1. The most direct way is to run `uv run streamlit run app.py`. Normally you would just use the `streamlit` command line tool, but because Python uses virtual environments, this command is only installed in this specific project. We are managing it with `uv`, so that's why we use `uv run` as well. You might be thinking: isn't this a little convoluted? The answer is yes, and that's just how Python is. It's annoying but there are good reasons for it.

2. Run `./start.sh`. This is a script that just runs the "real" command so you don't need to remember it.

## Getting an API key

Log into the TastyTrade developer portal and create a new sandbox account. Register a new sandbox user with whatever username and password you want, then run this command from the terminal:

```
curl -X POST "https://api.cert.tastyworks.com/sessions" \
  -d '{ "login": "your_username", "password": "your_password_123" }' \
  -H 'Content-Type: application/json'
```

Use the sandbox account user, not your regular TastyTrade account. The response will look like:

```
{
    "data": {
            "user": {
                "email":"example@gmail.com",
                "external-id":"U108d52c1-9690-410c-881c-11044cb5890a",
                "is-confirmed":false,
                "username":"your_username"
                },
            "session-expiration":"2025-03-30T01:58:39.865Z",
            "session-token":"$COPY_THIS_VALUE"
            },
    "context":"/sessions"
}
```

The `session-token` is the value to use in the API key field in the app.

The app is still not working because the fields in the response are nonexistent, but it will return real data that can be manipulated and analyzed.

## Resources

- [TastyTrade API Workspace](https://www.postman.com/tastytradeapi/tastytrade-api/overview)
- [Instruments API](https://developer.tastytrade.com/open-api-spec/instruments/)
- [Pandas documentation](https://pandas.pydata.org/)
    - *The `df` variable is a DataFrame - this is the library that will let you work with it*

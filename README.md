# Simple SA-MP Query Bot

| Build Production CI | pre-commit checks |
| :---: | :---: |
|  [![Build Production](https://github.com/clemiee/samp-query-bot/actions/workflows/build.yml/badge.svg)](https://github.com/clemiee/samp-query-bot/actions/workflows/build.yml)|  [![pre-commit](https://github.com/clemiee/samp-query-bot/actions/workflows/pre-commit.yml/badge.svg)](https://github.com/clemiee/samp-query-bot/actions/workflows/pre-commit.yml)  |
-------------------------------------------------

A Simple SA-MP Server Query Discord bot made with [NAFF](https://github.com/Discord-Snake-Pit/NAFF).
Visit [the official guide](https://naff.readthedocs.io/Guides/01%20Getting%20Started/) to get started.

# Running the Application
There are multiple ways to launch the application.


### Python
To start the bot with python, you first need to install the required packages with `pip install -r requirements.txt`


Then, run:

1) `python main.py`


### Docker-Compose
You can use the pre-made docker-compose by running:

1) `docker-compose up`

### Docker
For most users, the use of `docker-compose` is highly recommended.

Nevertheless, you can import the pre-made Dockerfile into your own docker-compose or run it manually by with:

1) `docker build -t samp-query-bot .`
2) `docker run -it samp-query-bot`

Note: Make sure that you created a volume so that you local `./logs` folder gets populated.

# Additional Information
Additionally, this comes with a pre-made [pre-commit](https://pre-commit.com) config to keep your code clean.

It is recommended that you set this up by running:

1) `pip install pre-commit`
2) `pre-commit install`

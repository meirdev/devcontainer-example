# Dockerfile

FROM python:3.12-bullseye

RUN apt update -y

# Nice welcome message
RUN apt install fortune-mod cowsay lolcat -y
ENV PATH="$PATH:/usr/games"

# Powerful shell
RUN apt install zsh -y && \
    sh -c "$(wget -O- https://github.com/deluan/zsh-in-docker/releases/download/v1.1.5/zsh-in-docker.sh)"

# Poetry
RUN curl -sSL https://install.python-poetry.org | \
    POETRY_VIRTUALENVS_IN_PROJECT=true \
    POETRY_NO_INTERACTION=true \
    POETRY_HOME=/opt/poetry \
    python3 -
ENV PATH="$PATH:/opt/poetry/bin"

# Set welcome message
RUN printf "fortune | cowsay | lolcat\n\n" >> ~/.zshrc

ENTRYPOINT ["/bin/zsh"]

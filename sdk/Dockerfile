FROM python:alpine3.15

# -----------------------------------------------------------------------------
# Set default values for localhost
# Edge Server
ARG EXCHANGE_USER_ORG=myorg
ARG EXCHANGE_USER_ADMIN_PW=brTG3oiDgOfe8Pw0l7rQjnQhR626av
ARG EXCHANGE_ROOT_PW_BCRYPTED=eu87OeKZnZNQRaoZd7aL56wFZ3CtWU

# Edge Node
ARG EXCHANGE_ROOT_PW=eu87OeKZnZNQRaoZd7aL56wFZ3CtWU
ARG HZN_ORG_ID=myorg
ARG HZN_EXCHANGE_USER_AUTH=admin:brTG3oiDgOfe8Pw0l7rQjnQhR626av
ARG EXCHANGE_HUB_ADMIN_PW=ZtJwW2MkOp5AjFh8LXc3Gba0oBhc63
ARG EXCHANGE_SYSTEM_ADMIN_PW=9iQtDIZdkVokxqZVb6EVYZfjZvX7N7
ARG AGBOT_TOKEN=mmPABVhdU9WNDtWE32lcIF1pzX1Ai1
ARG EXCHANGE_USER_ADMIN_PW=brTG3oiDgOfe8Pw0l7rQjnQhR626av
ARG HZN_DEVICE_TOKEN=BwIivBeeuHFTX7CzBQUK9jGQd11Erm
# -----------------------------------------------------------------------------

ENV EXCHANGE_USER_ORG=$EXCHANGE_USER_ORG
ENV EXCHANGE_USER_ADMIN_PW=$EXCHANGE_USER_ADMIN_PW
ENV EXCHANGE_ROOT_PW_BCRYPTED=$EXCHANGE_ROOT_PW_BCRYPTED
ENV EXCHANGE_ROOT_PW=$EXCHANGE_ROOT_PW
ENV HZN_ORG_ID=$HZN_ORG_ID
ENV HZN_EXCHANGE_USER_AUTH=$HZN_EXCHANGE_USER_AUTH
ENV EXCHANGE_HUB_ADMIN_PW=$EXCHANGE_HUB_ADMIN_PW
ENV EXCHANGE_SYSTEM_ADMIN_PW=$EXCHANGE_SYSTEM_ADMIN_PW
ENV AGBOT_TOKEN=$AGBOT_TOKEN
ENV EXCHANGE_USER_ADMIN_PW=$EXCHANGE_USER_ADMIN_PW
ENV HZN_DEVICE_TOKEN=$HZN_DEVICE_TOKEN

RUN apk update && apk add gettext moreutils zip openssh-keygen docker openssl jq
RUN /usr/local/bin/python -m pip install --upgrade pip
RUN pip install gdown

COPY ./bin /bin/

# Copy available example stacks
COPY ./stacks /var/automationhub/stacks
COPY ./edgenode /var/automationhub/edgenode
COPY ./certificate_template /var/automationhub/
COPY ./firstrun.sh /var/automationhub/

# Setup environment variables
COPY ./node_env_template /var/automationhub/.env_node
COPY ./server_env_template /var/automationhub/.env_server
COPY ./deployment_env_template /var/automationhub/.env_deployment

# Setup volumes and docker-compose file
COPY ./volumes /var/automationhub/volumes
COPY ./docker-compose.yml /var/automationhub/

ENTRYPOINT [ "/bin/sh" ]
#!/bin/bash
openssl ecparam -genkey -name prime256v1 | openssl ec -out private.key
# openssl rsa -in private-pkcs8-key.key -aes256 -out private.key
openssl req -new -x509 -nodes -days 730 -key private.key -out public.crt -config openssl.conf
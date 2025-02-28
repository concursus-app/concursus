#!/bin/bash

APP="concursus"
PORT=39075

echo "Starting concursus on $PORT"

npm run build

export PORT=$PORT
export ORIGIN="https://concursus.arson.dev"

pm2 delete $APP
pm2 start build/index.js --name "$APP"
pm2 save

echo "We are up and running"

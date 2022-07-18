set -ev

ipfs daemon --init &

sleep 15

ipfs config --json API.HTTPHeaders.Access-Control-Allow-Origin '["*"]'
ipfs config --json API.HTTPHeaders.Access-Control-Allow-Methods '["GET", "PUT", "POST"]'

ipfs log tail

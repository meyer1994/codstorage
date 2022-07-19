set -ev

ipfs daemon --init &

sleep 15

ipfs config --json API.HTTPHeaders.Access-Control-Allow-Origin '["*"]'
ipfs config --json API.HTTPHeaders.Access-Control-Allow-Methods '["GET", "PUT", "POST"]'

ipfs config Addresses.API '/ip4/0.0.0.0/tcp/5001'
ipfs config Addresses.Gateway '/ip4/0.0.0.0/tcp/8080'

ipfs log tail

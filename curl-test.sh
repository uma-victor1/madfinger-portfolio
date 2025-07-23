#!/bin/bash

# run the post request to db
# record if success with $?, 
# print to screen success or error

postres=$(curl -f -s -o -X POST http://127.0.0.1:5000/api/timeline_post -d 'name=madfinger&email=umavictor11@gmail.com&content=Just added another portfolio site')

if [[ "$?" -eq 0 ]]; then
echo "Successfully posted to database"
else
echo "Failed to post timeline to db. Retry"
exit 1
fi

reqres=$(curl -f -s -o -X GET http://127.0.0.1:5000/api/timeline_post)

if [[ "$?" -eq 0 ]]; then
echo "Successfully retrieved timeline"
echo "$reqres"
else
echo "Failed to retreive timeline"
exit 1
fi

#! /bin/bash

for FILE in *.fa;
do
    if [ ! -s $FILE ]; then
	echo "$FILE is empty, removing"
	rm $FILE
    else
	echo "$FILE has content"
    fi
done

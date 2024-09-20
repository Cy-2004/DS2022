#!/bin/bash

wget https://s3.amazonaws.com/ds2002-resources/labs/lab3-bundle.tar.gz

tar -xzvf lab3-bundle.tar.gz

awk '!/^[[:space:]]*$/' lab3_data.tsv

tr '\t' ',' < lab3_data.tsv > lab3_data.csv

#cat lab3_data.csv

LINES=$(tail -n +2 lab3_data.csv | wc -l)

echo "There are $LINES lines remaining in the file"

tar -czvf converted-archive.tar.gz lab3_data.csv

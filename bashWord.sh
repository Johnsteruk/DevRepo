#!/usr/bin/env bash

# After setting the environment check that a parameter has been passed to the script.
if [ $# -eq 0 ] 
then
    echo "No arguments supplied"
fi

# Explanation of between pipes 
# 1. cat the file
# 2. Split the file into individual words
# 3. Force the words to uppercase (so Snowflake and snowflake are counted as 1 word
# 4. Sort the file alphabetically
# 5. Count the unique values
# 6. Sort the output by descending numbers to match question output
cat $1|grep -o -E '\w+'|tr [:lower:] [:upper:]|sort|uniq -c|sort -r

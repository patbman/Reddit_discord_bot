#!/bin/bash

#get shower thoughts titles
showerthoughtsdata=$(curl -s 'https://old.reddit.com/r/showerthoughts/.json' | jq '.data.children[].data')
thought=$(echo $showerthoughtsdata | jq '.title')


#thoughturl=$(echo $data | jq '.url')

#echo $data

eval 'for word in '$thought'; 
        do 
            echo $word >> thoughts.txt; 
    done'




tail -n +2 "thoughts.txt" > "thoughts.tmp" && mv "thoughts.tmp" "thoughts.txt";


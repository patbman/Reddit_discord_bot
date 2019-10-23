#!/bin/bash

#get shower thoughts titles
meirldata=$(curl -s 'https://old.reddit.com/r/me_irl/.json' | jq '.data.children[].data')
links=$(echo $meirldata | jq '.url')


#thoughturl=$(echo $data | jq '.url')

#echo $data

eval 'for word in '$links'; 
        do 
            echo $word >> meirl.txt; 
    done'




tail -n +2 "meirl.txt" > "meirl.tmp" && mv "meirl.tmp" "meirl.txt";


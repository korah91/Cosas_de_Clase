#!/bin/bash

BUFFETT="Life is like a snowball. The important thing is finding wet snow and a really long hill."

# write your code here
# Change1: replace the first occurrence of ‘snow’ with ‘foot’. 
# Change2: delete the second occurrence of ‘snow’. 
# Change3: replace ‘finding’ with ‘getting’. 
# Change4: delete all characters following ‘wet’. Tip: One way to implement 
# Change4, if to find the index of ‘w’ in the word ‘wet’ and then use substring extraction.

ISAY=${BUFFETT[@]/snow/foot}
ISAY=${ISAY[@]/snow/}
ISAY=${ISAY[@]//finding/getting}

wIndex=`expr index "$ISAY" 'w'`

echo $wIndex
ISAY=${ISAY:0:wIndex+2}



# Test code - do not modify

echo "Warren Buffett said:"
echo $BUFFETT
echo "and I say:"
echo $ISAY

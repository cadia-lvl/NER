#!/bin/bash


sed 's/\&/\&amp;/g' $2 > tmp
sed -i 's/</\&lt;/g' tmp
sed -i 's/>/\&gt;/g' tmp
sed -i 's/"/\&quot;/g' tmp
sed -i "s/'/\&apos;/g" tmp


python3 scripts/makeNAF.py tmp > tmp1
current_dir=$(pwd)
tmp1=$current_dir"/tmp1"
tmp2=$current_dir"/tmp2"
#echo $tmp1
cd ixa-pipe/nerc/
#head $tmp1
cat $tmp1 | java -jar target/ixa-pipe-nerc-2.0.0-exec.jar tag -m $current_dir/ixa-pipe/1000K.bin -o conll02 > $tmp2
cd - > /dev/null 2>&1
rm tmp1 tmp
awk '{print $1 "\t" $4}' tmp2 > tmp3
rm tmp2
sed -i 's/^[ \t]*//' tmp3
sed -i 's/B-Per$/B-Person/g' tmp3
sed -i 's/I-Per$/I-Person/g' tmp3
sed -i 's/B-Loc$/B-Location/g' tmp3
sed -i 's/I-Loc$/I-Location/g' tmp3
sed -i 's/I-Org$/I-Organization/g' tmp3
sed 's/B-Org$/B-Organization/g' tmp3 > output/ixa-pipe

#sed -i 's/\&amp;/\&/g' tmp3
#sed -i 's/\&lt;/</g' tmp3
#sed -i 's/\&gt;/>/g' tmp3
#sed -i 's/\&quot;/"/g' tmp3
#sed -i "s/\&apos;/'/g" tmp3

#cat tmp3
rm tmp3


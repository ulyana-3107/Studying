#1/bin/bash
if [ -f temp.txt ]
then
        $(rm temp.txt)
fi
touch temp.txt
numbers=$(cat "$1")
result=$(./pairs.sh $numbers)
for elem in $result
do
        echo -n "$elem " >> temp.txt
done
numbers2=$(cat temp.txt)
result2=$(./seq_to_calc_fib.sh $numbers2)
if [ -f "$2" ]
then
        $(rm "$2")
fi
for elem in $result2
do
        echo -n "$elem " >> $2
done

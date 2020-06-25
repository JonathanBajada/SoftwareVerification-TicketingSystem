#!/bin/sh

#This script runs the tix program (main.py python script) with a text file as user input


#Testing login function
loginTests=$(find ./Tests/inputs/login -type f -name "*.tti" | sort --version-sort)
for i in $loginTests
do
    name="${i##*/}" #Get name from path
    base="${name%.*}"   #Get test name from filename
    acc=$(find ./Tests/inputs -type f -name "$base.tai")    #Get corresponding account file
    event=$(find ./Tests/inputs -type f -name "$base.tei")  #Get corresponding event file
    transaction="/Tests/outputs/$base.adt"  #Set path to output transaction file with test name
    echo "Running test: $base"
    python3 main.py $acc $event $transaction < $i > ./Tests/outputs/$base.ato   #Run test and write terminal output to file
done

#Testing logout function
logoutTests=$(find ./Tests/inputs/logout -type f -name "*.tti" | sort --version-sort)
for i in $logoutTests
do
    name="${i##*/}"
    base="${name%.*}"
    acc=$(find ./Tests/inputs -type f -name "$base.tai")
    event=$(find ./Tests/inputs -type f -name "$base.tei")
    transaction="/Tests/outputs/$base.adt"
    echo "Running test: $base"
    python3 main.py $acc $event $transaction < $i > ./Tests/outputs/$base.ato
done

#Testing add credit function
creditTests=$(find ./Tests/inputs/addCredit -type f -name "*.tti" | sort --version-sort)
for i in $creditTests
do
    name="${i##*/}"
    base="${name%.*}"
    acc=$(find ./Tests/inputs -type f -name "$base.tai")
    event=$(find ./Tests/inputs -type f -name "$base.tei")
    transaction="/Tests/outputs/$base.adt"
    echo "Running test: $base"
    python3 main.py $acc $event $transaction < $i > ./Tests/outputs/$base.ato
done

#Testing create account function
createTests=$(find ./Tests/inputs/create -type f -name "*.tti" | sort --version-sort)
for i in $createTests
do
    name="${i##*/}"
    base="${name%.*}"
    acc=$(find ./Tests/inputs -type f -name "$base.tai")
    event=$(find ./Tests/inputs -type f -name "$base.tei")
    transaction="/Tests/outputs/$base.adt"
    echo "Running test: $base"
    python3 main.py $acc $event $transaction < $i > ./Tests/outputs/$base.ato
done

#Testing delete account function
deleteTests=$(find ./Tests/inputs/delete -type f -name "*.tti" | sort --version-sort)
for i in $deleteTests
do
    name="${i##*/}"
    base="${name%.*}"
    acc=$(find ./Tests/inputs -type f -name "$base.tai")
    event=$(find ./Tests/inputs -type f -name "$base.tei")
    transaction="/Tests/outputs/$base.adt"
    echo "Running test: $base"
    python3 main.py $acc $event $transaction < $i > ./Tests/outputs/$base.ato
done

#Testing buy ticket function
buyTests=$(find ./Tests/inputs/buy -type f -name "*.tti" | sort --version-sort)
for i in $buyTests
do
    name="${i##*/}"
    base="${name%.*}"
    acc=$(find ./Tests/inputs -type f -name "$base.tai")
    event=$(find ./Tests/inputs -type f -name "$base.tei")
    transaction="/Tests/outputs/$base.adt"
    echo "Running test: $base"
    python3 main.py $acc $event $transaction < $i > ./Tests/outputs/$base.ato
done

#Testing sell ticket (new event) function
sellTests=$(find ./Tests/inputs/sell -type f -name "*.tti" | sort --version-sort)
for i in $sellTests
do
    name="${i##*/}"
    base="${name%.*}"
    acc=$(find ./Tests/inputs -type f -name "$base.tai")
    event=$(find ./Tests/inputs -type f -name "$base.tei")
    transaction="/Tests/outputs/$base.adt"
    echo "Running test: $base"
    python3 main.py $acc $event $transaction < $i > ./Tests/outputs/$base.ato
done

#Testing refund function
refundTests=$(find ./Tests/inputs/refund -type f -name "*.tti" | sort --version-sort)
for i in $refundTests
do
    name="${i##*/}"
    base="${name%.*}"
    acc=$(find ./Tests/inputs -type f -name "$base.tai")
    event=$(find ./Tests/inputs -type f -name "$base.tei")
    transaction="/Tests/outputs/$base.adt"
    echo "Running test: $base"
    python3 main.py $acc $event $transaction < $i > ./Tests/outputs/$base.ato
done





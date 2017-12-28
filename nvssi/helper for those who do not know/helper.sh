#! /bin/bash


URL="your github repo URL goes here"
message="initial message"
projectName="name of git project"

git init .
git add .
git commit -m "$message"
git remote add $projectName $URL

git pull $projectName master
git push $projectName

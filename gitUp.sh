#!/bin/bash

#Script to 1) add all files to git tracking, 2) prompt user for comment, & 3) push changes
read -r -p 'Commit message: ' desc #prompt user for commit message
git add --all			   #track all files
git add -u			   # track deletes
git commit -m "$desc"		   # commit with message
git push			   # push to git repo


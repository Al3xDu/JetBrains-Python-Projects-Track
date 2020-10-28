#!/bin/bash


commit_msg=$1

function commit(){
	git add . ; git commit -m "${commit_msg}" ; git push
	[[ $? ]] && echo "Commited with ${commit_msg}"
}

commit

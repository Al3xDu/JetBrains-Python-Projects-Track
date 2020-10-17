#!/bin/bash

commit_msg=$1

echo "Commited with ${commit_msg}"

function commit(){
	git add . ; git commit -m "${commit_msg}" ; git push
}
commit

import subprocess

cmd1="docker login -u user1 -p Abc1234 -e user1@vmware.com 127.0.0.1"
cmd2="docker tag alpine 127.0.0.1/myrepo1/alpine"
cmd3="docker push 127.0.0.1/myrepo1/alpine"
cmd6="docker logout user1"
cmd4="docker login -u user2 -p Abc1234 -e user2@vmware.com 127.0.0.1"
cmd5="docker pull 127.0.0.1/myrepo1/alpine"
print subprocess.call(cmd1.split(" "))
print subprocess.call(cmd2.split(" "))
print subprocess.call(cmd3.split(" "))
print subprocess.call(cmd6.split(" "))
print subprocess.call(cmd4.split(" "))
print subprocess.call(cmd5.split(" "))

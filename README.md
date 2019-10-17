# MongoDB_Demo

### Tweets Stream:
* Run "TwitterStream.py" and store as many tweets as you like and then stop the execution. The keyword here is "cloud".
* All your downloaded tweets are now stored in "tweets.txt" file in JSON format
* See "sample_tweet" to understand the structure of a tweet.

### General Information (Cloudera):
* Operating System:         Mac -> Microsoft Remote Desktop, Windows -> Default Remote Desktop, Ubuntu -> Remmina
* Machine:                  cqs-cs6304-xxx.ats.mst.edu
* User:                     cloudera
* Default Password:         stu-pass
* Change Password Command:  sudo passwd cloudera

* "Firefox already running" error solve by command:     killall -SIGTERM firefox

* "Eclipse workspace in use" error solve by command:
* cd ~/yourWorkspaceDirectory/.metadata
* rm .lock

* "Eclipse resource is out of sync" error solve by:
* Windows -> Preferences -> General -> Workspace
* Check "Refresh using native tool or polling"

### Install MongoDB in Cloudera:
* sudo chmod 777 '/etc/yum.repos.d/mongodb-org.repo' //to enable write permission to mongodb repository
* nano '/etc/yum.repos.d/mongodb-org.repo' //to open an editor to edit the repository file
* gpgcheck=0 //edit the line gpgcheck=1 to 0 to skip the key check
* ctrl+O //press control + o to promt the 'file save'
* Enter //hit enter to save the file
* ctrl+X //press control + x to exit the editor
* sudo yum install -y mongodb-org //to install mongodb in your computer
* sudo /sbin/service mongod start //to start the mongodb service
* sudo /sbin/service mongod stop //to stop the mongodb service

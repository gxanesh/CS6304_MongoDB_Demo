# MongoDB_Demo

Go to Command.txt and follow the instructions.

### General Information (access your VM):
* Operating System:         Mac -> Microsoft Remote Desktop, Windows -> Default Remote Desktop, Ubuntu -> Remmina
* Machine:                  cs6304-<mst_username>-01.class.mst.edu
* User:                     <mst_username>
* Default Password:         <mst_password>


### Install MongoDB (Self Note, not for students):
wget -qO - https://www.mongodb.org/static/pgp/server-6.0.asc | sudo apt-key add -  
echo "deb [ arch=amd64,arm64 ] https://repo.mongodb.org/apt/ubuntu focal/mongodb-org/6.0 multiverse" | sudo tee /etc/apt/sources.list.d/mongodb-org-6.0.list  
sudo apt-get update  
sudo apt-get install -y mongodb-org  
sudo systemctl start mongod   


If you receive an error similar to the following when starting mongod  
Failed to start mongod.service: Unit mongod.service not found.  
Run the following command first:  
sudo systemctl daemon-reload  

* check if service is running:  
sudo systemctl status mongod  

* Stop MongoDB:  
sudo systemctl stop mongod  

* Restart MongoDB:  
sudo systemctl restart mongod  

* Begin using MongoDB:  
mongosh  



### EXTRA:: Tweets Stream (Not required for the class):
* Run "TwitterStream.py" and store as many tweets as you like and then stop the execution. The keyword here is "cloud".
* All your downloaded tweets are now stored in "tweets.txt" file in JSON format
* See "sample_tweet" to understand the structure of a tweet.
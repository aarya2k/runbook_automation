# Runbook Automation

What is Runbook Automation ?

Runbook automation is a automation task to have master control over bunch of servers called Minions. 

This Runbook automation API will execute a list of basic commands when a server is newly added.

Since the Requirement was very vague, I have assumed the logics myself and completed the assignment.

We can easily deploy Runbook automation within a Docker container with the below steps. This deployment should work for all environments


Build the docker Image:
$ docker build -t runbook_automation:latest

Run the Docker Container:
$ docker run -d -p 5000:5000 runbook_automation

You can find the container runtime details as shown below

$ docker ps -a
CONTAINER ID  IMAGE                       COMMAND                        CREATED         STATUS           PORTS           
92fa3c65b4cd  runbook_automation:latest   "python runbook_automation.py" 3 minutes ago   Up 1 minutes    0.0.0.0:5000->5000/tcp   

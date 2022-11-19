Docs understood points:
**********************
# New Trenton CI Architecture
# This doc is to show the entire flow of tentron ci and it will shows differente stages and steps:

# SECTIONS :

  SECTION 1 :
    # What jobs do we have here

    . Trenton ci instead manual we can use jenkins file like pipeline job

    . we know the create to create a what kind of job like job as HUD

    . In the bitbucket we will create a repository under the repositoty to create branch like like master.

    . The devoloper commit the code like master branch/feature branch

    . Then we have to integrate jenkins with bitbucket

    . Create a pipeline job agents as docker

    . In the job we can give buils tabs,emails,and pull request it will avaoid the confusion of developer
      and also give build parameter

    . The job implementation that means jenkins file stored in bitbucket

    . To setup the build trigger as every 4hours, If any changes in remote repository automatically 
      the code will be build trigger in every 4hours

    . The build trigger and unit test run parallel

    . If the build is successfull to merge the pull request  

  SECTION 2:

    # Build, unit test,code quality check:

    . Clone the repository then if any merge changes locally the build is parallel like build,unit test, 
      code quality check

    . Then we have to push artifats in to artifast storage

    . once done build we can set up the build notification

    . It is notified the the result of if is build success or fail then send to emil

  SECTION 3 :

    # Maintenance jobs:

    Step 1 :
    # NFS cleanup :
    . we can use storage type like NFS storage

    . Check how much space is used on NFS/other storage

    . If storage is more than 70% space used we can set the email alert

    . And then to clean the oldest artifacts from the artifacts repository

    Step 2 :
    # nodes clean-up
    . we need to remove jenkins work place from old files

    . we have to find old files and remove them and also clean nodes from old docker images

    . Find old workspaces and delete them

    . Delete old directories starting with git

    Step 3 :    
    # Refresh reference clones  
    . We need a job that will refresh local clones from time to time on all nodes.
    
    . Refresh reference clone and create new ones if do not exist

    . List of repositories should be easy to change
----------------------------------------------------------------


# Jenkinsfiles:

    # Entrypoint :
    - Genarally A build parameter allows us to pass data into our Jenkins jobs
    - In the jenkins pipeline, first we need to pass the parameters like Build, Test, Promote, ent_ssd_test revision
    - Then Triggers Main job with the above parameters
    - Then next step will be to clean up the work space
    - Then we have to build job with our required parameters

    # Main job :   
    - In the pipeline we can pass the parameters and then agent is none then next stage will be pull request 
      and you can setup the environment also
    - We can use a agent as docker then next stages are code commit and pull request.
    - Under the stage we can create steps one by one
    - To build the code by using build steps like build stage   
    - Next stage will be code quality check under stage we can mention steps
    - Next stage will be Merge, the changes from develop locally automatically build
    - Then clean up the work place. 

    # Build :
    - In the build jenkins file first we need to pass the parameters
    - parameters like TRENTON_COMMIT_HASH, UPSTREAM_BUILD_NUMBER, ENT_SSD_TEST_REVISION etc...
    - We can take agent as docker and under the steps we can use docker image
    - Then next stage will be to run the build steps and then clean work space
    - The final stage is to publish the artifacts that means to copy the artifacts.

    # Code quality check :
    - Here also we can use the parameters in the pipeline
    - We can take agent as none and the stage will to run the test casess
    - Under the docker agent steps to clean the work space and use image and args
    - And then stage will be clock work and agent as docker and take image and args

@ I reffering Shared Libraries...............

    




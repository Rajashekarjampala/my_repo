1. AIM:
    Write Shell function, SCP a Shell file from your VM to Remote VM

2. Defination of done:
    Copy files from a local host to remote host by using shell functions and the user to securely copy files and directories      between two servers

3. Pre-requisites:
    1. Local host
    2. Remote server
    3. Remote server username and IP

4. Steps:
    Step 1:
        Login to remote server using IP, Port, Username.
        Specifies the port to establish connection with the remote host. By using the below command
            ssh username@remoteserver -p <portnumber>

    step 2 :
        Run the below scp command it will copy the file from (source) localhost to (designation) remote server 
        with securely   
            sshpass -p vudeadmin scp file1.txt vudeadmin@10.208.44.141:/home/vudeadmin

    step 3 :
        To Store entire output in the output folder, following the below command
            sshpass -p vudeadmin scp file1.txt vudeadmin@10.208.44.141:/home/vudeadmin > remote_server_info     

          

5. Algorithm:

    function scp () {
    # sshpass -p vudeadmin scp file1.txt vudeadmin@10.208.44.141:/home/vudeadmin
    sshpass -p $3 ssh -o "StrictHostKeyChecking=No" scp "$4" $2@$1:"$5"
    }

    # call scp
    scp $1 $2 $3 $4 $5

6. Sample Commands:
    To copy the file from local host to remote server by using command line
        scp <option> <source-file> remote_username@Ip:<designation-file>

    To copy the file from local host to remote server by using shell function
        sshpass -p vudeadmin scp scp.sh vudeadmin@10.208.44.141:/home/vudemaster
        sshpass -p $3 ssh -o "StrictHostKeyChecking=No" scp "$4" $2@$1:"$5" >> $6

        
7. Verifications:
    1. Login to the remote server -
    2. To Verify the files on remote server copy/not -


8. References:
    https://stackoverflow.com/questions/1346509/automate-scp-file-transfer-using-a-shell-script
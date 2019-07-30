

#Check if server access is available via ssh without password
#Assuming there is a public key file
#convert .ppk to OpenSSH key for paramiko
#Author: Brookly Younce
#Date last modified: 07/29/2019




# sys for use with command line args
# paramiko for ssh support with windows
import sys, time, paramiko




def connectToHost(line, ssh, ip, hostname, usernameForSSH, key):
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh.connect(ip, username=usernameForSSH, pkey=key, look_for_keys=False, allow_agent=False)
    stdin, stdout, stderr = ssh.exec_command('pwd')
    print(stdout.readline())


# arg 1 would be the file name as arg[0] is always the name of the script being run
fileWithServerIPs = sys.argv[1]
filenameForResults = sys.argv[2]
usernameForSSH = sys.argv[3]
filePathToKey = sys.argv[4]
print("File to read ", fileWithServerIPs)

try:
        # make file obj, open only with read rights
    fileObj = open(fileWithServerIPs, "r")
    fileResults = open(filenameForResults, "a")
    ip = ""
    hostname = ""
    connectionError = False
    sshClientFailure = False
    for line in fileObj:
        #IP, hostname
        #take all the spaces down to one space, remove duplicates
        lineData = " ".join(line.split())
        lineData = line.split()
        ip = lineData[1].strip()
        hostname = lineData[0].strip()
        writeString = "Connection to IP: " + ip + " HOSTNAME: " + hostname
        print("\nAttempting connection to", ip, hostname)

        try:
            connectionError = False
            ssh = paramiko.SSHClient()
            key = paramiko.RSAKey.from_private_key_file(filename=filePathToKey, password=None)
            connectToHost(line, ssh, ip, hostname, usernameForSSH, key)
        except Exception as ex:
            writeString = "*** " + writeString + " FAILED with " + str(ex) + "\n"
            connectionError = True
        finally:
            ssh.close()

        if connectionError != True:
            writeString = "*** " + writeString + " was SUCCESSFUL" + "\n"

        fileResults.write(writeString)
        print(writeString)

except Exception as e:
    print("--> An error occurred, see below \n\n\n")
    print(e)

finally:
    fileObj.close()
    fileResults.close()




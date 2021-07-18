import subprocess

subprocess.run(["ls","-l"])
completed = subprocess.run(["ls","-l"],
                       capture_output=True,
                        text=True)
print("\n type of completed",type(completed))
print("\n args",completed.args)
print("\n returncode",completed.returncode)
print("\n stderr",completed.stderr)
print("\n stdout: \n",completed.stdout)
#subprocess.call
#subprocess.check_call
#subprocess.check_output
#subprocess.Popen
completed2 = subprocess.run(["/usr/local/bin/python3","/Users/smenezes/python_projects/standardlibrary/other.py"],
                       capture_output=True,
                        text=True)
print("\n stdout: \n",completed2.stdout)

#try:    
#completed3 = subprocess.run(["false"],capture_output=True,text=True,check=True)
#print("hi")
                        
#except subprocess.CalledProcessError as ex:
 #   print(ex)
# The script which makes use of the POST API call from SLACK and POST the SLACK TOKEN and the COMMAND
# Step 1:
# We make use of request.form.get () method to get two values from variables (token,command and text) ==> Main factor

# Step 2:
# Once we get what TEXT is typed in SLACK,, the same text will be used as argument and based on TEXT , we are making some actions using subprocess module and make a JSON response via POST call to SLACK back.
# See the Image of how slack is being invoked


from flask import Flask, request, Response, jsonify, abort
import subprocess
import os
from subprocess import Popen, PIPE
app = Flask(__name__)
#slack_token = os.environ['Uhxybb4u0cVwFERAR6Nu2HM2']
#https://gist.github.com/devStepsize/59c15d850e82a77e539b8ff3d5cb5cad

# Below is the list to check on service status on Linux machine, ALthoug it is yet to developed in part of script

service = [ 'httpd', 'sshd', 'mysql' ]
string = "service"
@app.route('/show/', methods=['GET','POST'])
def hello():
    token = request.form.get('token', None)  # TODO: validate the token
    command = request.form.get('command', None)
    text = request.form.get('text', None)
    host_id = text.split()[2]
    actual_command = text.split()[1]
    print(text.split( )[2])
    if not token:
        abort(400)
    if text == 'uptime on localhost':
        a = subprocess.Popen(['uptime'],stdout=PIPE)
        stdout = a.communicate()
        response = { 
            "text" : "Here is the Uptime",
            "attachments": [
                {
                    "text": "you have entered host as {}".format(stdout)
                }    
            ]}   
        
        return response
    if text == 'disk on localhost':
        a = subprocess.Popen(['df', '-h'],stdout=PIPE)
        stdout = a.communicate()
        response = { 
            "text" : "Here is the Disk usage for the server ",
            "attachments" : [
                { "text" : " The Disk usage of the server seen as: {}".format(stdout)}]}
        return response
    if text == 'show covid report':
        a = subprocess.Popen(['python3', '/root/covid.py'],stdout=PIPE)
        stdout = a.communicate()
        response = {
            "text" : "Here is the Covid report usage",
            "attachments" : [
                { "text" : "The Covid report as of now as : {}".format(stdout)}]}

   # for i in  
   # if text == 'service

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='127.0.0.1', port=5000, debug=True)

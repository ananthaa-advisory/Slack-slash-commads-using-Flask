# Slack-slash-commads-using-Flask
Slash commands in slack using Flask POST API call


# The script which makes use of the POST API call from SLACK and POST the SLACK TOKEN and the COMMAND
# Step 1:
# We make use of request.form.get () method to get two values from variables (token,command and text) ==> Main factor

# Step 2:
# Once we get what TEXT is typed in SLACK,, the same text will be used as argument and based on TEXT , we are making some actions using subprocess module and make a JSON response via POST call to SLACK back.
# See the Image of how slack is being invoked


Step 3:

See the IMage to see how to create a SLACK integration:
To create Slash command --> click on workspace -> settings and adminstration - > Manage Apps - > From left plane, click on "Custom integrations"---> Type SLASH command and click on enter. 
From here, see the image to proceed as you have to enter the endpoint POST URL "/show" from the FLASK API created at backend.
For how to create POST call using FLASK API, refer the main script attached

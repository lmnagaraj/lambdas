import cfnresponse
import json
def Handler(event, context):
 print("entering into event")
 print(json.dumps(event))
 responseData = 'Nagarajan Manokaran'
 PhysicalResourceId = None
 cfnresponse.send(event, context, cfnresponse.SUCCESS, responseData, PhysicalResourceId)


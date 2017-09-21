import string
import random
import json
import cfnresponse
def handler(event, context):
 print "my function has been started"
 print json.dumps(event)


 if event['RequestType'] == 'Create':
   responseData = {}
   responseData['returnvalue'] =  ("i-") + "".join(random.choice('0123456789' + 'ABCDEFGHIJKLMNOPQRSTUVWXYZ') for _ in range(16))
   PhysicalResourceId = ("naga-") + "".join(str(random.randint(2, 100)) for _ in range(4))

   print "Sending the below response data back to cloudformation"
   cfnresponse.send(event, context, cfnresponse.SUCCESS, responseData, PhysicalResourceId)
 
 elif event['RequestType'] == 'Update':
   responseData = {}
   responseData['returnvalue'] =  ("i-") + "".join(random.choice('0123456789' + 'ABCDEFGHIJKLMNOPQRSTUVWXYZ') for _ in range(16))
   PhysicalResourceId = ("naga-") + "".join(str(random.randint(2, 100)) for _ in range(4))

   print "Sending the below response data back to cloudformation"
   cfnresponse.send(event, context, cfnresponse.SUCCESS, responseData, PhysicalResourceId)
 
 else:
  responseData = None
  PhysicalResourceId = event['PhysicalResourceId']
  print("deleted")
  cfnresponse.send(event, context, cfnresponse.SUCCESS, responseData, PhysicalResourceId)

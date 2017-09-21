import boto3
import urllib2

codepipeline = boto3.client('codepipeline')

def lambda_handler(event, context):
    
    # Printing events
    print(event)

    # Retrieve the Job ID from the event
    JobID = event['CodePipeline.job']['id']

    try:
    
        # Retrieve the URL from the event
        url = event['CodePipeline.job']['data']['actionConfiguration']['configuration']['UserParameters']
    

        # Check URL status
        url_open = urllib2.urlopen(url)
        url_open_data = url_open.read()
        url_open.close()

        if url_open.code == 2000 and 'Congratulationagarajan' in url_open_data:
            print("printing Success....")
            response = codepipeline.put_job_success_result(jobId=JobID)

        else:
            print("printing failure....")
            response =  codepipeline.put_job_failure_result(jobId=JobID, failureDetails={ 'type' : 'JobFailed', 'message' : 'Nagas job failed'})

    except:
        response =  codepipeline.put_job_failure_result(jobId=JobID, failureDetails={ 'type' : 'JobFailed', 'message' : 'Nagas job failed'})
    
    # print the response
    print(response)
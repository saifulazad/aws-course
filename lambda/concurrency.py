from concurrent import futures
import boto3
import json
from concurrent.futures import as_completed
import time

client = boto3.client('lambda', region_name='us-east-1')

def call_lambda(i):
   response =client.invoke(FunctionName='dynamo-write',
           InvocationType='RequestResponse',
            Payload = json.dumps({
                'id': str(i),
                'title':'asas',
            })

   )
   return i, json.loads(response['Payload'].read())
start = (time.time())
with futures.ThreadPoolExecutor(max_workers=500) as executor:
    # submit tasks and collect futures
    l = []
    o = list(range(20))
    futures = [executor.submit(call_lambda, i) for i in range(700)]
    # process task results as they are available
    for future in as_completed(futures):
        # retrieve the result
        e = (future.result())
        print(e)
        l.append(e[0])

    print(sorted(l))

end = (time.time())

print(end-start)

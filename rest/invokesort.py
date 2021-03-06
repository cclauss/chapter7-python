import os, requests, json

def url(operation):
    return "%s/api/v1/namespaces/%s/%s" % (
        os.environ["__OW_API_HOST"],
        os.environ["__OW_NAMESPACE"],
        operation
    )

def auth():
    up = os.environ['__OW_API_KEY'].split(":")
    return (up[0], up[1])

def whisk_invoke(action, args,  
                 blocking=True, result=True):
    invoke = "actions/%s?blocking=%d&result=%d" % (
        action, blocking, result)
    resp = requests.post(
        url=url(invoke), 
        auth=auth(),
        json=args
    )
    return json.loads(resp.text)

def main(args):
    input = {"lines": args["text"].split(" ")}
    res = whisk_invoke("utils/sort", input)
    return res

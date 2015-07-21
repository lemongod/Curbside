#Vincent Wang
#wang.q.vincent@gmail.com
import requests
import json


keyurl = 'http://challenge.shopcurbside.com/get-session'
baseurl = 'http://challenge.shopcurbside.com/'
key = requests.get(keyurl)
head = {'Session': key.text}

stack = ['start']
visited = set()
ans = ''
counter = 0

#basic DFS
while stack:
    counter += 1
    if counter >= 10: #must refresh header key
        key = requests.get(keyurl)
        head = {'Session': key.text}
        counter = 0
    vertex = stack.pop()
    r = requests.get(baseurl+vertex, headers=head)

    parsed_json = json.loads(r.text) #malformed JSON keys fix
    for key in parsed_json.keys():
        parsed_json[key.lower()] = parsed_json[key]

    if parsed_json.get('next'):
        next_nodes = parsed_json['next']
        if vertex not in visited: #not actually necessary since secrets are only on lowest depth
            visited.add(vertex)
            if type(next_nodes) == list: #if it's a list of nodes
                for next_vertex in next_nodes:
                    stack.append(next_vertex)
            else:
                stack.append(next_nodes) #entire list is just one node
    if parsed_json.get('secret'):
        ans = ans + parsed_json['secret']

print ans[::-1] #python! string reversal

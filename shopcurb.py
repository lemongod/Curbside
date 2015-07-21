#Vincent Wang
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
    if counter >= 10:
        key = requests.get(keyurl)
        head = {'Session': key.text}
        counter = 0
    vertex = stack.pop()
    r = requests.get(baseurl+vertex, headers=head)
    parsed_json = json.loads(r.text)
    if parsed_json.get('next'):
        next_nodes = parsed_json['next']
        if vertex not in visited:
            visited.add(vertex)
            if type(next_nodes) == list:
                for next_vertex in next_nodes:
                    stack.append(next_vertex)
            else:
                stack.append(next_nodes)
    if parsed_json.get('secret'):
        ans = ans + parsed_json['secret']
print ans[::-1] #python! string reversal

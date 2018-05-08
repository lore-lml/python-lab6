import requests

url= 'http://127.0.0.1:5000/api'

if __name__ == '__main__':
    #TRY TO INSERT
    task = {'description': 'buy some pasta', 'priority': '2'}
    requests.post(url + "/tasks", json=task)

    #TRY TO UPDATE
    task = {'description': 'book summer holidays', 'priority': '0'}
    requests.put(url + "/tasks/11", json=task)

    #TRY TO DELETE
    requests.delete(url + "tasks/15")

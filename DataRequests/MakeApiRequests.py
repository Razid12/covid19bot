import requests
import json
class Api:
    def __init__(self):
        pass

    def makeApiRequestForCounrty(self, country_name):
        url = "https://covid-193.p.rapidapi.com/statistics"

        headers = {
            "X-RapidAPI-Host": "covid-193.p.rapidapi.com",
	        "X-RapidAPI-Key": "2a93a437b9msh4a5e7f0687b7264p13a489jsnf5f918c84ed5"
	        
        }
        response = requests.request("GET", url, headers=headers, params=querystring)
        #print(response.json())
        js = json.loads(response.text)
        print("******", js)
        result = js.get('response')[0]
        print(result.get('cases'))
        print("*" * 20)
        return result.get('cases') , result.get('deaths'),result.get('tests')


    def makeApiRequestForIndianStates(self):
        url = "https://covid19-data.p.rapidapi.com/india"
        headers = {
            "X-RapidAPI-Host": "covid19-data.p.rapidapi.com",
	        "X-RapidAPI-Key": "2a93a437b9msh4a5e7f0687b7264p13a489jsnf5f918c84ed5"
        }
        response = requests.request("GET", url, headers=headers)
        # print(response.text)
        js = json.loads(response.text)
        print("******", js)
        #result = js.get('list')
        return js


    def makeApiWorldwide(self):
        url = "https://covid-19-statistics.p.rapidapi.com/reports/total"
        headers = {
            "X-RapidAPI-Host": "covid-19-statistics.p.rapidapi.com",
	        "X-RapidAPI-Key": "2a93a437b9msh4a5e7f0687b7264p13a489jsnf5f918c84ed5"

        }
        response = requests.request("GET", url, headers=headers)
        # print(response.text)
        js = json.loads(response.text)
        print("******", js)
        result = js.get('data')

        return result


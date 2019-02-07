# -*- coding: utf-8 -*-
"""
Created on Thu Feb  7 12:13:36 2019

@author: Onie
"""

from flask import Flask, request
from flask_restful import Resource, Api
from requests import get, post


app = Flask(__name__)
api = Api(app)


class ProxyAPI(Resource):
    def get(self, target_url):
        return get(target_url).json()

    def post(self, target_url):
        headers = {'User-Agent': request.headers['User-Agent']}
        data = request.form
        response = post(target_url, data=data, headers=headers)
        #print(response.text)
        return response


api.add_resource(ProxyAPI, '/proxy/<path:target_url>', endpoint = 'proxy_ep')

if __name__ == '__main__':
    app.run(debug=True)
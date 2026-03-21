# -*- coding: utf-8 -*-
"""
Created on Sat Mar 21 10:57:27 2026

@author: Admin
"""

import requests

import os

# your JWT token
token = os.getenv('JWT')

url = "https://api.resourcewatch.org/v1/application"

headers = {
    "Authorization": f"Bearer {token}",
    "Content-Type": "application/json"
}

data = {
    "name": "my-app"
}

response = requests.post(url, json=data, headers=headers)

print(response.json())
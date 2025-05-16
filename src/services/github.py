import pandas as pd
import requests
import json
import boto3
from utils.aws import AWSUtil


# Create a class for a Github service that will call the Github API
class GithubService:
    def __init__(self, token: str, base_url: str = "https://api.github.com"):
        self.token = token
        self.base_url = base_url

    def get_user(self, username: str) -> dict:
        """Get user information from Github."""
        url = f"{self.base_url}/users/{username}"
        headers = {
            "Authorization": f"token {self.token}",
            "Accept": "application/vnd.github.v3+json",
        }
        response = requests.get(url, headers=headers)
        response.raise_for_status()
        return response.json()
    def __get_token(self) -> str:
        """Get the Github token from AWS Secrets Manager."""
        aws = AWSUtil(secret_name="github_token")
        secret = aws.get_secret()
        return secret["github_token"]
    
    # Create a function to get paginated data from the Github API
    # Modify __get_paginated_data to use __call_api for each page
    def __get_paginated_data(self, url: str) -> list:
        """Get paginated data from Github API.""" 
        data = []
        while url:
        # Use __call_api to fetch data for the current page
        page_data = self.__call_api(url)
        data.extend(page_data)
        # Extract the next page URL from the response headers
        headers = {
            "Authorization": f"token {self.token}",
            "Accept": "application/vnd.github.v3+json",
        }
        response = requests.get(url, headers=headers)
        response.raise_for_status()
        url = response.links.get("next", {}).get("url")
        return data
    
    def get_user_repos(self, username: str) -> list:
        """Get user repositories from Github."""
        url = f"{self.base_url}/users/{username}/repos"
        return self.__call_api(url)
    
    # Create a generic private function to call the Github API that will accept a url as a parameter that other functions will call to get data
    def __call_api(self, url: str) -> dict:
        """Call the Github API."""
        headers = {
            "Authorization": f"token {self.token}",
            "Accept": "application/vnd.github.v3+json",
        }
        response = requests.get(url, headers=headers)
        response.raise_for_status()
        return response.json()
    
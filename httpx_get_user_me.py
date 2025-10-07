import httpx

login_payload = {
    "email": "user1@example.com",
    "password": "123"
}
login_response = httpx.post("http://localhost:8000/api/v1/authentication/login", json=login_payload)
print(f"Login response: {login_response.json()}")
print(f"Status code: {login_response.status_code}")

access_token = login_response.json()["token"]["accessToken"]
headers = {"Authorization": f"Bearer {access_token}"}
get_user_response = httpx.get("http://localhost:8000/api/v1/users/me", headers=headers)
print(f"Get user response: {get_user_response.json()}")
print(f"Status code: {get_user_response.status_code}")

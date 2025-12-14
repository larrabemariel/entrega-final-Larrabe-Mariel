import requests

class TestAPI:
    
    BASE_URL = "https://jsonplaceholder.typicode.com"

    def test_get_posts(self):
        response = requests.get(f"{self.BASE_URL}/posts")
        assert response.status_code == 200
        assert isinstance(response.json(), list)

    def test_create_post(self):
        new_post = {
            "title": "foo",
            "body": "bar",
            "userId": 1
        }
        response = requests.post(f"{self.BASE_URL}/posts", json=new_post)
        assert response.status_code == 201
        assert response.json()["title"] == "foo"

    def test_delete_post(self):
        response = requests.delete(f"{self.BASE_URL}/posts/1")
        assert response.status_code == 200

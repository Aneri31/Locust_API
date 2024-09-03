from locust import HttpUser, TaskSet, task, between

class JsonPlaceholderUserBehavior(TaskSet):
    @task(1)
    def get_posts(self):
        response = self.client.get("/posts", name="Get Posts")
        if response.status_code != 200:
            print(f"Failed to get posts. Status code: {response.status_code}")

    @task(2)
    def get_post(self):
        post_id = 1
        response = self.client.get(f"/posts/{post_id}", name="Get Single Post")
        if response.status_code != 200:
            print(f"Failed to get post {post_id}. Status code: {response.status_code}")

class JsonPlaceholderUser(HttpUser):
    tasks = [JsonPlaceholderUserBehavior]
    wait_time = between(2, 5)  # Simulate a user wait time between 2 and 5 seconds
    host = "https://jsonplaceholder.typicode.com"  # Set the base URL for the requests

    def on_start(self):
        print("User has started")

    def on_stop(self):
        print("User has stopped")

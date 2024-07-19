from locust  import HttpUser, TaskSet, task, between
import json
import random

class UserBehavior(TaskSet):

    @task
    def like_post(self):
        
        self.client.get(
            '/like/1',
            data=json.dumps({}),
            headers={"Content-Type": "application/json"},
        )

class WebsiteUser(HttpUser):
    tasks = [UserBehavior]
    wait_time = between(1, 2)  # Wait between 1 and 2 seconds between tasks

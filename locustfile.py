from locust import HttpUser, task, between

class WebsiteUser(HttpUser):

    @task
    def home_page(self):
        self.client.post("/predict")

from locust import HttpLocust, TaskSet, task


class TestEndpoints(TaskSet):
    @task
    def test_homepage(self):
        self.client.get("/")

    @task
    def test_about(self):
        self.client.get("/about")

    @task
    def test_form(self):
        self.client.post("/form", data={"user": "random"})


class MyLocust(HttpLocust):
    task_set = TestEndpoints

from locust import HttpLocust, TaskSet, between


def index(l):
    l.client.get("/WeatherForecast")


class UserBehavior(TaskSet):
    tasks = {index: 1}


class WebsiteUser(HttpLocust):
    task_set = UserBehavior
    wait_time = between(0, 0)

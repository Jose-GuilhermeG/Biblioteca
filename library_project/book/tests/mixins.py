from rest_framework.test import APIClient

class ForcedLoggedClient:
    @staticmethod
    def get_logged_client(user):
        client = APIClient()
        client.force_login(user)
        return client
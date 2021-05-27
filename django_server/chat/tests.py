from django.test import TestCase
from rest_framework.test import APIClient
from rest_framework import status
from . import config

client = APIClient()


class TaskTestCase(TestCase):

    def setUp(self):
        pass

    def test_banglish_greet_success(self):
        response = client.post(
            '/chat/message/',
            {
                "sender": "test_user",
                "message": "asen bhai!"
            },
            format='json',
        )
        print(response.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_banglish_fail_success(self):
        response = client.post(
            '/chat/message/',
            {
                "sender": "test_user",
                "message": "@@@$..h..!,i,,,,~~~~~~~"
            },
            format='json',
        )
        print(response.data)
        err_txt = response.data["text"]
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertFalse(err_txt == config.ERR_TXT)

    def test_banglish_fail_len(self):
        response = client.post(
            '/chat/message/',
            {
                "sender": "test_user",
                "message": "@@@$..h..!,,,,,~~~~~~~"
            },
            format='json',
        )
        print(response.data)
        err_txt = response.data["text"]
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(err_txt, config.ERR_TXT)

    def test_banglish_fail_num(self):
        response = client.post(
            '/chat/message/',
            {
                "sender": "test_user",
                "message": "0011"
            },
            format='json',
        )
        print(response.data)
        err_txt = response.data["text"]
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(err_txt, config.ERR_TXT)

        response = client.post(
            '/chat/message/',
            {
                "sender": "test_user",
                "message": "123567hi232"
            },
            format='json',
        )
        print(response.data)
        err_txt = response.data["text"]
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertFalse(err_txt == config.ERR_TXT)

from django.urls import reverse, resolve
from django.test import SimpleTestCase
from accounts.views import CustomUserListView
from rest_framework.test import APITestCase
from accounts.models import CustomUser
from rest_framework.authtoken.models import Token
from rest_framework import status

class ShelfApiTests(SimpleTestCase):

    def test_get_users_is_resolved(self):
        url = reverse('users')
        self.assertEquals(resolve(url).func.view_class, CustomUserListView)


class UserAPIViewTest(APITestCase):

    users_urls = reverse('users')

    def setUp(self):

        self.user = CustomUser.objects.create_user(username="unit_test_user", password="123456789")
        self.token = Token.objects.create(user=self.user)
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + self.token.key)

    def TearDown(self):
        pass

    def test_get_users_authenticated(self):
        response = self.client.get(self.users_urls)
        self.assertEqual(response.status_code, status.HTTP_200_OK)


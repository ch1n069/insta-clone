from django.test import TestCase
from .models import Post, HashTag

# Create your tests here.

class PostTestClass(TestCase):

    def setUp(self):
        self.bruno = Post(author=self.bruno, title='this is gatiba post', body='this is body of gatibas post', title_tag='this my uno post',hash_tag='this is good', image='image.jpeg')

        # instantiation happened above 




    def test_instances(self):
        self.assertTrue(isinstance(self.bruno,Post))


class HashTagTestClass(TestCase):


    def setUp(self):
        self.perfect = HashTag(name="perfecto")
import pytest
from cats import get_cat_random_image_url

def test_get_cat_image_success(mocker):
   mock_get = mocker.patch('cats.requests.get')

   mock_get.return_value.status_code = 200
   mock_get.return_value.json.return_value = {
       'id':'c69',
       'url': "https://cdn2.thecatapi.com/images/c69.jpg",
       'width': 588,
       'height':331
   }

   cat_url = get_cat_random_image_url()
   assert cat_url == "https://cdn2.thecatapi.com/images/c69.jpg"


def test_get_cat_image_failure(mocker):
   mock_get = mocker.patch('cats.requests.get')

   mock_get.return_value.status_code = 404
   cat_url = get_cat_random_image_url()
   assert cat_url is None

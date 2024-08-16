import unittest
from app import app

class AppTestCase(unittest.TestCase):
    def setUp(self):
        """Set up a test client."""
        self.client = app.test_client()
        self.client.testing = True

    def test_index_page(self):
        """Test if the index page loads successfully."""
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Upload your content and style images', response.data)

    def test_upload(self):
        """Test the upload functionality."""
        data = {
            'content_image': (open('data/examples/sample_content.jpg', 'rb'), 'content.jpg'),
            'style_image': (open('data/examples/sample_style.jpg', 'rb'), 'style.jpg')
        }
        response = self.client.post('/upload', content_type='multipart/form-data', data=data)
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Generated Music', response.data)

if __name__ == '__main__':
    unittest.main()

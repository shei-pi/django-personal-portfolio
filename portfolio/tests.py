"TDD Demo!"
from urllib import response
from django.test import TestCase
from django.urls import reverse
from test_plus.test import TestCase as PlusTestCase
class DemoTests(TestCase):
    
    def test_ping_get(self):
        """GET Ping
        """
        response = self.client.get('/ping/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.content.decode('utf8'),'pong')
        
    def test_ping_head(self):
        """HEAD ping
        """
        response = self.client.head('/ping/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.content, b"")
        self.assertGreater(int(response["Content-Length"]), 0)
    def test_ping_options(self):
        """OPTIONS ping
        """
        response = self.client.options('/ping/')
        self.assertEqual(response.status_code, 200) 
        self.assertEqual(int(response["Content-Length"]), 0)
        for method in ["GET", "HEAD", "OPTIONS"]:
            with self.subTest(method=method):
                self.assertIn(method, response["Allow"], f"{method} not in ALLOW header")
    
    def test_ping_method_not_allowed(self):
        """Do we handle disallowed mehtods
        """
        not_allowed = ["post", "put", "patch", "delete", "trace"]
        for method in not_allowed:
            with self.subTest(method=method):
                call_method = getattr(self.client, method)
                response = call_method('/ping/')
                self.assertEqual(response.status_code, 405)
            
        
    def test_status_get(self):
        """Test the status page"""
        url = reverse('site_status')
        self.assertEqual(url,'/status/')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        templates=["portfolio/base.html",
                   "portfolio/status.html"]
        for t_name in templates:
            with self.subTest(template=t_name):
                self.assertTemplateUsed(response, t_name)
        self.assertIn('status', response.context)
        self.assertEqual(response.context['status'],'Good')
        
        self.assertInHTML('<p>Status is Good</>', response.content.decode("utf8"))
    
class DemoTestsPlus(PlusTestCase):
    
    def test_status_get_refactored(self):
        """Test the status page"""
        response = self.get_check_200("site_status")
        templates=["portfolio/base.html",
                   "portfolio/status.html"]
        for t_name in templates:
            with self.subTest(template=t_name):
                self.assertTemplateUsed(response, t_name)
        self.assertInContext('status')
        self.assertContext('status','Good')
        self.assertResponseContains("Status is Good", html=False)
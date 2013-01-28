import json
import unittest
import urllib2

from piui import PiUi

class PiUiTestCase(unittest.TestCase):

    def setUp(self):
        self._ui = PiUi("Test", timeout=1)

    def tearDown(self):
        print "tearDown"
        self._ui.exit()

    def http_get(self, rel_url):
        handler = urllib2.urlopen('http://localhost:9999/' + rel_url)
        return handler.getcode(), handler.read()

    def click(self):
        pass

    def test_menu(self):
        self.page = self._ui.new_ui_page(title="PiUi")
        self.list = self.page.add_list()
        self.list.add_item("Static Content", chevron=True, onclick=self.click)
        self.list.add_item("Buttons", chevron=True, onclick=self.click)
        self.list.add_item("Input", chevron=True, onclick=self.click)
        self.list.add_item("Images", chevron=True, onclick=self.click)
        self.list.add_item("Toggles", chevron=True, onclick=self.click)
        self.list.add_item("Console!", chevron=True, onclick=self.click)
        resp = self.http_get('/')
        assert "initPiUi();" in resp[1]
        resp = self.http_get('/init')
        assert "ok" in resp[1]
        resp = self.http_get('/poll')
        assert '"cmd": "newpage"' in resp[1]
        resp = self.http_get('/poll')
        assert '"cmd": "pagepost"' in resp[1]
        resp = self.http_get('/poll')
        assert '"cmd": "addul"' in resp[1]
        resp = self.http_get('/poll')
        assert '"cmd": "addli"' in resp[1]
        resp = self.http_get('/poll')
        assert '"cmd": "addli"' in resp[1]
        resp = self.http_get('/poll')
        assert '"cmd": "addli"' in resp[1]
        resp = self.http_get('/poll')
        assert '"cmd": "addli"' in resp[1]
        resp = self.http_get('/poll')
        assert '"cmd": "addli"' in resp[1]
        resp = self.http_get('/poll')
        assert '"cmd": "addli"' in resp[1]
        resp = self.http_get('/poll')
        assert '"cmd": "timeout"' in resp[1]


if __name__ == '__main__':
    unittest.main()
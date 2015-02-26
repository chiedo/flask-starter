from project.tests.test_base import BaseTestCase
from expects import *


class TestBasicPages(BaseTestCase):
    def test_index_basic(self):
        self.client.get("/")

        # Make sure the context variable is passed to the index page
        expect(self.get_context_variable("page")).to(equal("index"))

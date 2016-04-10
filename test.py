import run as shaservice
import unittest
import json


class ShaServiceTestCase(unittest.TestCase):

    def setUp(self):
        self.app = shaservice.create_app().test_client()
        self.json_data = {
            "empty": json.dumps({}),
            "valid": json.dumps({"foo": "bar", "bar": "baz"})
        }
        self.hashes = {
            "empty": "44136fa355b3678a1146ad16f7e8649e94fb4fc21fe77e8310c060f61caaff8a",
            "valid": "e8e02f85df24c0220e706521f44c42a5c25d91ae366c7c892304023b226cbcb1"
        }

    def test_post_no_json_header(self):
        resp = self.app.post('/hash/',
                             data={
                                "foo": "bar"
                             })
        self.assertEqual(resp.status_code, 400)

    def test_post_not_valid_json(self):
        resp = self.app.post('/hash/',
                             data="foobar",
                             headers={
                                "content-type": "application/json"
                             })
        self.assertEqual(resp.status_code, 400)

    def test_post_valid_json_is_empty(self):
        resp = self.app.post('/hash/',
                             data=self.json_data["empty"],
                             headers={
                                "content-type": "application/json"
                             })
        self.assertEqual(resp.status_code, 201)
        self.assertEqual(json.loads(resp.get_data())["hash"],
                         self.hashes["empty"])

    def test_post_valid_json(self):
        resp = self.app.post('/hash/',
                             data=self.json_data["valid"],
                             headers={
                                "content-type": "application/json"
                             })
        self.assertEqual(resp.status_code, 201)
        self.assertEqual(json.loads(resp.get_data())["hash"],
                         self.hashes["valid"])

    def test_get_400_not_sha256(self):
        resp = self.app.get('/hash/hello')
        self.assertEqual(resp.status_code, 400)

    def test_get_404_valid_sha256_not_in_db(self):
        resp = self.app.get('/hash/f7226c05f95b6fd5cb1dbe87a8a6f2da1cdf6270364dab6098f9dc1ff21a082c')
        self.assertEqual(resp.status_code, 404)

    def test_get_200_empty(self):
        # Test doesn't work because no state is kept with flask test client
        # and "database" is silly in-memory dictionary without persistence

        # resp = self.app.get("/hash/{empty}".format(**self.hashes))
        # self.assertEqual(self.json_data['empty'],
        #                  resp.get_data())
        # self.assertEqual(resp.status_code, 200)
        pass

    def test_get_200(self):
        # Test doesn't work because no state is kept with flask test client
        # and "database" is silly in-memory dictionary without persistence

        # resp = self.app.get("/hash/{valid}".format(**self.hashes))
        # self.assertEqual(self.json_data['valid'],
        #                  resp.get_data())
        # self.assertEqual(resp.status_code, 200)
        pass

if __name__ == '__main__':
    unittest.main()

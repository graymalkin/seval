import unittest

import seval
import seval.global_env

# Used to get to sys in test_no_sysver
import json

class EncapsulationTest(unittest.TestCase):
    def test_no_sysver(self):
        print(repr(seval.global_env))
        env = seval.global_env.globalenv
        env['json'] = json
        with self.assertRaises(Exception) as _:
            seval.seval.parse_string(env, "json.codecs.sys.version")

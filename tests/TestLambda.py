import json

import unittest

from src import Lambda

class TestLambda(unittest.TestCase):
    __context = None

    # Test para probar que la clase de Bancos y sus constantes no han cambiado con el layout del CCP
    def test_get_passive(self):
        event = {
            "mob_type": "passive"
        }

        passive = {'mob_type': ["Chicken", "Cow", "Horse", "Ocelot", "Pig", "Sheep",
         "Bat", "Mushroom", "Squid", "Villager"]}
        self.assertEqual(passive, Lambda.lambda_handler(event, self.__context))

    # Test para probar que la clase de Bancos y sus constantes no han cambiado con el layout del CCP
    def test_get_neutral(self):
        event = {
            "mob_type": "neutral"
        }

        neutral = {'mob_type': ["Cave Spider", "Enderman", "Spider", "Wolf",
                    "Zombie Pigman"]}
        self.assertEqual(neutral, Lambda.lambda_handler(event, self.__context))


    def test_get_boss_json(self):
        with open('boss.json') as data_file:
            event = json.load(data_file)

        boss = {'mob_type': ["Whither", "Ender Dragon"]}
        self.assertEqual(boss, Lambda.lambda_handler(event, self.__context))

if __name__ == '__main__':
    unittest.main()
import unittest
from src.active_pipelines import find_connection_with_storages, build_graph


class MyTestCase(unittest.TestCase):
    def test_connection_with_graph1(self):
        storages = ['Сховище_1', 'Сховище_2']
        cities = ['Львів', 'Стрий', 'Долина']
        active_gas_pipeline = [['Львів', 'Стрий'], ['Долина', 'Львів'], ['Сховище_1', 'Сховище_2']]

        result = find_connection_with_storages(active_gas_pipeline, storages, cities)
        self.assertEqual([['Сховище_1', ['Львів', 'Стрий', 'Долина']], ['Сховище_2', ['Львів', 'Стрий', 'Долина']]]
                         , result)

    def test_connection_with_graph2(self):


        storages = ['Сховище_1', 'Сховище_2']
        cities = ['Львів', 'Стрий', 'Долина']
        active_gas_pipeline = [['Львів', 'Стрий'], ['Долина', 'Львів', 'Житомир'], ['Сховище_1', 'Долина'],
                               ['Сховище_2', 'Долина']]

        result = find_connection_with_storages(active_gas_pipeline, storages, cities)
        self.assertEqual([['Сховище_1', []], ['Сховище_2', []]]
                         , result)


if __name__ == '__main__':
    unittest.main()

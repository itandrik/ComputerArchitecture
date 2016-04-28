import sys
import argparse
from model import Model
from view import View
from serialize import Serialize


class ControllerArgs:
    def __init__(self):
        self.parser = self._create_parser()
        self.view = View()
        self.serialize = Serialize()

    def _create_parser(self):
        parser = argparse.ArgumentParser(
            prog='Calories calculator',
            description='''Use this program to know quantity
             of calories you spend per day''',
            epilog='''(c) Chersilmuk inc.'''
        )
        group = parser.add_argument_group(title='Parameters')
        group.add_argument('--gender', '-g',
                           required=True,
                           choices=[1, 2],
                           type=int,
                           metavar='|1 - MALE, 2 - FEMALE|')
        group.add_argument('--activity',
                           '-pa',
                           required=True,
                           choices=[1, 2, 3, 4, 5],
                           type=int,
                           metavar='|Physical activity :'
                                   ' 1 - Minimum physical activity'
                                   '2 - 3 times per week '
                                   '3 - 5 times per week'
                                   '4 - Every day 5 - 2 times per day|')
        group.add_argument('--weight', '-w',
                           required=True,
                           choices=range(35, 239, 1),
                           type=int,
                           metavar='|WEIGHT >34 and <240|')
        group.add_argument('--height',
                           '-ht',
                           required=True,
                           choices=range(120, 249, 1),
                           type=int,
                           metavar='|HEIGHT >119 and <250|')
        group.add_argument('--age',
                           '-a',
                           required=True,
                           choices=range(13, 79, 1),
                           type=int,
                           metavar='|AGE >12 and <80|')
        return parser

    def parse(self):
        namespace = self.parser.parse_args(sys.argv[1:])
        model=Model()
        calories = model.calculate_calories(namespace.gender,
                                            namespace.weight,
                                            namespace.height,
                                            namespace.age,
                                            namespace.activity)
        self.view.get_info(calories)
        data = (namespace.gender, namespace.weight,
                namespace.height, namespace.age,
                namespace.activity, calories)
        input()
        if self.view.is_dump():
            self.serialize.dump(data)

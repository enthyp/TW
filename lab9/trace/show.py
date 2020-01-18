import os
import argparse
from pprint import pprint
from traces import System, MinDependenceGraph, trace, fnf

package_dir = os.path.dirname(os.path.realpath(__file__))
test_input = os.path.join(package_dir, 'tests', 'in')
input_config = [  # should be in config file but come on
    {
        'system_source': 'system1.txt',
        'from_ind': True,
        'word': 'baadcb'
    },
    {
        'system_source': 'system2.txt',
        'from_ind': True,
        'word': 'acdcfbbe'
    },
    {
        'system_source': 'system3.txt',
        'from_ind': False,
        'word': 'acebdac'
    }
]

class Runner:
    def __init__(self, input_config):
        self.input_config = input_config
        self.tasks = {
            1: show_dependence,
            2: show_trace,
            3: show_foata,
            4: show_graph,
            5: show_fnf_from_graph
        }

    def run(self, task_no):
        for n, config in enumerate(self.input_config):
            system = self._system(config)

            print('System {}:'.format(n + 1))
            t = self.tasks[task_no]
            t(system, config['word'])
            print()

    def _system(self, config):
        input_path = os.path.join(test_input, config['system_source'])
        return System(input_path, config['from_ind'])


def show_dependence(system, word):
    pprint(system.dep_relation)

def show_trace(system, word):
    pprint(trace(word, system))

def show_foata(system, word):
    pprint(fnf(word, system))

def show_graph(system, word):
    graph = MinDependenceGraph(word, system)
    graph.render('graph_' + word, show=True)

def show_fnf_from_graph(system, word):
    graph = MinDependenceGraph(word, system)
    pprint(graph.fnf())

def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('-t', default=1, type=int, help='choose the task number 1-5')
    args = parser.parse_args()    
    
    if not args.t in set(range(1, 6)):
        parser.error('1-5 are valid task numbers')
    else:
        return args.t

def main():
    runner = Runner(input_config)
    task_no = parse_args()
    runner.run(task_no)


if __name__ == '__main__':
    main()


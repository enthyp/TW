import os
import argparse
from pprint import pprint
from traces import System, MinDependenceGraph, trace, fnf

package_dir = os.path.dirname(os.path.realpath(__file__))
test_input = os.path.join(package_dir, 'tests', 'in')

# Should have a Config class, be read from config file but come on...
input_config = [  
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


class Task:
    def __init__(self, id, config):
        self.id = id
        self.system = self._system(config)
        self.word = config['word']

    def _system(self, config):
        input_path = os.path.join(test_input, config['system_source'])
        return System(input_path, config['from_ind'])

    def _show(self, result):
        print('System {}: '.format(self.id))
        pprint(result)
               
    def run(self):
        raise NotImplementedError


class Dependence(Task):
    def run(self):
        self._show(self.system.dep_relation)

class Trace(Task):
    def run(self):
        self._show(trace(self.word, self.system))

class Foata(Task):
    def run(self):
        self._show(fnf(self.word, self.system))

class Graph(Task):
    def run(self):
        graph = MinDependenceGraph(self.word, self.system)
        graph.render('graph_{}'.format(self.word), show=True)
      
class FNFFromGraph(Task):
    def run(self):
     graph = MinDependenceGraph(self.word, self.system)
     self._show(graph.fnf())

  
class Runner:
    def __init__(self, input_config):
        self.input_config = input_config
        self.tasks = {
            1: Dependence,
            2: Trace,
            3: Foata,
            4: Graph,
            5: FNFFromGraph
        }

    def run(self, task_no):
        for id, config in enumerate(self.input_config):
            t = self.tasks[task_no](id, config)
            t.run()


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


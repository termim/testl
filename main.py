import numpy as np
import pytest
import cProfile
import logging
from matrix_mult_tester import matrix_multiplier_tester
from obtain_input import obtain_input, print_matricies
from matrix_multiplier import matrix_multiplier

logging.basicConfig(format='%(asctime)s - %(message)s', level=logging.INFO)
logging.info('This program was utilized')

def main():
    matrix_multiplier_tester(a, b)


if __name__ == '__main__':
    cProfile.run('main()')
    matrix_multiplier_tester(a, b)
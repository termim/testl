import pytest
import cProfile
import logging
import tracemalloc
from matrix_mult_tester import matrix_multiplier_tester
from obtain_input import obtain_input_mats, print_matricies
from matrix_multiplier import matrix_multiplier

logging.basicConfig(format='%(asctime)s - %(message)s', level=logging.INFO)
logging.info('This program was utilized')


def main():
    tracemalloc.start()
    matrix1, matrix2 = obtain_input_mats()
    assert (matrix1 == matrix2)
    print_matricies(matrix1, matrix2)
    matrix_multiplier_tester(matrix1, matrix2)
    result = matrix_multiplier(matrix1, matrix2)
    res_print(result)
    snapshot = tracemalloc.take_snapshot()
    top_stats = snapshot.statistics('lineno')
    print("[ Top 10 ]")
    for stat in top_stats[:10]:
        print(stat)


cProfile.run('main()')
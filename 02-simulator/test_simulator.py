import simulator as sim
from gates import *

def assert_eq(a, b):
    assert a == b, "Expected {}, got {}".format(b, a)

def test_or():
    nodes = [Input('a'), Input('b'), Or('or_1'), Output('c')]
    edges = [('a', 'or_1'), ('b', 'or_1'), ('or_1', 'c')]

    for a in [0, 1]:
        for b in [0, 1]:
            inputs = {'a': a, 'b': b}
            outputs = sim.simulate(nodes, edges, inputs)
            assert_eq(outputs['c'], a | b)
  
def test_and():
    nodes = [Input('a'), Input('b'), And('and_1'), Output('c')]
    edges = [('a', 'and_1'), ('b', 'and_1'), ('and_1', 'c')]

    for a in [0, 1]:
        for b in [0, 1]:
            inputs = {'a': a, 'b': b}
            outputs = sim.simulate(nodes, edges, inputs)
            assert_eq(outputs['c'], a & b)

def test_not():
    nodes = [Input('a'), Not('not_1'), Output('c')]
    edges = [('a', 'not_1'), ('not_1', 'c')]

    for a in [0, 1]:
        inputs = {'a': a}
        outputs = sim.simulate(nodes, edges, inputs)
        assert_eq(outputs['c'], 1 - a)

def test_xor():
    nodes = [Input('a'), Input('b'), Xor('xor_1'), Output('c')]
    edges = [('a', 'xor_1'), ('b', 'xor_1'), ('xor_1', 'c')]

    for a in [0, 1]:
        for b in [0, 1]:
            inputs = {'a': a, 'b': b}
            outputs = sim.simulate(nodes, edges, inputs)
            assert_eq(outputs['c'], a ^ b)

def test_mux_2_1():
    nodes = [
        Input('a'), Input('b'), Input('s'),
        Not('not_1'), And('and_1'), And('and_2'), Or('or_1'),
        Output('z')
    ]
    edges = [
        ('s', 'not_1'), 
        ('not_1', 'and_1'), ('a', 'and_1'),
        ('s', 'and_2'), ('b', 'and_2'),
        ('and_1', 'or_1'), ('and_2', 'or_1'),
        ('or_1', 'z')
    ]

    for a in [0, 1]:
        for b in [0, 1]:
            for s in [0, 1]:
                inputs = {'a': a, 'b': b, 's': s}
                outputs = sim.simulate(nodes, edges, inputs)
                assert_eq(outputs['z'], (a & ~s) | (b & s))


def test_demux_1_2():
    nodes = [
        Input('z'), Input('s'),
        Not('not_1'), And('and_1'), And('and_2'),
        Output('a'), Output('b')
    ]
    edges = [
        ('s', 'not_1'),
        ('not_1', 'and_1'), ('z', 'and_1'),
        ('s', 'and_2'), ('z', 'and_2'),
        ('and_1', 'a'),
        ('and_2', 'b')
    ]

    for z in [0, 1]:
        for s in [0, 1]:
            inputs = {'z': z, 's': s}
            outputs = sim.simulate(nodes, edges, inputs)
            assert_eq(outputs['a'], z & ~s)
            assert_eq(outputs['b'], z & s)

def test_half_adder():
    nodes = [
        Input('a'), Input('b'),
        Xor('xor_1'), And('and_1'),
        Output('s'), Output('c')
    ]
    edges = [
        ('a', 'xor_1'), ('b', 'xor_1'),
        ('a', 'and_1'), ('b', 'and_1'),
        ('xor_1', 's'), ('and_1', 'c')
    ]

    for a in [0, 1]:
        for b in [0, 1]:
            inputs = {'a': a, 'b': b}
            outputs = sim.simulate(nodes, edges, inputs)
            assert_eq(outputs['s'], a ^ b)
            assert_eq(outputs['c'], a & b)

def test_full_adder():
    nodes = [
        Input('a'), Input('b'), Input('c_in'),
        Xor('xor_1'), Xor('xor_2'), And('and_1'), And('and_2'), Or('or_1'),
        Output('s'), Output('c_out')
    ]
    edges = [
        ('a', 'xor_1'), ('b', 'xor_1'), # xor_1
        ('xor_1', 'xor_2'), ('c_in', 'xor_2'), # xor_2
        ('c_in', 'and_1'), ('xor_1', 'and_1'), # and_1
        ('a', 'and_2'), ('b', 'and_2'), # and_2
        ('and_1', 'or_1'), ('and_2', 'or_1'), # or_1
        ('xor_2', 's'), # S
        ('or_1', 'c_out'), # C_out
    ]

    for a in [0, 1]:
        for b in [0, 1]:
            for c_in in [0, 1]:
                inputs = {'a': a, 'b': b, 'c_in': c_in}
                outputs = sim.simulate(nodes, edges, inputs)
                assert_eq(outputs['s'], a ^ b ^ c_in)
                assert_eq(outputs['c_out'], ((a ^ b) & c_in) | (a & b))

def test_4_1_mux():
    # TODO: Write out nodes and edges and test all possible inputs

    # remove this assert when you start working on it
    assert False, "Not implemented yet!"


if __name__ == '__main__':
    tests = [
        test_or,
        test_and,
        test_not,
        test_xor,
        test_mux_2_1,
        test_demux_1_2,
        test_half_adder,
        test_full_adder,

        # TODO: Implement the rest of the tests
        test_4_1_mux,
    ]
 
    for test in tests:
        try:
            test()
            print('.', end='', flush=True)

        except AssertionError:
            raise
    print()
    print('All tests passed!')


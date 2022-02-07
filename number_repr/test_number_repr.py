import number_repr as nr

def assert_eq(a, b):
    assert a == b, "Expected {}, got {}".format(b, a)


def test_to_unsigned_binary_from_dec():
    assert_eq(nr.to_unsigned_binary_from_dec(0), [0, 0, 0, 0, 0, 0, 0, 0])
    assert_eq(nr.to_unsigned_binary_from_dec(1), [0, 0, 0, 0, 0, 0, 0, 1])
    assert_eq(nr.to_unsigned_binary_from_dec(231), [1, 1, 1, 0, 0, 1, 1, 1])

def test_to_sign_mag_binary_from_dec():
    assert_eq(nr.to_sign_mag_binary_from_dec(0), [0, 0, 0, 0, 0, 0, 0, 0])
    assert_eq(nr.to_sign_mag_binary_from_dec(1), [0, 0, 0, 0, 0, 0, 0, 1])
    assert_eq(nr.to_sign_mag_binary_from_dec(-15), [1, 0, 0, 0, 1, 1, 1, 1])
    assert_eq(nr.to_sign_mag_binary_from_dec(-113), [1, 1, 1, 1, 0, 0, 0, 1])

def test_to_ones_comp_binary_from_dec():
    assert_eq(nr.to_ones_comp_binary_from_dec(0), [0, 0, 0, 0, 0, 0, 0, 0])
    assert_eq(nr.to_ones_comp_binary_from_dec(1), [0, 0, 0, 0, 0, 0, 0, 1])
    assert_eq(nr.to_ones_comp_binary_from_dec(-15), [1, 1, 1, 1, 0, 0, 0, 0])
    assert_eq(nr.to_ones_comp_binary_from_dec(-113), [1, 0, 0, 0, 1, 1, 1, 0])

def test_to_twos_comp_binary_from_dec():
    assert_eq(nr.to_twos_comp_binary_from_dec(0), [0, 0, 0, 0, 0, 0, 0, 0])
    assert_eq(nr.to_twos_comp_binary_from_dec(1), [0, 0, 0, 0, 0, 0, 0, 1])
    assert_eq(nr.to_twos_comp_binary_from_dec(-15), [1, 1, 1, 1, 0, 0, 0, 1])
    assert_eq(nr.to_twos_comp_binary_from_dec(-113), [1, 0, 0, 0, 1, 1, 1, 1])

def test_binary_add_unsigned():
    assert_eq(nr.binary_add_unsigned([0, 0, 0, 0, 0, 0, 0, 0],
                                     [0, 0, 0, 0, 0, 0, 0, 0]),
                                     [0, 0, 0, 0, 0, 0, 0, 0])
    assert_eq(nr.binary_add_unsigned([0, 0, 0, 0, 0, 0, 0, 1],
                                     [0, 0, 0, 0, 0, 0, 0, 0]),
                                     [0, 0, 0, 0, 0, 0, 0, 1])
    assert_eq(nr.binary_add_unsigned([0, 0, 0, 0, 1, 0, 1, 1],
                                     [0, 0, 0, 0, 0, 0, 1, 0]),
                                     [0, 0, 0, 0, 1, 1, 0, 1])
    assert_eq(nr.binary_add_unsigned([0, 0, 1, 1, 1, 0, 1, 1],
                                     [1, 0, 0, 0, 0, 0, 1, 0]),
                                     [1, 0, 1, 1, 1, 1, 0, 1])

def test_binary_add_ones_comp():
    assert_eq(nr.binary_add_ones_comp([0, 0, 0, 0, 0, 0, 0, 0],
                                      [0, 0, 0, 0, 0, 0, 0, 0]),
                                      [0, 0, 0, 0, 0, 0, 0, 0])
    assert_eq(nr.binary_add_ones_comp([1, 0, 1, 1, 1, 0, 1, 1],
                                      [0, 1, 0, 0, 0, 1, 0, 0]),
                                      [1, 1, 1, 1, 1, 1, 1, 1])
    assert_eq(nr.binary_add_ones_comp([1, 1, 0, 1, 1, 0, 1, 1],
                                      [1, 1, 0, 0, 1, 1, 0, 0]),
                                      [1, 0, 1, 0, 1, 0, 0, 0])

def test_binary_add_twos_comp():
    assert_eq(nr.binary_add_twos_comp([0, 0, 0, 0, 0, 0, 0, 0],
                                      [0, 0, 0, 0, 0, 0, 0, 0]),
                                      [0, 0, 0, 0, 0, 0, 0, 0])
    assert_eq(nr.binary_add_twos_comp([0, 0, 0, 0, 0, 0, 0, 1],
                                      [0, 0, 0, 0, 0, 0, 0, 0]),
                                      [0, 0, 0, 0, 0, 0, 0, 1])
    assert_eq(nr.binary_add_twos_comp([0, 0, 0, 0, 1, 0, 1, 1],
                                      [0, 0, 0, 0, 0, 0, 1, 0]),
                                      [0, 0, 0, 0, 1, 1, 0, 1])
    assert_eq(nr.binary_add_twos_comp([0, 0, 1, 1, 1, 0, 1, 1],
                                      [1, 0, 0, 0, 0, 0, 1, 0]),
                                      [1, 0, 1, 1, 1, 1, 0, 1])

def test_to_dec_from_ones_comp_binary():
    # test zero
    assert_eq(nr.to_dec_from_ones_comp_binary([0, 0, 0, 0, 0, 0, 0, 0]), 0)

    # test positive
    assert_eq(nr.to_dec_from_ones_comp_binary([0, 0, 0, 0, 0, 0, 0, 1]), 1)
    assert_eq(nr.to_dec_from_ones_comp_binary([0, 0, 0, 0, 0, 0, 1, 0]), 2)
    assert_eq(nr.to_dec_from_ones_comp_binary([0, 1, 0, 0, 0, 1, 1, 1]), 71)

    # test negative
    assert_eq(nr.to_dec_from_ones_comp_binary([1, 1, 1, 1, 1, 0, 1, 0]), -5)
    assert_eq(nr.to_dec_from_ones_comp_binary([1, 1, 1, 1, 1, 0, 0, 1]), -6)
    assert_eq(nr.to_dec_from_ones_comp_binary([1, 0, 0, 1, 0, 0, 0, 0]), -111)

def test_to_dec_from_twos_comp_binary():
    # test zero
    assert_eq(nr.to_dec_from_twos_comp_binary([0, 0, 0, 0, 0, 0, 0, 0]), 0)

    # test positive
    assert_eq(nr.to_dec_from_twos_comp_binary([0, 0, 0, 0, 0, 0, 0, 1]), 1)
    assert_eq(nr.to_dec_from_twos_comp_binary([0, 0, 0, 0, 0, 0, 1, 0]), 2)
    assert_eq(nr.to_dec_from_twos_comp_binary([0, 1, 0, 0, 0, 1, 1, 1]), 71)

    # test negative
    assert_eq(nr.to_dec_from_twos_comp_binary([1, 1, 1, 1, 1, 0, 1, 1]), -5)
    assert_eq(nr.to_dec_from_twos_comp_binary([1, 1, 1, 1, 1, 0, 1, 0]), -6)
    assert_eq(nr.to_dec_from_twos_comp_binary([1, 0, 0, 1, 0, 0, 0, 1]), -111)

def test_to_dec_from_sign_mag_binary():
    # test zero
    assert_eq(nr.to_dec_from_sign_mag_binary([0, 0, 0, 0, 0, 0, 0, 0]), 0)

    # test positive
    assert_eq(nr.to_dec_from_sign_mag_binary([0, 0, 0, 0, 0, 0, 0, 1]), 1)
    assert_eq(nr.to_dec_from_sign_mag_binary([0, 0, 0, 0, 0, 0, 1, 0]), 2)
    assert_eq(nr.to_dec_from_sign_mag_binary([0, 1, 0, 0, 0, 1, 1, 1]), 71)

    # test negative
    assert_eq(nr.to_dec_from_sign_mag_binary([1, 1, 1, 1, 1, 0, 1, 0]), -122)
    assert_eq(nr.to_dec_from_sign_mag_binary([1, 1, 1, 1, 1, 0, 0, 1]), -121)
    assert_eq(nr.to_dec_from_sign_mag_binary([1, 0, 0, 1, 0, 0, 0, 0]), -16)

def test_to_dec_from_unsigned_binary():
    # test zero
    assert_eq(nr.to_dec_from_unsigned_binary([0, 0, 0, 0, 0, 0, 0, 0]), 0)

    # test positive
    assert_eq(nr.to_dec_from_unsigned_binary([0, 0, 0, 0, 0, 0, 0, 1]), 1)
    assert_eq(nr.to_dec_from_unsigned_binary([0, 0, 0, 0, 0, 0, 1, 0]), 2)
    assert_eq(nr.to_dec_from_unsigned_binary([0, 1, 0, 0, 0, 1, 1, 1]), 71)
    assert_eq(nr.to_dec_from_unsigned_binary([1, 1, 1, 1, 1, 0, 1, 0]), 250)
    assert_eq(nr.to_dec_from_unsigned_binary([1, 1, 1, 1, 1, 0, 1, 1]), 251)
    assert_eq(nr.to_dec_from_unsigned_binary([1, 0, 0, 1, 0, 0, 0, 1]), 145)


def test_unsigned_conv_full():
    from_bin = nr.to_dec_from_unsigned_binary
    to_bin = nr.to_unsigned_binary_from_dec
    for n in range(0, 256):
        assert_eq(from_bin(to_bin(n)), n)


def test_sign_mag_conv_full():
    from_bin = nr.to_dec_from_sign_mag_binary
    to_bin = nr.to_sign_mag_binary_from_dec
    for n in range(-127, 128):
        assert_eq(from_bin(to_bin(n)), n)


def test_ones_comp_conv_full():
    from_bin = nr.to_dec_from_ones_comp_binary
    to_bin = nr.to_ones_comp_binary_from_dec
    for n in range(-127, 128):
        assert_eq(from_bin(to_bin(n)), n)


def test_twos_comp_conv_full():
    from_bin = nr.to_dec_from_twos_comp_binary
    to_bin = nr.to_twos_comp_binary_from_dec
    for n in range(-128, 128):
        assert_eq(from_bin(to_bin(n)), n)


def test_add_unsigned_full():
    from_bin = nr.to_dec_from_unsigned_binary
    to_bin = nr.to_unsigned_binary_from_dec
    add_fn = nr.binary_add_unsigned
    for n in range(0, 256):
        for m in range(0, 256):
            if n + m < 256:
                assert_eq(from_bin(add_fn(to_bin(n), to_bin(m))), n + m)


def test_add_ones_comp_full():
    from_bin = nr.to_dec_from_ones_comp_binary
    to_bin = nr.to_ones_comp_binary_from_dec
    add_fn = nr.binary_add_ones_comp
    for n in range(-127, 128):
        for m in range(-127, 128):
            if n + m > -128 and n + m < 128:
                assert_eq(from_bin(add_fn(to_bin(n), to_bin(m))), n + m)


def test_add_twos_comp_full():
    from_bin = nr.to_dec_from_twos_comp_binary
    to_bin = nr.to_twos_comp_binary_from_dec
    add_fn = nr.binary_add_twos_comp
    for n in range(-128, 128):
        for m in range(-128, 128):
            if n + m > -128 and n + m < 128:
                assert_eq(from_bin(add_fn(to_bin(n), to_bin(m))), n + m)


if __name__ == '__main__':
    tests = [
        # Decimal to Binary
        test_to_unsigned_binary_from_dec,
        test_to_sign_mag_binary_from_dec,
        test_to_ones_comp_binary_from_dec,
        test_to_twos_comp_binary_from_dec,
        # Binary Addition
        test_binary_add_unsigned,
        test_binary_add_ones_comp,
        test_binary_add_twos_comp,
        # Binary to Decimal
        test_to_dec_from_unsigned_binary,
        test_to_dec_from_sign_mag_binary,
        test_to_dec_from_ones_comp_binary,
        test_to_dec_from_twos_comp_binary,

        # Tests all possible conversions (8-bit)
        test_unsigned_conv_full,
        test_sign_mag_conv_full,
        test_ones_comp_conv_full,
        test_twos_comp_conv_full,

        # Tests all possible additions (8-bit); no-overflow
        test_add_unsigned_full,
        test_add_ones_comp_full,
        test_add_twos_comp_full,
    ]

    for test in tests:
        try:
            test()
            print('.', end='', flush=True)

        except AssertionError:
            raise
    print()
    print('All tests passed!')

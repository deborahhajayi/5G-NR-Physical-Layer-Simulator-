import numpy as np
import pytest

from src.modulation.qpsk import qpsk_modulate, qpsk_demodulate


def test_qpsk_modulation_and_demodulation():

    bits = np.array([0, 0, 0, 1, 1, 0, 1, 1])

    symbols = qpsk_modulate(bits)
    recovered_bits = qpsk_demodulate(symbols)

    assert np.array_equal(bits, recovered_bits)


def test_qpsk_symbol_count():

    bits = np.random.randint(0, 2, 100)

    symbols = qpsk_modulate(bits)

    assert len(symbols) == 50
h

def test_odd_number_of_bits():

    bits = np.array([0, 1, 0])

    with pytest.raises(ValueError):
        qpsk_modulate(bits)
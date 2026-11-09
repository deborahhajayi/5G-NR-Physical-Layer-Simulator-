import numpy as np


def qpsk_modulate(bits):
    """
    Convert binary data into QPSK symbols.

    Each pair of bits represents one QPSK symbol.
    """

    if len(bits) % 2 != 0:
        raise ValueError("Number of bits must be even.")

    if not np.all(np.isin(bits, [0, 1])):
        raise ValueError("Input must contain only 0s and 1s.")

    # Reshape bits into pairs
    bit_pairs = bits.reshape(-1, 2)

    # Map bits to I and Q components
    i_component = 1 - 2 * bit_pairs[:, 0]
    q_component = 1 - 2 * bit_pairs[:, 1]

    # Create complex QPSK symbols
    symbols = (i_component + 1j * q_component) / np.sqrt(2)

    return symbols


def qpsk_demodulate(symbols):
    """
    Convert QPSK symbols back into binary data.
    """

    bits = np.zeros((len(symbols), 2), dtype=int)

    # Recover the original bits using the sign of I and Q
    bits[:, 0] = (symbols.real < 0).astype(int)
    bits[:, 1] = (symbols.imag < 0).astype(int)

    return bits.flatten()
import numpy as np

from src.modulation.qpsk import qpsk_modulate, qpsk_demodulate
from src.modulation.plot_constellation import plot_constellation

def main():

    # Generate random binary data
    num_bits = 1000
    bits = np.random.randint(0, 2, num_bits)

    # Modulate the bits
    symbols = qpsk_modulate(bits)

    # Demodulate the symbols
    recovered_bits = qpsk_demodulate(symbols)

    # Plot the constellation diagram
    plot_constellation(symbols)

    # Verify transmission
    print("5G NR Physical Layer Simulator")
    print("--------------------------------")
    print(f"Original bits: {len(bits)}")
    print(f"Generated QPSK symbols: {len(symbols)}")
    print(f"Recovered bits: {len(recovered_bits)}")

    print("\nTransmission successful:",
          np.array_equal(bits, recovered_bits))


if __name__ == "__main__":
    main()
import matplotlib.pyplot as plt
import numpy as np


def plot_constellation(symbols):

    plt.figure(figsize=(7, 7))

    plt.scatter(
        symbols.real,
        symbols.imag,
        alpha=0.5,
        label="QPSK Symbols"
    )

    plt.axhline(0, linewidth=0.8)
    plt.axvline(0, linewidth=0.8)

    plt.xlabel("In-phase (I)")
    plt.ylabel("Quadrature (Q)")
    plt.title("QPSK Constellation Diagram")

    plt.grid(True)
    plt.axis("equal")
    plt.legend()

    plt.show()
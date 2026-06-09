"""
Quantum AI Module

هذه الوحدة توفر أدوات وخوارزميات للذكاء الاصطناعي الكمومي
"""

__version__ = "0.1.0"
__author__ = "Moumou097"

from .quantum_neural_network import QuantumNeuralNetwork
from .quantum_classifier import QuantumClassifier

__all__ = [
    "QuantumNeuralNetwork",
    "QuantumClassifier",
]

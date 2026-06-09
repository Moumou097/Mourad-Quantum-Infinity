#!/usr/bin/env python3
"""
مثال رئيسي للمشروع Mourad Quantum Infinity

هذا البرنامج يوضح كيفية استخدام جميع المكونات الثلاثة:
- الذكاء الاصطناعي الكمومي
- الحوسبة الكمومية
- الأمان السيبراني الكمومي
"""

import sys
from quantum_ai import QuantumNeuralNetwork
from quantum_computing import QuantumCircuit
from quantum_security import PostQuantumCrypto, QuantumKeyDistribution
import numpy as np


def demo_quantum_ai():
    """عرض توضيحي للذكاء الاصطناعي الكمومي"""
    print("\n" + "="*60)
    print("🤖 1. الذكاء الاصطناعي الكمومي")
    print("="*60)
    
    qnn = QuantumNeuralNetwork(n_qubits=4, n_layers=2)
    print("✓ تم إنشاء شبكة عصبية كمومية")
    
    X = np.random.randn(10, 4)
    y = np.random.randint(0, 2, 10)
    qnn.train(X, y, epochs=5)
    
    predictions = qnn.predict(X[:3])
    print(f"✓ التنبؤات: {predictions}")


def demo_quantum_computing():
    """عرض توضيحي للحوسبة الكمومية"""
    print("\n" + "="*60)
    print("⚛️ 2. الحوسبة الكمومية")
    print("="*60)
    
    qc = QuantumCircuit(n_qubits=3)
    print("✓ تم إنشاء دارة كمومية")
    
    qc.add_h_gate(0)
    qc.add_cnot_gate(0, 1)
    print("✓ تم إضافة البوابات الكمومية")
    
    results = qc.measure(shots=100)
    print(f"✓ نتائج القياس: {len(results)} حالات مختلفة")


def demo_quantum_security():
    """عرض توضيحي للأمان السيبراني الكمومي"""
    print("\n" + "="*60)
    print("🔐 3. الأمان السيبراني الكمومي")
    print("="*60)
    
    # التشفير ما بعد الكمومي
    message = b"رسالة سرية"
    pqc = PostQuantumCrypto()
    hash_val = pqc.generate_hash(message)
    print(f"✓ تم تشفير الرسالة: {hash_val[:16]}...")
    
    # توزيع المفاتيح الكمومية
    qkd = QuantumKeyDistribution(n_qubits=128)
    shared_key, _ = qkd.bb84_protocol()
    is_secure = qkd.validate_channel()
    print(f"✓ توزيع المفاتيح: آمن = {is_secure}")


def main():
    """البرنامج الرئيسي"""
    print("\n" + "∞" * 30)
    print("     MOURAD QUANTUM INFINITY")
    print("    منصة الذكاء الاصطناعي الكمومي")
    print("∞" * 30)
    
    try:
        demo_quantum_ai()
        demo_quantum_computing()
        demo_quantum_security()
        
        print("\n" + "="*60)
        print("✅ اكتملت جميع العروض التوضيحية بنجاح!")
        print("="*60 + "\n")
        
    except Exception as e:
        print(f"\n❌ حدث خطأ: {e}")
        return 1
    
    return 0


if __name__ == "__main__":
    sys.exit(main())

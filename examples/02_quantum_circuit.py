"""
مثال: دارة كمومية بسيطة

هذا المثال يوضح كيفية إنشاء واستخدام دارة كمومية
"""

import numpy as np
from quantum_computing import QuantumCircuit


def main():
    print("="*50)
    print("مثال: دارة كمومية بسيطة")
    print("="*50)
    
    # إنشاء دارة كمومية
    qc = QuantumCircuit(n_qubits=3)
    print(f"✓ تم إنشاء دارة كمومية بـ 3 كيوبتات")
    
    # إضافة بوابات
    print(f"\n📊 إضافة البوابات...")
    qc.add_h_gate(0)
    qc.add_h_gate(1)
    qc.add_cnot_gate(0, 1)
    qc.add_cnot_gate(1, 2)
    qc.add_rx_gate(0, np.pi / 4)
    
    # عرض الدارة
    print(f"\n🔬 الدارة الكمومية:")
    qc.display_circuit()
    
    # قياس الدارة
    print(f"\n📏 قياس الدارة (1000 مرة)...")
    results = qc.measure(shots=1000)
    print(f"  - النتائج:")
    for state, count in sorted(results.items(), key=lambda x: x[1], reverse=True)[:5]:
        percentage = (count / 1000) * 100
        print(f"    |{state}⟩: {count} مرة ({percentage:.1f}%)")
    
    print(f"\n" + "="*50)
    print("✓ انتهى المثال بنجاح!")
    print("="*50)


if __name__ == "__main__":
    main()

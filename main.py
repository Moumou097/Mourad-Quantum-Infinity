import sys
import time
import os
from src.models import CosmicMessage, CosmicResponse
from src.engine import CommunicationEngine

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def main():
    engine = CommunicationEngine()
    
    print("\n" + "∞" * 60)
    print("    COSMIC COMMUNICATION PROJECT - [PROJECT EXECUTION]")
    print("         نظام التواصل الكوني - من الخيال إلى التنفيذ")
    print("    🚀 TRANSCENDING ALL PHYSICAL LIMITATIONS")
    print("∞" * 60 + "\n")
    
    print("💡 [INFO]: تم تفعيل محرك التواصل الكوني.")
    print("💡 [INFO]: جاري تهيئة بوابات الأكوان والمجرات...")
    time.sleep(1)
    print("💡 [INFO]: النظام جاهز تماماً للاستخدام.\n")
    
    while True:
        try:
            print("-" * 60)
            user_input = input("🌌 أدخل رسالتك الكونية (أو 'خروج' للإنهاء): ").strip()
            
            if user_input.lower() in ['خروج', 'exit', 'quit']:
                print("\n🌟 [SESSION ENDED]: جاري إغلاق بوابات التواصل...")
                time.sleep(1)
                print("∞🌌 الكون ينتظر رسالتكم القادمة... 🌌∞\n")
                break
            
            if not user_input:
                continue
            
            # 1. إنشاء الرسالة
            message = CosmicMessage(content=user_input)
            print(f"\n📤 [إرسال]: جاري تشفير الرسالة (التشابك الكمي)...")
            encrypted = engine.simulate_entanglement(user_input)
            print(f"🔒 [تشفير]: {encrypted[:15]}... (Quantum Secure)")
            
            # 2. معالجة الإرسال والحصول على رد
            print("📡 [بث]: يتم الآن البث عبر 156 حضارة كونية...")
            response = engine.process_message(message)
            
            # 3. عرض الرد الكوني
            print("\n" + "=" * 40)
            print(f"📥 [رد وارد]: {response.content}")
            print(f"📍 [المصدر]: {response.universe_origin}")
            print(f"⏰ [التوقيت]: {response.timestamp.strftime('%H:%M:%S')}")
            print("=" * 40 + "\n")
            
        except KeyboardInterrupt:
            print("\n\n🌟 تم إغلاق النظام يدوياً.")
            break
        except Exception as e:
            print(f"\n❌ [خطأ في النظام]: {e}")

if __name__ == "__main__":
    main()

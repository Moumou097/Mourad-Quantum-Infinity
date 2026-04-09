import sys
import time
import os
import socket
from src.network import CosmicNode

def main():
    # 1. إعداد العقدة المحلية (الخادم)
    local_port = 9999
    if len(sys.argv) > 1:
        try:
            local_port = int(sys.argv[1])
        except:
            pass
            
    node = CosmicNode(port=local_port)
    node.start_receiver()
    
    print("\n" + "∞" * 60)
    print("    HYPERBOLOID COSMIC NETWORK - [DIMENSIONAL MESH]")
    print("         نظام التواصل الهايبربولويدي - شبكة الأبعاد المتشابكة")
    print("    🚀 INTEGRATED QUANTUM & GEOMETRIC CONNECTIVITY")
    print("∞" * 60 + "\n")
    
    print(f"💡 [INFO]: عنوانك البعدي: {socket.gethostbyname(socket.gethostname())}:{local_port}")
    print(f"💡 [GEOM]: إحداثيات السرج: Z = {node.z_coord:.4f}")
    print("💡 [INFO]: بوابات الأبعاد مفتوحة لاستقبال الإشارات...")
    
    target_host = "127.0.0.1"
    target_port = 9999
    
    while True:
        try:
            print("-" * 60)
            user_input = input("🌌 أدخل رسالتك الكونية (أو 'خروج' للإنهاء): ").strip()
            
            if user_input.lower() in ['خروج', 'exit', 'quit']:
                print("\n🌟 [SESSION ENDED]: جاري طي الأبعاد وإغلاق البوابات...")
                node.stop()
                time.sleep(1)
                print("∞🌌 المسارات الجيوديسية في انتظارك دائماً... 🌌∞\n")
                break
            
            if not user_input:
                continue
            
            if user_input.startswith("/connect"):
                parts = user_input.split()
                if len(parts) > 1:
                    try:
                        host_port = parts[1].split(':')
                        target_host = host_port[0]
                        target_port = int(host_port[1])
                        print(f"🔗 [بوابة]: تم توجيه المسار إلى {target_host}:{target_port}")
                    except:
                        print("❌ [خطأ]: التنسيق الصحيح هو /connect IP:Port")
                continue

            # 2. إرسال الرسالة عبر المسار الهايبربولويدي
            print(f"📤 [بث]: جاري تشفير الرسالة وتوجيهها عبر المسار الجيوديسي إلى {target_host}:{target_port}...")
            success = node.send_message(target_host, target_port, user_input)
            
            if success:
                print("✅ [نجاح]: تم عبور الرسالة عبر انحناء الزمكان بنجاح.")
            else:
                print("❌ [فشل]: انقطاع في المسار الجيوديسي. (تأكد من وجود عقدة في الطرف الآخر)")
            
        except KeyboardInterrupt:
            print("\n\n🌟 تم إغلاق العقدة يدوياً.")
            node.stop()
            break
        except Exception as e:
            print(f"\n❌ [خطأ في النظام]: {e}")

if __name__ == "__main__":
    main()

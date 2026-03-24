from acppl import CausalEngine, Event
from acppl.analyzers import brute_force_policy, credential_stuffing_policy
from datetime import datetime, timedelta

print("🔬 اختبار واقعي لـ ACPPL")
print("=" * 50)

# 1. إنشاء المحرك
engine = CausalEngine()

# 2. تسجيل سياسات
engine.register_policy(brute_force_policy)
engine.register_policy(credential_stuffing_policy)

print("✅ تم تحميل السياسات")

# 3. محاكاة هجوم حقيقي
now = datetime.now()

# 150 محاولة تسجيل دخول فاشلة خلال 5 دقائق
for i in range(5):
    engine.add_event(Event(
        "failed_logins",
        now - timedelta(minutes=i),
        count=30
    ))

# 20 IP غير معتاد
engine.add_event(Event(
    "unusual_ips",
    now,
    count=20
))

print("📥 تم إدخال الأحداث")

# 4. تحليل
results = engine.analyze(window_minutes=10)

print("\n📊 النتائج:")
print("-" * 50)

if not results:
    print("❌ لم يتم اكتشاف أي خطر (هذه مشكلة)")
else:
    for r in results:
        print(f"\n🔴 الخطر: {r.risk_name}")
        print(f"المستوى: {r.level}")
        print(f"الاحتمالية: {r.probability:.2f}")
        print(f"المسار: {' → '.join(r.causal_path)}")
        print(f"التوصيات: {r.recommendations}")

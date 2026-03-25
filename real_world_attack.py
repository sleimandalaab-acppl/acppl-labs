"""
Real-world scenario: Credential Stuffing Attack
"""

from acppl import CausalEngine, Event
from acppl.analyzers import credential_stuffing_policy
from datetime import datetime, timedelta


def simulate_attack():
    print("🔐 Simulating real-world attack...")
    print("=" * 50)

    engine = CausalEngine()
    engine.register_policy(credential_stuffing_policy)

    now = datetime.now()

    # 1. Failed logins (bulk attack)
    for i in range(5):
        engine.add_event(Event(
            "failed_logins",
            now - timedelta(minutes=i),
            count=40,  # 40 * 5 = 200 attempts
            source="185.22.33.10"
        ))

    # 2. Multiple IPs
    engine.add_event(Event(
        "unusual_ips",
        now,
        count=25
    ))

    # 3. Login success spike
    engine.add_event(Event(
        "login_success",
        now,
        count=10
    ))

    print(f"📥 Total events: {len(engine.events)}")

    # Analysis
    print("\n🔍 Running causal analysis...\n")
    results = engine.analyze(window_minutes=10)

    if not results:
        print("❌ No threats detected")
        return

    print("📊 RESULTS:")
    print("=" * 50)

    for r in results:
        print(f"\n🚨 Risk: {r.risk_name}")
        print(f"Level: {r.level.value}")
        print(f"Probability: {r.probability:.1%}")
        print(f"Confidence: {r.confidence:.1%}")

        print("\n🔗 Causal Path:")
        print(" → ".join(r.causal_path))

        print("\n💡 Recommendations:")
        for rec in r.recommendations:
            print(f"- {rec}")

    print("\n✅ Analysis complete.")


if __name__ == "__main__":
    simulate_attack()

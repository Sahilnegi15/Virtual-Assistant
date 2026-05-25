import schedule
import time
from agents import handle_query

# Example automated task
def daily_ai_research():
    print("Running Daily AI Research Task...")
    
    query = "Latest trends in AI in 2026"
    result = handle_query(query)
    
    # For now just print (later we send email/telegram)
    print("\n=== AI Research Report ===")
    print(result)
    print("=========================\n")


# Schedule tasks
def start_scheduler():
    schedule.every(1).minutes.do(daily_ai_research)  # change to .day later

    print("Automation started...")

    while True:
        schedule.run_pending()
        time.sleep(1)


def smart_research_task():
    print("Running Smart Research Agent...")

    steps = [
        "Find latest AI trends",
        "Summarize key tools in AI",
        "Explain impact on finance sector"
    ]

    final_report = ""

    for step in steps:
        result = handle_query(step)
        final_report += f"\nStep: {step}\n{result}\n"

    print("\n=== SMART REPORT ===")
    print(final_report)
    print("====================\n")
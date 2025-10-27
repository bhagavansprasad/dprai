# dpr_main.py
"""
DPR Main Entry Point - Stage 1 Test
"""
from langchain_core.messages import HumanMessage
from termcolor import cprint

from dpr_orchestrator import orchestrator_graph


def main():
    """
    Test the orchestrator with a sample DPR request
    """
    # Sample user prompt
    prompt = """
    I need to create a DPR for my MSME cluster project with the following details:
    
    - Cluster Type: Printing Industry
    - Location: Tirupati, Andhra Pradesh
    - Number of Members: 50 units
    - Project Cost: ₹8.2 crore
    - Common Facility Centre: Digital Printing Equipment
    - Seeking: MSE-CDP Grant (60-80% subsidy)
    
    Please help me generate a complete DPR with all 21 sections.
    """
    
    print("\n" + "="*80)
    print("DPR AUTOMATION PLATFORM - STAGE 1 TEST")
    print("="*80)
    print()
    cprint(f"{'USER PROMPT':-^80}", 'blue', attrs=['bold'])
    print(f"\n{prompt}\n")
    print("="*80 + "\n")
    
    # Create initial message
    hprompt = HumanMessage(content=prompt)
    
    # Initialize state
    init_state = {
        "messages": [hprompt]
    }
    
    # Invoke orchestrator
    print("🚀 Starting orchestrator...\n")
    response = orchestrator_graph.invoke(init_state)
    
    # Display final result
    print("\n" + "="*80)
    print("FINAL RESULT")
    print("="*80)
    
    if response and "messages" in response:
        final_message = response["messages"][-1]
        print(f"\n{final_message.content}\n")
    
    print("="*80)
    print("✅ Stage 1 Test Complete!")
    print("="*80 + "\n")
    
    return response


if __name__ == "__main__":
    main()

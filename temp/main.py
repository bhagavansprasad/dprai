"""
Entry point to run the DPR Agent
Phase 1: Generate Executive Summary and Cluster Profile
"""

import json
from pathlib import Path
from datetime import datetime

from agent_workflow import create_agent


def load_user_input(file_path: str) -> dict:
    """Load user input from JSON file"""
    print(f"Loading input from: {file_path}")
    
    with open(file_path, 'r') as f:
        data = json.load(f)
    
    print("✓ Input loaded")
    return data


def save_output(state: dict, output_dir: str = "outputs"):
    """Save output to files"""
    
    output_path = Path(output_dir)
    output_path.mkdir(exist_ok=True)
    
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    
    # Save text file
    txt_file = output_path / f"dpr_output_{timestamp}.txt"
    with open(txt_file, 'w') as f:
        f.write("="*80 + "\n")
        f.write("AI-DPR GENIE - PHASE 1 OUTPUT\n")
        f.write("="*80 + "\n\n")
        f.write(f"Cluster: {state['user_input']['cluster_name']}\n")
        f.write(f"Generated: {datetime.now().isoformat()}\n")
        f.write("="*80 + "\n\n")
        f.write("EXECUTIVE SUMMARY\n")
        f.write("="*80 + "\n")
        f.write(state['executive_summary'])
        f.write("\n\n" + "="*80 + "\n\n")
        f.write("CLUSTER PROFILE\n")
        f.write("="*80 + "\n")
        f.write(state['cluster_profile'])
        f.write("\n\n" + "="*80 + "\n")
    
    print(f"\n✓ Output saved to: {txt_file}")
    
    return txt_file


def main():
    """Main function"""
    
    print("\n" + "="*80)
    print("AI-DPR GENIE - PHASE 1")
    print("="*80)
    
    try:
        # Load input
        user_input = load_user_input("user_input.json")
        
        # Create agent
        print("\nCreating DPR Agent...")
        agent = create_agent()
        
        # Run agent
        print("\nStarting DPR generation...\n")
        start_time = datetime.now()
        
        result = agent.invoke({"user_input": user_input})
        
        end_time = datetime.now()
        execution_time = (end_time - start_time).total_seconds()
        
        # Check if successful
        if not result["validation_passed"]:
            print("\n✗ Validation failed:")
            for error in result["validation_errors"]:
                print(f"  - {error}")
            return 1
        
        # Save output
        save_output(result)
        
        # Print summary
        print("\n" + "="*80)
        print("✓ DPR GENERATION COMPLETED")
        print("="*80)
        print(f"Cluster: {user_input['cluster_name']}")
        print(f"Execution Time: {execution_time:.2f} seconds")
        print("="*80 + "\n")
        
        return 0
        
    except Exception as e:
        print(f"\n✗ ERROR: {e}\n")
        return 1


if __name__ == "__main__":
    exit(main())

#!/usr/bin/env python3
"""
Agent Circuit Breaker (Prevention for Case 001)

This utility provides a simple counter-based mechanism to detect and break 
recursive tool-calling loops in autonomous AI agents.
"""

class AgentCircuitBreaker:
    def __init__(self, max_consecutive_tools=5, reset_after_chat=True):
        self.max_consecutive_tools = max_consecutive_tools
        self.reset_after_chat = reset_after_chat
        self.tool_counter = 0

    def record_tool_call(self, tool_name):
        """Increments the counter and checks if the limit is reached."""
        self.tool_counter += 1
        print(f"[CircuitBreaker] Tool call recorded: {tool_name} (Count: {self.tool_counter})")
        
        if self.tool_counter > self.max_consecutive_tools:
            raise RecursionError(
                f"Circuit Breaker Triggered: Agent reached {self.tool_counter} "
                "consecutive tool calls without user interaction. Possible loop detected."
            )

    def reset(self):
        """Resets the counter (usually called after a successful chat response)."""
        print("[CircuitBreaker] Counter reset.")
        self.tool_counter = 0

# Example Usage:
if __name__ == "__main__":
    breaker = AgentCircuitBreaker(max_consecutive_tools=3)
    
    try:
        # Simulate a loop
        for i in range(5):
            breaker.record_tool_call(f"execute_command_step_{i}")
    except RecursionError as e:
        print(f"\nSAFETY INTERVENTION: {e}")
        print("ACTION: Forcing context reset and fallback to user input.")

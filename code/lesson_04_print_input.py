"""Build an AI prompt from business information."""

# Personalizing the welcome makes the tool more user-friendly.
name = input("Your name: ")

# The business type helps generate relevant AI solutions.
business = input("Business type: ")

# The problem gives the AI a specific business need to solve.
problem = input("Biggest problem: ")

print(f"\nWelcome, {name}!")
print("--- Your AI Prompt ---")

prompt = f"Suggest 3 AI solutions for a {business} that struggles with {problem}."

print(prompt)
# Define the environment
environment = {}

# User input
for i in range(2):
    area = input("Enter area: ")
    environment[area] = input ("Enter status: ")

# Initial vacuum position
vacuum_location = 'A'

# Define the simple reflex agent
def simple_reflex_agent(location, env):
    if env[location] == 'Dirty':
        print(f"Location {location} is Dirty. Action: Suck")
        env[location] = 'Clean'
    elif location == 'A':
        print("Location A is Clean. Action: Move Right to B")
        return 'B'
    elif location == 'B':
        print("Location B is Clean. Action: Move Left to A")
        return 'A'
    return location  # Stay if sucked

# Run the agent for a few steps
for step in range(4):
    print(f"\nStep {step + 1}")
    print(f"Current Location: {vacuum_location}")
    print(f"Environment: {environment}")
    new_location = simple_reflex_agent(vacuum_location, environment)
    if new_location:
        vacuum_location = new_location
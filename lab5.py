# Define the environment
environment = {}
areas = []

# User input
n = int(input("Enter number of partitions: "))
for i in range(n):
    area = input(f"Enter area name {i+1}: ").strip()
    status = input(f"Enter status of {area} (Clean/Dirty): ").strip().capitalize()
    environment[area] = status
    areas.append(area)

# Initial vacuum position
vacuum_location = areas[0]  # Start at the first area

# Define the simple reflex agent
def simple_reflex_agent(location, env):
    if env[location] == 'Dirty':
        print(f"Location {location} is Dirty. Action: Suck and move to next area")
        env[location] = 'Clean'
    else:
        print(f"Location {location} is Clean. Action: Move to next area")

# Run the agent
for step in range(n):
    print(f"\nStep {step + 1}")
    print(f"Current Location: {vacuum_location}")
    print(f"Environment: {environment}")
    
    simple_reflex_agent(vacuum_location, environment)
    
    # Move to next area if it exists
    current_index = areas.index(vacuum_location)
    if current_index + 1 < n:
        vacuum_location = areas[current_index + 1]

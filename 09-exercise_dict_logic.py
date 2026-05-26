"""
TASK: DICTIONARY MANIPULATION AND BASIC DATA FILTERING

1. Data State:
   Create a dictionary named 'server_farm' with the following keys and initial values:
   - "total_servers" (int: 5)
   - "active_servers" (int: 3)
   - "load_percentage" (int: 85)
   - "status_alert" (bool: False)

2. Logic Check (Conditions):
   Write an if/elif/else structure that processes the following rules:
   - IF 'load_percentage' is greater than 80 AND 'active_servers' is less than 'total_servers':
     -> Increase 'active_servers' by 1.
     -> Reset 'load_percentage' to 60.
   - ELIF 'load_percentage' is greater than 90 (and no more servers are available):
     -> Set 'status_alert' to True.
   - ELSE:
     -> Set 'status_alert' to False.

3. Output:
   Print the modified dictionary to the console at the end of the loop
   to verify the logic results.
"""

server_farm = {
    "total_servers": 5,
    "active_servers": 3,
    "load_percentage": 85,
    "status_alert": False
}

while True:
    print(f"Current Server State: {server_farm}")

    if server_farm['load_percentage'] > 80 and server_farm['active_servers'] < server_farm['total_servers']:
        server_farm['active_servers'] = server_farm['active_servers'] + 1
        server_farm['load_percentage'] = 60
    elif server_farm['load_percentage'] > 90 and server_farm['active_servers'] == server_farm['total_servers']:
        server_farm['status_alert'] = True
    else:
        server_farm['status_alert'] = False

    input("Press Enter to continue...")

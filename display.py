
def display(data):
    try:
        if data is not None and len(data) > 0:
            for event in data:
                timestamp = event['created_at'].replace('T', ' ').replace('Z', '')
                if event['type'] == 'PushEvent':
                    print(f"Pushed to {event['repo']['name']} at {timestamp}")
                elif event['type'] == 'CreateEvent':
                    print(f"Created {event['payload']['ref_type']} in {event['repo']['name']} at {timestamp}")
                elif event['type'] == 'PullRequestEvent':
                    print(f"Pull request {event['payload']['action']} in {event['repo']['name']} at {timestamp}")
                elif event['type'] == 'IssuesEvent':
                    print(f"Issue {event['payload']['action']} in {event['repo']['name']} at {timestamp}")
                elif event['type'] == 'WatchEvent':
                    print(f"Starred {event['repo']['name']} at {timestamp}")
                elif event['type'] == 'ForkEvent':
                    print(f"Forked {event['repo']['name']} at {timestamp}")
                else:
                    print(f"{event['type']} in {event['repo']['name']} at {timestamp}")
        else:
            print("No recent activity found for this user.")
    except Exception as e:
        print(e)
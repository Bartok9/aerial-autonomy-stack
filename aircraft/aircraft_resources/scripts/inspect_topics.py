"""
Inspect all topics' message type, publisher node(s), and subscriber nodes

Use as:
    python3 /aas/aircraft_resources/scripts/inspect_topics.py
"""
import subprocess

from inspect_topics_parse import parse_topic_info_lines

def inspect_topics():
    try:
        topics = subprocess.check_output(['ros2', 'topic', 'list']).decode().split()
    except Exception:
        print("Failed to run 'ros2 topic list'. Did you source your ROS setup.bash?")
        return

    print(f"{'TOPIC':<60} | {'TYPE':<40} | {'PUBLISHERS (Nodes)':<40} | {'SUBSCRIBERS (Nodes)':<40}")
    print("-" * 185)

    for t in topics:
        try:
            info = subprocess.check_output(['ros2', 'topic', 'info', '-v', t], stderr=subprocess.DEVNULL).decode().splitlines()
        except Exception:
            continue

        parsed = parse_topic_info_lines(info)
        msg_type = parsed["msg_type"]
        pubs = parsed["pubs"]
        subs = parsed["subs"]

        pub_str = ", ".join(pubs) if pubs else "None"
        sub_str = ", ".join(subs) if subs else "None"

        print(f"{t:<60} | {msg_type:<40} | {pub_str:<40} | {sub_str:<40}")

if __name__ == '__main__':
    inspect_topics()

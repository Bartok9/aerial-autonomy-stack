"""Pure parser for `ros2 topic info -v` line output (offline-testable)."""

from __future__ import annotations


def parse_topic_info_lines(lines):
    """Parse verbose ros2 topic info lines into type/pubs/subs.

    Parameters
    ----------
    lines : iterable of str
        Output of ``ros2 topic info -v <topic>`` split into lines.

    Returns
    -------
    dict with keys: msg_type (str), pubs (list[str]), subs (list[str])
    """
    msg_type = "Unknown"
    pubs, subs = [], []
    current_section = None

    for raw in lines:
        line = raw.strip()
        if line.startswith("Type:"):
            msg_type = line.split("Type:", 1)[1].strip() or "Unknown"
        elif line.startswith("Publisher count:"):
            current_section = "pub"
        elif line.startswith("Subscription count:"):
            current_section = "sub"
        elif line.startswith("Node name:"):
            node_name = line.split("Node name:", 1)[1].strip()
            if node_name != "UNKNOWN" and not node_name.startswith("_ros2cli"):
                if current_section == "pub":
                    pubs.append(node_name)
                elif current_section == "sub":
                    subs.append(node_name)

    return {"msg_type": msg_type, "pubs": pubs, "subs": subs}

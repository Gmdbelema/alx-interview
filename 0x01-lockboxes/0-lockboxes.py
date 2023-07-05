#!/usr/bin/python3

def can_unlock_all(boxes):
    num_boxes = len(boxes)  # Total number of boxes
    unlocked_boxes = [False] * num_boxes  # Track the status of each box (locked/unlocked)
    unlocked_boxes[0] = True  # The first box is initially unlocked

    # Start with the keys in the first box (box 0)
    keys = boxes[0]

    # Iterate over the keys and unlock the corresponding boxes
    for key in keys:
        if key < num_boxes and not unlocked_boxes[key]:
            unlocked_boxes[key] = True
            keys.extend(boxes[key])  # Add the keys from the newly opened box

    # Check if all boxes have been unlocked
    return all(unlocked_boxes)


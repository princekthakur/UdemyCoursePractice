def separate_stones(arr, K):
    box_count = 0  # Counter for boxes used
    current_box_size = 0  # Counter for the size of the current box

    for stone in arr:
        if stone == 0:
            # If the current box is full, increment box count and reset current box size
            if current_box_size == K:
                box_count += 1
                current_box_size = 0
        else:
            # If the current box is not full, increment the current box size
            if current_box_size < K:
                current_box_size += 1
            # If the current box is full, increment box count and reset current box size
            else:
                box_count += 1
                current_box_size = 1

    # Increment box count if there are remaining stones
    if current_box_size > 0:
        box_count += 1

    return box_count


# Example usage
arr = [1, 0, 1, 1]
K = 3
min_boxes = separate_stones(arr, K)
print("Minimum number of boxes required:", min_boxes)

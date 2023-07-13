def separate_stones(arr, K):
    white_count = 0  # Counter for white stones
    black_count = 0  # Counter for black stones
    box_count = 0  # Counter for boxes used

    for stone in arr:
        if stone == 0:
            white_count += 1
        else:
            black_count += 1

        # If the current box is full, increment box count and reset stone counters
        # if white_count == K or black_count == K:
        #     box_count += 1
        #     white_count = 0
        #     black_count = 0

    # If there are remaining stones, increment box count by 1
    while white_count > 0:
        white_count-=K
        box_count += 1
    
    while black_count > 0:
        black_count-=K
        box_count += 1

    return box_count


# Example usage
arr = [1,1,1,1,1]
K = 3
min_boxes = separate_stones(arr, K)
print("Minimum number of boxes required:", min_boxes)

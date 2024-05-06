class Solution:
    def maxWidthOfVerticalArea(self, points: List[List[int]]) -> int:
        # Extract x-coordinates from points
        x_coords = [point[0] for point in points]
    
        # Sort x-coordinates
        x_coords.sort()
    
        # Initialize maximum width
        max_width = 0
    
        # Calculate maximum width between consecutive x-coordinates
        for i in range(1, len(x_coords)):
            max_width = max(max_width, x_coords[i] - x_coords[i - 1])
    
        return max_width
class Solution:
    # Greedy
    def videoStitching(self, clips: List[List[int]], time: int) -> int:
        clips = sorted(clips, key=lambda x:x[0])
        end, count, index, farthestMove = 0, 0, 0, 0
        while end < time:
            while index < len(clips) and clips[index][0] <= end:
                farthestMove = max(farthestMove, clips[index][1])
                index += 1
            if farthestMove == end:
                return -1
            count += 1
            end = farthestMove
    
        return count
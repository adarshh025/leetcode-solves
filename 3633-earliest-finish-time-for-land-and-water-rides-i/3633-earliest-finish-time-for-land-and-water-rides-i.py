class Solution:
    def earliestFinishTime(self, landStartTime: list[int], landDuration: list[int], waterStartTime: list[int], waterDuration: list[int]) -> int:
        min_land = min(s + d for s, d in zip(landStartTime, landDuration))
        min_water = min(s + d for s, d in zip(waterStartTime, waterDuration))
        
        land_first = min(max(min_land, s) + d for s, d in zip(waterStartTime, waterDuration))
        water_first = min(max(min_water, s) + d for s, d in zip(landStartTime, landDuration))
        
        return min(land_first, water_first)
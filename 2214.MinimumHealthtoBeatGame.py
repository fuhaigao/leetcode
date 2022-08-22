class Solution:
    def minimumHealth(self, damage: List[int], armor: int) -> int:
        armorUsed, maxDamage, res = False, 0, 1
        for d in damage:
            res += d
            maxDamage = max(maxDamage, d)
            if not armorUsed and d >= armor:
                armorUsed = True
                res -= armor
        return res if armorUsed else res-maxDamage

    #optimal solution
        # return 1 + sum(damage) - min(max(damage), armor)

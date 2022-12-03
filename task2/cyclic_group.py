from typing import Tuple, Any, Dict

class CyclicGroup():
    def __init__(self, sorted_group: Tuple[Any]) -> None:
        self._cyclic_hashmap = {sorted_group[i]:i for i in range(len(sorted_group))}
        self._cyclic_group = sorted_group

        self.order = len(self._cyclic_group)

    def next(self, value: Any):
        id1 = self._cyclic_hashmap[value]
        next_id = (id1+1)%self.order
        return self._cyclic_group[next_id]

    def previous(self, value: Any):
        id1 = self._cyclic_hashmap[value]
        previous_id = (id1-1)%self.order
        return self._cyclic_group[previous_id]

# Part 1
class RPS(CyclicGroup):
    def __init__(self, sorted_group: Tuple[Any], mapper: Dict[Any, Any]) -> None:
        for key in mapper:
            assert mapper[key] in sorted_group, f"Wrong mapper value: {mapper[key]}.\
                                                  Value in mapper should be in sorted_group."
        super().__init__(sorted_group)
        self.mapper = mapper

    def is_beating(self, value1, value2):
        if self.next(value1) == value2:
            return True
        else:
            return False

    def round_score(self, opponent, player):
        player_value = self.mapper[player]
        opponent_value = opponent

        if opponent_value == player_value:
            return 3
        elif self.is_beating(opponent_value, player_value):
            return 0
        else:
            return 6
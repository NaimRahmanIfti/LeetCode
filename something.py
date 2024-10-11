from dataclasses import dataclass
from typing import List, Dict

@dataclass
class LionDescription:
    name: str
    height: int

@dataclass
class LionSchedule:
    name: str
    enter_time: int
    exit_time: int

class LionCompetition:
    def __init__(self, lions: List[LionDescription], schedule: List[LionSchedule]):
        self.lions = {lion.height: lion.name for lion in lions}  # Mapping heights to names
        self.schedule = {s.name: (s.enter_time, s.exit_time) for s in schedule}
        self.current_lions = {}  # Tracks lions currently in the showroom by height

    def lion_entered(self, current_time: int, height: int):
        # Assume the height is unique for each lion, map directly to names
        if height in self.lions:
            self.current_lions[height] = self.lions[height]

    def lion_left(self, current_time: int, height: int):
        if height in self.current_lions:
            del self.current_lions[height]

    def get_biggest_lions(self) -> List[str]:
        if not self.current_lions:
            return []
        max_height = max(self.current_lions.keys())
        # Filter for all lions that match the maximum height
        biggest_lions = [name for height, name in self.current_lions.items() if height == max_height]
        biggest_lions.sort()  # Sort alphabetically for consistent output
        return biggest_lions

if __name__ == "__main__":
    import sys
    input = sys.stdin.read
    data = input().split()

    descriptions = []
    lion_schedule = []
    i = 0

    while i < len(data):
        if data[i] == 'definition':
            name = data[i + 1]
            height = int(data[i + 2])
            descriptions.append(LionDescription(name, height))
            i += 3
        elif data[i] == 'schedule':
            name = data[i + 1]
            enter_time = int(data[i + 2])
            exit_time = int(data[i + 3])
            lion_schedule.append(LionSchedule(name, enter_time, exit_time))
            i += 4
        elif data[i] == 'start':
            i += 1
            break
        else:
            raise Exception('Invalid input')

    lion_competition = LionCompetition(descriptions, lion_schedule)

    while i < len(data):
        if data[i] == 'enter':
            time = int(data[i + 1])
            height = int(data[i + 2])
            lion_competition.lion_entered(time, height)
            i += 3
        elif data[i] == 'exit':
            time = int(data[i + 1])
            height = int(data[i + 2])
            lion_competition.lion_left(time, height)
            i += 3
        elif data[i] == 'inspect':
            biggest_lions = lion_competition.get_biggest_lions()
            print(biggest_lions)
            i += 1
        elif data[i] == 'end':
            break
        else:
            raise Exception('Invalid input')

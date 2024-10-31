from data import Rectangle, Point, Duration, Song
from typing import List, Optional


# Part 1

def create_rectangle(point1 : Point,point2 : Point)-> Rectangle:
    top_left_x = min(point1.x, point2.x)
    top_left_y = max(point1.y,point2.y)
    bottom_right_x =max(point1.x,point2.x)
    bottom_right_y = min(point1.y,point2.y)

    top_left = Point(top_left_x,top_left_y)
    bottom_right = Point(bottom_right_x, bottom_right_y)

    return Rectangle(top_left,bottom_right)


# Part 2
def shorter_duration_than(duration_1:Duration, duration_2:Duration):
    if duration_1.minutes > duration_2.minutes:
        return True
    elif duration_2.seconds > duration_1.seconds:
        return False
    else:
        return duration_1.seconds > duration_2.seconds

# Part 3
def song_shorter_than(songs: list[Song], upper_bound: Duration) -> list[Song]:
    def shorter_duration_than_2(duration_1: Duration, duration_2: Duration) -> bool:
        if duration_1.minutes < duration_2.minutes:
            return True
        elif duration_1.minutes > duration_2.minutes:
            return False
        else:
            return duration_1.seconds < duration_2.seconds

    return [song for song in songs if shorter_duration_than_2(song.duration, upper_bound)]

# Part 4
def running_time(songs:list[Song])->Duration:
   total_minutes = 0
   total_seconds = 0

   for song in songs:
       total_minutes += song.duration.minutes
       total_seconds += song.duration.seconds

       total_minutes += total_seconds // 60
       total_seconds = total_seconds % 60
   return Duration(total_minutes,total_seconds)



# Part 5
def validate_route(city_links: list[list[str]], route: list[str]) -> bool:
    if not route or len(route) == 1:
        return True

    for i in range(len(route) - 1):
        if [route[i], route[i + 1]] not in city_links and [route[i + 1], route[i]] not in city_links:
            return False
    else:
        return True

# Part 6
def find_repetition_length(arr: List[int], index: int) -> int:
    count = 1
    while index + count < len(arr) and arr[index] == arr[index + count]:
        count += 1
    return count


def longest_repetition(arr: List[int]) -> Optional[int]:
    if not arr:
        return None

    max_length = 0
    max_index = None
    i = 0

    while i < len(arr):
        length = find_repetition_length(arr, i)
        if length > max_length:
            max_length = length
            max_index = i
        i += length

    return max_index

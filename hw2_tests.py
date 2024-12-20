import data
import hw2
import unittest


class TestCases(unittest.TestCase):
    from data import Point, Rectangle, Duration, Song
from hw2_edit.py import create_rectangle,shorter_duration_than, song_shorter_than, running_time,validate_route, longest_repetition
import unittest


    def test_create_rectangle(self):
        point1 = Point(2, 10)
        point2 = Point(10, 2)
        expected = Rectangle(Point(2, 10), Point(10, 2))
        result = create_rectangle(point1, point2)
        self.assertEqual(result.top_left.x, expected.top_left.x)
        self.assertEqual(result.top_left.y, expected.top_left.y)
        self.assertEqual(result.bottom_right.x, expected.bottom_right.x)
        self.assertEqual(result.bottom_right.y, expected.bottom_right.y)

    def test_create_rectangle_2(self):
        point1 = Point(5, 5)
        point2 = Point(5, 5)
        expected = Rectangle(Point(5, 5), Point(5, 5))
        result = create_rectangle(point1, point2)
        self.assertEqual(result.top_left.x, expected.top_left.x)
        self.assertEqual(result.top_left.y, expected.top_left.y)
        self.assertEqual(result.bottom_right.x, expected.bottom_right.x)
        self.assertEqual(result.bottom_right.y, expected.bottom_right.y)

    # Part 2
    def test_shorter_duration_than(self):
        duration1 = Duration(0, 2)
        duration2 = Duration(0, 3)
        expected = False
        result = shorter_duration_than(duration1, duration2)
        self.assertEqual(expected, result)

    def test_shorter_duration_than_2(self):
        duration1 = Duration(0, 3)
        duration2 = Duration(0, 3   )
        expected = False
        result = shorter_duration_than(duration1, duration2)
        self.assertEqual(expected, result)

    # Part 3
    def test_song_shorter_than_1(self):
        songs = [
            Song("Artist A", "Song A", Duration(2, 30)),
            Song("Artist B", "Song B", Duration(3, 0))
        ]
        upper_bound = Duration(2, 45)
        expected = [songs[0]]
        result = song_shorter_than(songs, upper_bound)
        self.assertEqual(expected, result)

    def test_song_shorter_than_2(self):
        songs = [
            Song("Artist A", "Song A", Duration(4, 30)),
            Song("Artist B", "Song B", Duration(3, 0))
        ]
        upper_bound = Duration(3, 45)
        expected = [songs[1]]
        result = song_shorter_than(songs, upper_bound)
        self.assertEqual(expected, result)

    # Part 4

    def test_running_time_1(self):
        songs = [
            Song("Artist A", "Song A", Duration(3, 30)),
            Song("Artist B", "Song B", Duration(4, 45))
        ]
        expected = Duration(8, 15)
        result = running_time(songs)
        self.assertEqual(expected.minutes, result.minutes)
        self.assertEqual(expected.seconds, result.seconds)

    def test_running_time_2(self):
        songs = [
            Song("Artist A", "Song A", Duration(2, 30)),
            Song("Artist B", "Song B", Duration(2, 30))
        ]
        expected = Duration(5, 0)
        result = running_time(songs)
        self.assertEqual(expected.minutes, result.minutes)
        self.assertEqual(expected.seconds, result.seconds)

    # Part 5
    def test_validate_route_1(self):
        city_links = [['san luis obispo', 'santa margarita'], ['santa margarita', 'atascadero']]
        route = ['san luis obispo', 'santa margarita', 'atascadero']
        expected = True
        result = validate_route(city_links, route)
        self.assertEqual(expected, result)

    def test_validate_route_2(self):
        city_links = [['san luis obispo', 'santa margarita'], ['santa margarita', 'atascadero']]
        route = ['san luis obispo', 'atascadero']
        expected = False
        result = validate_route(city_links, route)
        self.assertEqual(expected, result)

    # Part 6

    def test_longest_repetition_1(self):
        arr = [1, 1, 2, 2, 1, 1, 1, 3]
        expected = 4
        result = longest_repetition(arr)
        self.assertEqual(expected, result)

    def test_longest_repetition_2(self):
        arr = [4, 4, 4, 3, 3, 2, 2, 2]
        expected = 0
        result = longest_repetition(arr)
        self.assertEqual(expected, result)


if __name__ == '__main__':
    unittest.main()

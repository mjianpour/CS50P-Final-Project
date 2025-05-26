from project import check_input, single, read_data
import pytest


def main():
    test_check_input()
    test_single()
    test_read_data()


def test_check_input():
    with pytest.raises(SystemExit):
        check_input("allow.csv")
    with pytest.raises(SystemExit):
        check_input("data.txt")
    with pytest.raises(SystemExit):
        check_input("90.25.9")
    assert check_input("   data.csv    ") == "data.csv"
    assert check_input("    45,25,9.8  ") == "45,25,9.8"
    assert check_input(" 45 , 25 , 9.8   ") == "45 , 25 , 9.8"


def test_single():
    assert (
        single("90,25,9.8")
        == "Duration: 5.1s\nRange of the motion: 0.0m\nMax altitude: 31.89m"
    )
    assert (
        single("   90 ,  25  ,  9.8  ")
        == "Duration: 5.1s\nRange of the motion: 0.0m\nMax altitude: 31.89m"
    )
    with pytest.raises(TypeError):
        single("90.25.10")


def test_read_data():
    with pytest.raises(FileNotFoundError):
        read_data("90,25,9.8")
    with pytest.raises(FileNotFoundError):
        read_data("allow.csv")
    assert read_data("data.csv") == [
        ["90", "25", "9.8"],
        ["75", "35", "9.8"],
        ["60", "35", "9.8"],
        ["45", "25", "9.8"],
        ["30", "60", "24.79"],
        ["30", "70", "24.79"],
    ]


if __name__ == "__main__":
    main()

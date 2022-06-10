"""Тестове завдання"""
import argparse


def get_list_from_file(filename: str) -> list:
    """
    Read file and create list of numbers

            Parameters:
                    filename (str): Path to file

            Returns:
                    lines (list): List of numbers
    """
    with open(filename, 'r') as f:
        lines = [int(line.strip()) for line in f]
    return lines


def get_max(filename: str) -> int:
    """
        Finds the maximum number in the file using loop

                Parameters:
                        filename (str): Path to file

                Returns:
                        max (int): Maximum number
    """
    max_num = None
    with open(filename, 'r') as f:
        for line in f:
            num = int(line.strip())
            if not max_num:
                max_num = num
                continue
            if num > max_num:
                max_num = num
    return max_num


def get_min(filename: str) -> int:
    """
        Finds the minimum number in the file using loop

                Parameters:
                        filename (str): Path to file

                Returns:
                        min (int): Minimum number
    """
    min_num = None
    with open(filename, 'r') as f:
        for line in f:
            num = int(line.strip())
            if not min_num:
                min_num = num
                continue
            if num < min_num:
                min_num = num
    return min_num


def get_median(filename: str) -> float:
    """
        Finds the median in the file

                Parameters:
                        filename (str): Path to file

                Returns:
                        med (float): Median
        """
    numbers = get_list_from_file(filename)
    nums_sort = sorted(numbers)
    mid = len(numbers) // 2
    if len(numbers) % 2 == 0:
        med = (nums_sort[mid] + nums_sort[~mid]) / 2
    else:
        med = nums_sort[mid]
    return med


def get_avg(filename: str) -> float:
    """
        Calculate the arithmetic mean in the file

                Parameters:
                        filename (str): Path to file

                Returns:
                        avg (float): Arithmetic mean
        """
    file_len = 0
    file_sum = 0
    with open(filename, 'r') as f:
        for line in f:
            file_sum += int(line.strip())
            file_len += 1
    return file_sum / file_len


def grow_seq(filename: str) -> list:
    """
        Find out the growing sequence of the file.

                Parameters:
                        filename (str): Path to file

                Returns:
                        seq (list): Growing sequence
        """
    seq = []
    tmp = []
    with open(filename, 'r') as f:
        for line in f:
            num = int(line.strip())
            if len(tmp) == 0:
                tmp.append(num)
                continue
            if num > tmp[-1]:
                tmp.append(num)
            else:
                if len(tmp) > len(seq):
                    seq = tmp[:]
                tmp.clear()
    return seq


def fall_seq(filename: str) -> list:
    """
        Find out the falling sequence of the file.

                Parameters:
                        filename (str): Path to file

                Returns:
                        seq (list): Falling sequence
        """
    seq = []
    tmp = []
    with open(filename, 'r') as f:
        for line in f:
            num = int(line.strip())
            if len(tmp) == 0:
                tmp.append(num)
                continue
            if num < tmp[-1]:
                tmp.append(num)
            else:
                if len(tmp) > len(seq):
                    seq = tmp[:]
                tmp.clear()
    return seq


def _main():
    parser = argparse.ArgumentParser(description='File Handler')
    parser.add_argument('-f', '--file', dest='file', type=str, help='Path to file.')

    parser.add_argument('-maxff', '--max_file', action='store_true',
                        help='Finds the maximum number in the file.')

    parser.add_argument('-minff', '--min_file', action='store_true',
                        help='Finds the minimum number in the file.')

    parser.add_argument('-mf', '--med_func', action='store_true',
                        help='Finds the median in the file.')

    parser.add_argument('-avgff', '--avg_file', action='store_true',
                        help='Calculate the arithmetic mean in the file.')

    parser.add_argument('-aseqf', '--aseq_file', action='store_true',
                        help='Find out the growing sequence of the file.')

    parser.add_argument('-dseqf', '--dseq_file', action='store_true',
                        help='Find out the falling sequence of the file.')

    parser.add_argument('-a', '--all', action='store_true', help='Perform all.')

    args = parser.parse_args()

    if args.file:
        try:
            if args.max_file:
                print(get_max(args.file))
            elif args.min_file:
                print(get_min(args.file))
            elif args.med_func:
                print(get_median(args.file))
            elif args.avg_file:
                print(get_avg(args.file))
            elif args.aseq_file:
                print(grow_seq(args.file))
            elif args.dseq_file:
                print(fall_seq(args.file))
            elif args.all:
                print(f"MAX: {get_max(args.file)}")
                print(f"MIN: {get_min(args.file)}")
                print(f"MEDIAN: {get_median(args.file)}")
                print(f"AVG: {get_avg(args.file)}")
                print(f"Growing seq: {grow_seq(args.file)}")
                print(f"Falling seq: {fall_seq(args.file)}")
            else:
                print("You must select functions to calculate.")
        except SystemExit:
            print("Invalid argument.")
        except Exception as e:
            print(f"Error from work with file.\n{e}")
    else:
        print("Enter filename!")


if __name__ == '__main__':
    _main()

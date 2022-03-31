import csv
import logging
import sys
import time


logger = logging.getLogger(__name__)
logging.basicConfig(stream=sys.stdout, level=logging.INFO)


def get_postcodes(files: dict):
    """Get only postcodes and returns a list for further sorting"""
    with open(files['in'], newline='') as file:
        reader = csv.reader(file, dialect='excel')
        postcodes = [row[3] for row in reader]
        return postcodes


def parse_csv(files: dict):
    """Parse csv file and write unique results to a file"""

    postcodes, results_sorted = get_postcodes(files), []
    with open(files['out'], mode='r', newline='') as csvfile:
        with open(files['out'], mode='r', newline='') as resultsfile:
            reader, writer = (
                csv.reader(csvfile, dialect='excel'),
                csv.writer(resultsfile, dialect='excel')
            )
            for row in reader:
                if all(
                        [
                            postcodes.count(row[3]) > 1,
                            row not in results_sorted,
                            row[3] not in results_sorted
                        ]
                ):
                    results_sorted.append(row)
                    writer.writerow(row)
                else:
                    continue


if __name__ == "__main__":
    filepaths = {
        'in': '/home/dfadeev/pp-complete.csv',
        'out': '/home/dfadeev/results.csv'
    }
    t = time.time()
    parse_csv(filepaths)

























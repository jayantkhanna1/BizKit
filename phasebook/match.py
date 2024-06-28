import time
from flask import Blueprint

from .data.match_data import MATCHES


bp = Blueprint("match", __name__, url_prefix="/match")


@bp.route("<int:match_id>")
def match(match_id):
    if match_id < 0 or match_id >= len(MATCHES):
        return "Invalid match id", 404

    start = time.time()
    msg = "Match found" if (is_match(*MATCHES[match_id])) else "No match"
    end = time.time()

    return {"message": msg, "elapsedTime": end - start}, 200


def is_match(fave_numbers_1, fave_numbers_2):
    # Convert the first list of favorite numbers to a set for faster look-up
    fave_numbers_1_set = set(fave_numbers_1)

    # Iterate through each number in the second list of favorite numbers
    for number in fave_numbers_2:
        # If the current number is not in the set of the first list's numbers, return False
        if number not in fave_numbers_1_set:
            return False

    # If all numbers in the second list are found in the set of the first list's numbers, return True
    return True

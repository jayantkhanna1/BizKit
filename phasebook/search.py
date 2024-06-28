from flask import Blueprint, request

from .data.search_data import USERS


bp = Blueprint("search", __name__, url_prefix="/search")


@bp.route("")
def search():
    return search_users(request.args.to_dict()), 200


def search_users(args):
    """Search users database

    Parameters:
        args: a dictionary containing the following search parameters:
            id: string
            name: string
            age: string-
            occupation: string

    Returns:
        a list of users that match the search parameters
    """
   

    # Implement search here!

    # Initialize an empty list to store the search results
    results = []

    # Extract search parameters from the args dictionary
    id = args.get('id')
    name = args.get('name')
    age = args.get('age')
    occupation = args.get('occupation')

    # Search by user ID if provided
    if id:
        for user in USERS:
            if user['id'] == id:
                results.append(user)

    # Search by name if provided (case-insensitive)
    if name:
        name = name.lower()
        for user in USERS:
            if name in user['name'].lower():
                results.append(user)

    # Search by age if provided (within a range of ±1 year)
    if age:
        age = int(age)
        for user in USERS:
            if user['age'] >= age - 1 and user['age'] <= age + 1:
                results.append(user)

    # Search by occupation if provided (case-insensitive)
    if occupation:
        occupation = occupation.lower()
        for user in USERS:
            if occupation in user['occupation'].lower():
                results.append(user)
    
    # If no results were found, return all users
    if len(results)  == 0:
        return USERS

    # Remove duplicate users from the results
    results = list({user['id']: user for user in results}.values())

    # Return the list of users that match the search parameters
    return results

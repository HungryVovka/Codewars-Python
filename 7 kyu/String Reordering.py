# -----------------------------------------------------------
# The input will be an array of dictionaries.
# 
# Return the values as a string-seperated sentence in the order of their keys' integer equivalent (increasing order).
# 
# The keys are not reoccurring and their range is -999 < key < 999. The dictionaries' keys & values will always be strings and will always not be 
# empty.
# 
# Example
# Input:
# List = [
#         {'4': 'dog' }, {'2': 'took'}, {'3': 'his'},
#         {'-2': 'Vatsan'}, {'5': 'for'}, {'6': 'a'}, {'12': 'spin'}
#        ]
# 
# Output:
# 'Vatsan took his dog for a spin'
# -----------------------------------------------------------

def sentence(List):
    new_d = {}
    for d in List:
        new_d.update(d)
    new_arr = new_d.keys()
    sort_arr = sorted([int(item) for item in new_arr])
    arr = []
    for i in sort_arr:
        arr.append(new_d[str(i)])
    return " ".join(arr)
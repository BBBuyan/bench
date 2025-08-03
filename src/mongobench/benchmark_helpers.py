import pymongo

def calc_diffs(old: list[float], new: list[float]):
    for i in range(len(old)):
        old_val = old[i]
        new_val = new[i]
        diff = ((new_val - old_val)/old_val)*100
        print(f"|{old[i]:>10.0f}|{new[i]:>10.0f}|{diff:>10.0f}|")

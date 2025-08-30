def save_result(old: list[float], new: list[float], operation: str):
    depth_list = [1,2,4,8]

    with open("result.txt", "a") as f:
        f.write(f"##{operation}\n")
        f.write(f"|{'depth':^10}|{'w/o index':^10}|{'w index':^10}|{'diff':^10}|\n")
        f.write(f"|{'':-^10}|{'':-^10}|{'':-^10}|{'':-^10}|\n")

        for i in range(len(old)):
            old_val = old[i]
            new_val = new[i]
            diff = ((new_val - old_val)/old_val)*100
            f.write(f"|{depth_list[i]:^10}|{old[i]:>10.0f}|{new[i]:>10.0f}|{diff:>10.0f}|\n")

        f.write("\n")

def mark_end():
    with open("result.txt", "a") as f:
        f.write(f"{'':-<45}")
        f.write("\n")

def mark_operation(operation: str):
    with open("result.txt", "a") as f:
        f.write("\n")
        f.write(f"{operation:-^45}\n")


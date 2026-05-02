




def is_passing(score):
    if score >= 50:
        return True
    else:
        return False

def grade_label(score):
    if score >= 80:
        return "A"
    elif score >= 70:
        return "B"
    elif score >= 50:
        return "C"
    else:
        return "F"

scores = [45, 55, 72, 88]

for s in scores:
    print(s, is_passing(s), grade_label(s))
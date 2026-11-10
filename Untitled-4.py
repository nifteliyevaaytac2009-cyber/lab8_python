def add_bonus(scores, bonus):
    """Orijinal listi yerindəcə dəyişir (heç nə qaytarmır)"""
    for i in range(len(scores)):
        scores[i] += bonus
        if scores[i] > 100:
            scores[i] = 100

def with_bonus(scores, bonus):
    """Orijinala toxunmur, yeni dəyişdirilmiş list qaytarır"""
    new_scores = []
    for s in scores:
        updated = s + bonus
        if updated > 100:
            updated = 100
        new_scores.append(updated)
    return new_scores

# Yoxlamaq üçün test sətirləri:
scores = [70, 95, 88, 100]
print(with_bonus(scores, 10)) 
print(scores)                  
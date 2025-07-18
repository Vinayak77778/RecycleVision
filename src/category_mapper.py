def map_to_category(labels):
    recyclable = ['plastic', 'bottle', 'glass', 'metal', 'can', 'paper', 'cardboard']
    compostable = ['banana', 'leaf', 'food', 'fruit', 'vegetable', 'organic']
    non_recyclable = ['diaper', 'styrofoam', 'sponge', 'plastic wrap', 'trash','battery']

    for label in labels:
        if label in recyclable:
            return "♻️ Recyclable"
        elif label in compostable:
            return "🌱 Compostable"
        elif label in non_recyclable:
            return "🚯 Non-Recyclable"
    return "❓ Unknown"

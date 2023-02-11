from django.test import TestCase

def select_category_parcer(category,sex):
    """принимает вес и выводит категорию и пол"""
    mens=[110, 100, 90, 90, 85, 80, 75, 70, 65, 60, 55]
    woman = [80, 75, 70, 65, 60, 55, 50]
    if sex=='m':
        for i in mens:
            if category>110:
                return "+110"
            if category>i:
                return str(mens[mens.index(i)-1])
        return mens[-1]
    elif sex=='w':
        for i in woman:
            if category>80:
                return "+80"
            if category>i:
                return str(woman[woman.index(i)-1])
        return woman[-1]



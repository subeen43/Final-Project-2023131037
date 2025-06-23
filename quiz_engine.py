import random
from fractions import Fraction

def generate_quiz(grade, level):
    """
    2학년 레벨1~5: 두 자리 덧셈·뺄셈
    3학년 레벨1~5: 세 자리 덧셈·뺄셈, 곱셈
    4학년 레벨1~5: 분수·소수 연산 및 혼합
    """
    questions = []
    for _ in range(10):
        if grade == 2:
            # 2학년
            if level == 1:
                a, b = random.randint(10,19), random.randint(10,19); op = '+'
            elif level == 2:
                a, b = random.randint(10,19), random.randint(10,19); op = '-'
            elif level == 3:
                a, b = random.randint(20,99), random.randint(20,99); op = '+'
            elif level == 4:
                a, b = random.randint(20,99), random.randint(20,99); op = '-'
            else:
                a, b = random.randint(10,99), random.randint(10,99); op = random.choice(['+','-'])
            expr = f"{a} {op} {b}"
            ans = eval(expr)

        elif grade == 3:
            # 3학년
            if level == 1:
                a, b = random.randint(100,199), random.randint(100,199); op = '+'
            elif level == 2:
                a, b = random.randint(100,199), random.randint(100,199); op = '-'
            elif level == 3:
                a, b = random.randint(200,999), random.randint(200,999); op = '+'
            elif level == 4:
                a, b = random.randint(200,999), random.randint(200,999); op = '-'
            else:
                a, b = random.randint(10,99), random.randint(1,9)
                expr = f"{a} * {b}"; ans = a * b
                questions.append((expr, float(ans)))
                continue
            expr = f"{a} {op} {b}"
            ans = eval(expr)

        else:
            # 4학년
            if level == 1:
                a,b = random.randint(1,5), random.randint(1,5)
                c,d = random.randint(1,5), random.randint(1,5)
                expr = f"{a}/{b} + {c}/{d}"
                ans = float(Fraction(a,b) + Fraction(c,d))
            elif level == 2:
                a,b = random.randint(1,9), random.randint(1,9)
                c,d = random.randint(1,9), random.randint(1,9)
                expr = f"{a}/{b} - {c}/{d}"
                ans = float(Fraction(a,b) - Fraction(c,d))
            elif level == 3:
                a = round(random.uniform(0,10),1); b = round(random.uniform(0,10),1)
                expr = f"{a} + {b}"; ans = round(eval(expr),1)
            elif level == 4:
                a = round(random.uniform(0,10),1); b = round(random.uniform(0,10),1)
                expr = f"{a} - {b}"; ans = round(eval(expr),1)
            else:
                a = round(random.uniform(1,10),1)
                b = round(random.uniform(1,10),1)
                c = round(random.uniform(1,10),1)
                ops = random.sample(['+','-','*','/'],2)
                expr = f"{a} {ops[0]} {b} {ops[1]} {c}"
                ans = round(eval(expr),2)

        questions.append((expr, float(ans)))
    return questions
from quiz_engine import generate_quiz

def run_quiz():
    print("\n🎯 Welcome to 수학 덧셈 퀴즈! 🎯")

    # 학년 및 레벨 선택
    grade = 0
    while grade not in (2, 3, 4):
        try:
            grade = int(input("학년을 선택하세요 (2, 3, 4): "))
            if grade not in (2, 3, 4):
                print("❌ 2, 3, 4 중 하나를 입력하세요.")
        except ValueError:
            print("❌ 숫자만 입력하세요.")

    level = 0
    while level not in range(1, 6):
        try:
            level = int(input("레벨을 선택하세요 (1~5): "))
            if level not in range(1, 6):
                print("❌ 1에서 5 사이의 숫자를 입력하세요.")
        except ValueError:
            print("❌ 숫자만 입력하세요.")

    print(f"\n👉 시작: {grade}학년 레벨{level} 문제 최대 10문제\n")

    # 퀴즈 반복 실행
    while True:
        questions = generate_quiz(grade, level)
        correct = 0

        for idx, (q, ans) in enumerate(questions, 1):
            print(f"Q{idx}: {q} = ?")
            try:
                user_ans = float(input(">> "))
            except ValueError:
                print("❌ 숫자를 입력해주세요.")
                continue

            if abs(user_ans - ans) < 1e-6:
                print("✅ 정답!")
                correct += 1
            else:
                print(f"❌ 오답. 정답은 {ans}입니다.")


        # 10문제 완료 후 성취율 계산
        total = len(questions)
        rate = correct / total * 100
        print(f"\n🎉 결과: {correct}/{total} 정답 ({rate:.0f}%)")

        # 80% 이상: 다음 레벨 or 반복
        if rate >= 80:
            choice = input("80% 이상 달성! 다음 레벨로 넘어가시겠습니까? (next/repeat): ").strip().lower()
            if choice == 'next' and level < 5:
                level += 1
                print(f"📈 레벨이 {level}로 상승합니다! 🎊\n")
            else:
                print("🔁 현재 레벨을 다시 도전합니다.\n")
            continue

        # 70% 이하: 반복 or 종료
        if rate <= 70:
            choice = input("70% 이하입니다. 현재 레벨을 다시 도전하시겠습니까? (y/n): ").strip().lower()
            if choice == 'y':
                print("🔁 현재 레벨을 다시 도전합니다.\n")
                continue
            else:
                print("퀴즈를 종료합니다.")
                return

        # 70% 초과 80% 미만: 종료
        print("목표를 달성하지 못했습니다. 퀴즈를 종료합니다.")
        return

if __name__ == "__main__":
    run_quiz()
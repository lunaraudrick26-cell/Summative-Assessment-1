# Exercise 4: Primitive Quiz - OPTIMIZED

quiz = {
    "France": "Paris", "Germany": "Berlin", "Italy": "Rome",
    "Spain": "Madrid", "Portugal": "Lisbon", "Netherlands": "Amsterdam",
    "Belgium": "Brussels", "Sweden": "Stockholm", "Norway": "Oslo",
    "Poland": "Warsaw"
}

score = 0
print("European Capitals Quiz\n" + "=" * 40)

for country, capital in quiz.items():
    answer = input(f"What is the capital of {country}? ")
    if answer.lower() == capital.lower():
        print("Correct!\n")
        score += 1
    else:
        print(f"Wrong! The correct answer is {capital}.\n")

print("=" * 40 + f"\nQuiz complete! Your score: {score}/{len(quiz)}")
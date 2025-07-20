def solve_cryptarithmetic_bt():
    words = ['SEND', 'MORE']
    result = 'MONEY'

    unique_letters = set(''.join(words) + result)
    assert len(unique_letters) <= 10, "Too many unique letters."

    letters = list(unique_letters)
    assignment = {}
    used_digits = set()

    def word_to_num(word):
        return int(''.join(str(assignment[ch]) for ch in word))

    def is_valid():
        # Leading digit check
        for word in words + [result]:
            if assignment[word[0]] == 0:
                return False
        total = sum(word_to_num(word) for word in words)
        return total == word_to_num(result)

    def backtrack(index):
        if index == len(letters):
            if is_valid():
                print("Solution found!")
                for word in words + [result]:
                    print(f"{word} = {word_to_num(word)}")
                print("Mapping:", assignment)
                return True
            return False

        for digit in range(10):
            if digit in used_digits:
                continue
            assignment[letters[index]] = digit
            used_digits.add(digit)
            if backtrack(index + 1):
                return True
            # Backtrack
            used_digits.remove(digit)
            del assignment[letters[index]]
        return False

    if not backtrack(0):
        print("No solution found.")

solve_cryptarithmetic_bt()

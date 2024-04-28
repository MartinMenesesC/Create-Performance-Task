# AP CSP CREATE PERFORMANCE TASK V1
import random, time, math

# Define dictionaries to store problems and solutions for each math section
problem_library = {
    'algebra': {

        'Quadratics': {
            'problems': ["x^2+4x+4 = 0", "x^2-4=0", "2x^2 + 3x - 5 = 0", "3x^2 - 7x + 2 = 0", "4x^2 - 12x + 9 = 0",
                         "x^2 - 10x + 25 = 0", "2x^2 - 8x + 6 = 0"],
            'solutions': ["2", "2", "1", "1/3", "3/2", "5", "1"]
        },
        'Logs': {
            'problems': ["log3(9)", "log3(27)-log3(3)", "log5(125)", "log2(8)", "log4(16)",
                         "log2(4)", "log3(81) - log3(27)", "ln(e)", "ln(e) - ln(1)"],
            'solutions': ["2", "2", "3", "3", "2", "2", "3", "1", "1"]
        },
        'Functions': {
            'problems': ["what is f^-1(3), given f(x) 3x - 9", "what is f^-1)(4), given f(x) (x+1)^2",
                         "what is f^-1(-2), given f(x) 2x^2 + 3x - 4",
                         "what is f^-1)(1), given f(x) x^3 - 2x^2 + x - 1",
                         "what is f^-1(5), given f(x) 2/x",
                         "what is f^-1(2), given f(x) x^2 + 4x + 4", "what is f^-1(1), given f(x) 2/x + 3"],
            'solutions': ["4", "1", "-3/4", "1", "2/5", "-2", "-1/3"]
        },
        'Linear functions': {
            'problems': ["What is the slope-intercept form of the line passing through points (2, 3) and (4, 7)?",
                         "Find the slope of the line passing through (-1, 5) and (3, -2).",
                         "What is the slope of the line passing through (4, 6) and (4, -2)?",
                         "Determine if the points (1, 2), (2, 4), and (3, 6) are collinear.",
                         "Find the x-intercept of the line with equation 2y - 4x = 8.",
                         "Find the y-intercept of the line passing through (3, 5) and (7, 9).",
                         "What is the slope of the line passing through (-3, 2) and (5, 8)?"
                         ],
            'solutions': ["2", "-1.75", "undefined", "Yes", "-2", "1", "1"]
        }},
    'geometry': {
        'Trigonometry': {'problems': ["What is the value of sin(45°)?",
                                      "Calculate cos(30°).",
                                      "Find tan(60°).",
                                      "Determine the value of sin(90°).",
                                      "Compute cos(0°)."], 'solutions': ["1", "√3/2", "√3", "1", "1"]},
        'Volume': {'problems': ["Find the volume of a cube with side length 5 units.",
                                "Calculate the volume of a cylinder with radius 4 units and height 10 units.",
                                "Determine the volume of a cone with radius 3 units and height 8 units.",
                                "Find the volume of a sphere with radius 6 units.",
                                "Calculate the volume of a rectangular prism with dimensions 6 units × 4 units × 3 units."],
                   'solutions': ["125", "502.4", "75.36", "904.32", "72"]},
        'Area': {
            'problems':
                ["Calculate the area of a triangle with base 6 units and height 8 units.",
                 "Find the area of a rectangle with length 10 units and width 5 units.",
                 "Determine the area of a parallelogram with base 12 units and height 7 units.",
                 "Calculate the area of a trapezoid with bases 5 units and 10 units, and height 8 units.",
                 "Find the area of a circle with radius 9 units."],
            'solutions': ["24", "50", "84", "60", "254.34"]},
        'Circles': {
            'problems': ["Calculate the circumference of a circle with radius 6 units.",
                         "Determine the area of a sector of a circle with radius 10 units and central angle of 45 degrees.",
                         "Find the circumference of a circle with diameter 12 units.",
                         "Calculate the area of a segment of a circle with radius 8 units and central angle of 90 degrees.",
                         "Determine the length of an arc of a circle with radius 5 units and central angle of 60 degrees."],
            'solutions': ["37.68", "39.27", "37.68", "50.24", "5"]}
    },
    'calculus':
        {
            'Derivatives': {
                'problems': [
                    "Find the derivative of f(x) = x^2 + 3x - 5 at x = 3.",
                    "Calculate the derivative of g(x) = √x at x = 4.",
                    "Find the derivative of h(x) = 1/x at x = 2.",
                    "Determine the derivative of f(x) = e^x at x = 0.",
                    "Find the derivative of g(x) = ln(x) at x = 1."
                ],
                'solutions': ["9", "1/4", "-1/4", "1", "1"]
            },
            'Integrals': {
                'problems': [
                    "Calculate the integral of f(x) = 2x + 3 from x = 1 to x = 5.",
                    "Find the integral of g(x) = x^2 from x = 0 to x = 3.",
                    "Calculate the integral of h(x) = e^x from x = 0 to x = 2.",
                    "Find the integral of f(x) = sin(x) from x = 0 to x = π.",
                    "Calculate the integral of g(x) = 1/x from x = 1 to x = 2."
                ],
                'solutions': ["26", "9", "e^2 - 1", "2", "ln(2)"]
            },
            'Limits': {
                'problems': [
                    "Find the limit of f(x) = 3x^2 - 2x + 1 as x approaches 2.",
                    "Calculate the limit of g(x) = √x as x approaches 4.",
                    "Find the limit of h(x) = (x^2 - 4)/(x - 2) as x approaches 2.",
                    "Determine the limit of f(x) = sin(x)/x as x approaches 0.",
                    "Find the limit of g(x) = 1/x as x approaches ∞."
                ],
                'solutions': ["11", "2", "4", "1", "0"]},
            'Series': {
                'problems': [
                    "Determine whether the series Σ(1/n) from n=1 to ∞ converges or diverges.",
                    "Decide whether the series Σ((-1)^n)/n from n=1 to ∞ converges or diverges.",
                    "Determine the convergence or divergence of the series Σ(1/n^3) from n=1 to ∞.",
                    "Decide whether the series Σ(1/(2^n)) from n=1 to ∞ converges or diverges.",
                    "Find out if the series Σ((2/3)^n) from n=1 to ∞ converges or diverges.",
                    "Decide whether the series Σ(1/(n*(n+1))) from n=1 to ∞ converges or diverges.",
                    "Determine the convergence or divergence of the series Σ((-1)^(n+1))/(2n - 1) from n=1 to ∞.",
                    "Decide whether the series Σ(1/(n^2 + 1)) from n=1 to ∞ converges or diverges."
                ],
                'solutions': ["diverges", "converges", "converges", "converges", "converges", "converges", "converges",
                              "converges"]
            }

        }
}


def quantity_select():
    global quantity_q
    global math_field

    while True:
        print(f"How many questions on {math_field.capitalize()} do you want to practice?")
        ask_q = input("🡺 ")
        if ask_q.isdigit():
            quantity_q = int(ask_q)
            break
        else:
            print("Please select a valid number.")


def print_with_delay(word, delay=0.2):
    for letter in word:
        print(letter, end='', flush=True)
        time.sleep(delay)
    print()


def select_math():
    global math_field
    while True:
        print(colors.RESET, "\n")
        print("MATH PRACTICE PROGRAM ±")
        print("\n")

        print("What field of math would you like to practice?")
        print(colors.BRIGHT_BLUE, "➤ [1] Algebra")
        print(colors.BRIGHT_GREEN, "➤ [2] Geometry")
        print(colors.BRIGHT_RED, "➤ [3] Calculus")
        print(colors.RESET, 'Type [i] for more information on each topic')

        math_selection = str(input("🡺  "))

        # ADD MORE INFO SECTION

        if math_selection == "1" or math_selection == "algebra":
            math_field = "algebra"
            break
        elif math_selection == "2" or math_selection == "geometry":
            math_field = "geometry"
            break
        elif math_selection == "3" or math_selection == "calculus":
            math_field = "calculus"
            break
        elif math_selection.lower() == "i":
            print_topics_separated()
            print("! Respond with a single number")
            print("! If a question has 2 possible answers, respond with the smallest positive answer")

        else:
            print("You typed an unvalid topic, select again")
            continue

    print("\n")


def print_topics_separated():
    algebra_topics = list(problem_library.get('algebra', {}).keys())
    geometry_topics = list(problem_library.get('geometry', {}).keys())
    calculus_topics = list(problem_library.get('calculus', {}).keys())

    print("Algebra topics:", ', '.join(algebra_topics))
    print("Geometry topics:", ', '.join(geometry_topics))
    print("Calculus topics:", ', '.join(calculus_topics))


def ask_questions():
    global math_field
    global quantity_q
    global correct_answers
    global correct
    global incorrect

    # Initialize dictionaries to track performance of subtopics
    good_topics = {subtopic: 0 for subtopic in problem_library[math_field]}
    bad_topics = {subtopic: 0 for subtopic in problem_library[math_field]}
    total_questions = quantity_q  # Total number of questions asked

    for i in range(quantity_q):  # Will ask the right number of questions
        subtopic = random.choice(list(problem_library[math_field].keys()))  # Choose a random subtopic

        print(colors.RESET, "\n")
        print("---------------------------------------------------------------")
        print("")
        print("Question ", i + 1, ":", sep="")
        num_problems = len(problem_library[math_field][subtopic]['problems'])
        rand_index = random.randint(0, num_problems - 1)

        question_now = problem_library[math_field][subtopic]['problems'][rand_index]
        solution_now = problem_library[math_field][subtopic]['solutions'][rand_index]
        print(question_now)

        print("")
        print(colors.BRIGHT_YELLOW, "Answer: ")
        response = input("➤ ")

        if response == solution_now:
            correct_answers += 1
            correct.append((question_now, solution_now))
            good_topics[subtopic] += 1

        else:
            incorrect.append((question_now, solution_now, response))
            bad_topics[subtopic] += 1


    evaluation()
    subtopic_weak = []

    print("")
    time.sleep(0.6)
    print("\nPerformance by Subtopics:")
    print("")
    print(colors.BRIGHT_GREEN, "\nTopics Performed Well:")
    for subtopic, count in good_topics.items():
        if count > bad_topics[subtopic]:
            print(colors.BRIGHT_YELLOW, subtopic, "-", colors.BRIGHT_GREEN, count, colors.RESET, "correct answer(s)")
            time.sleep(0.3)
    time.sleep(0.3)

    print(colors.BRIGHT_RED, "\nTopics That Need Improvement:", colors.RESET)
    for subtopic, count in bad_topics.items():
        if (count >= good_topics[subtopic]) and (count>=1):
            print(colors.BRIGHT_YELLOW, subtopic, "-", colors.BRIGHT_RED, count, colors.RESET, "incorrect answer(s)")
            subtopic_weak.append(subtopic)
            time.sleep(0.3)

    print("")
    print("Would you like to:")
    print(" [1] Practice a Subtopic")
    print(" [2] Restart")
    user_choice = input(" ➤ ")

    if user_choice == "2":
        return

    print("")
    print("Recommended Practice: ")
    for i in range(0, len(subtopic_weak)):
        print("➤", subtopic_weak[i])
    print("")
    choice_subtopic = input("Which Subtopic would you like to practice? ➤ ").capitalize()
    num_of_q = int(input(f"How much questions do you want to practice on {choice_subtopic}?: "))

    ask_questions_in_subtopic(choice_subtopic, num_of_q)


def ask_questions_in_subtopic(subtopic, num_questions):
    global math_field
    global correct_answers
    global correct
    global incorrect
    global quantity_q

    correct_answers = 0
    correct = []  # Initialize list to store correct answers
    incorrect = []  # Initialize list to store incorrect answers



    total_questions = num_questions  # Total number of questions asked
    quantity_q = total_questions
    for i in range(num_questions):  # Will ask the right number of questions
        print(colors.RESET, "\n")
        print("---------------------------------------------------------------")
        print("")
        print("Question ", i + 1, ":", sep="")

        num_problems = len(problem_library[math_field][subtopic]['problems'])
        rand_index = random.randint(0, num_problems - 1)

        question_now = problem_library[math_field][subtopic]['problems'][rand_index]
        solution_now = problem_library[math_field][subtopic]['solutions'][rand_index]
        print(question_now)

        print("")
        print(colors.BRIGHT_YELLOW, "Answer: ")
        response = input("➤ ")

        if response == solution_now:
            correct_answers += 1
            correct.append((question_now, solution_now))

        else:
            incorrect.append((question_now, solution_now, response))


    evaluation()


def evaluation():
    print("\n\n")
    print("---------------------------------------------------------------")
    print("")
    print("CORRECT ANSWERS:")

    for question, solution in correct:
        print(colors.RESET, "Question:", question)
        print("Correct Answer:", colors.BRIGHT_GREEN, solution)
        print(colors.RESET, "")
        time.sleep(0.5)

    print(colors.BRIGHT_YELLOW, "\n\n")
    print("INCORRECT ANSWERS:")
    for question, solution, response in incorrect:
        print(colors.RESET, "Question:", question)
        print("Correct Answer:", solution)
        print("Your Answer:", colors.BRIGHT_RED, response)
        print(colors.RESET, "")
        time.sleep(0.5)

    print(colors.RESET, "\n ---------------------------------------------------------------")
    print("")
    print(colors.BRIGHT_YELLOW, "Total Correct Answers:", colors.BRIGHT_GREEN, correct_answers, colors.RESET,
          "out of", colors.BRIGHT_BLUE, quantity_q)
    print(colors.BRIGHT_YELLOW, "SCORE: ", colors.RESET, round((100 * (correct_answers / quantity_q)), 2), "%", sep="")
    print("")
    print(" ---------------------------------------------------------------")


class colors:
    BLACK = '\033[30m'
    RED = '\033[31m'
    GREEN = '\033[32m'
    YELLOW = '\033[33m'
    BLUE = '\033[34m'
    MAGENTA = '\033[35m'
    CYAN = '\033[36m'
    WHITE = '\033[37m'
    BRIGHT_BLACK = '\033[90m'
    BRIGHT_RED = '\033[91m'
    BRIGHT_GREEN = '\033[92m'
    BRIGHT_YELLOW = '\033[93m'
    BRIGHT_BLUE = '\033[94m'
    BRIGHT_MAGENTA = ''
    BRIGHT_CYAN = '\033[96m'
    ORANGE = '\033[38;5;208m'
    RESET = '\033[0m'
    PINK = '\033[95m'


# Main Loop
while True:
    correct = []
    incorrect = []
    math_field = ""
    quantity_q = 0
    correct_answers = 0
    good_topics = []
    bad_topics = []

    print(" ---------------------------------------------------------------")

    select_math()
    print_with_delay(math_field.upper())
    quantity_select()
    ask_questions()

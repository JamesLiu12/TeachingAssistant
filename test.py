from PromptGenerator import PromptGenerator

# input = f"""

# """

# text = """Given that 2x + 5y = 22, 3x + 2y = 11, what is the value of x and y?"""
# text = r"""\lim\limits_{{x \to 1}} \frac{\sqrt{x}-1}{\ln{x}}"""
text = r"""Calculate the integral of sin(x)/x"""
print(text)

promptGenerator = PromptGenerator()

response = promptGenerator.get_question_answer(text)
print(response)
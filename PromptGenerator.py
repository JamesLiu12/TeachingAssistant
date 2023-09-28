import g4f

class PromptGenerator:
    def __init__(self, provider=g4f.Provider.ChatBase, model="gpt-4"):
        self.model = model
        self.provider = provider
    def get_completion(self, prompt):
        response = g4f.ChatCompletion.create(
            provider=self.provider,
            model=self.model,
            messages=[{"role": "user", "content": prompt}],
            temperature=0.1, # this is the degree of randomness of the model's output
        )
        return response
    def get_paper_answer(self, input):
        instructions = f"""
        Your task is to answer all the questions in the text delimited by triple backticks by the following steps:
        1 - Divide all the questions into two types. The first type: non-mathematic question. The second type: mathematic question.
        For the first type of question:
            2 - Summarize the reading materials if there is reading materials.
            3 - Work out the solution for each question according to the reading materials.
            4 - Output in the following format:
            <solution 1>
            <seperate line>
            <solution 2>
            <seperate line>
            <solution 3>
            <seperate line>
            ...

        For the second type of question:
            2 - Work out your own solution to each question. Do not start to give solution until you have done the question.
            3 - Output in the following format:
            <solution 1>
            <seperate line>
            <solution 2>
            <seperate line>
            <solution 3>
            <seperate line>
            ...

            Output each solution in the following format:
            Step 1 - <step 1>
            Step 2 - <step 2>
            ...
            Step N - <step N>
        """
        prompt = f"""{instructions}\n```{input}```"""
        return self.get_completion(prompt)

        # Let's think step by step.
    def get_question_answer(self, text):
        instructions = fr"""
        Your task is to help a student finish their math homework in the text delimited by triple backticks.
        Please provide a step-by-step solution to the math problem presented below, ensuring accuracy and correctness in the methodology. Utilize the correct mathematical techniques and principles in your solution. 
        Please format your solution in LaTeX, using the `\begin{{align*}}…\end{{align*}}` environment exclusively. Avoid using the `\[…\]` environment. 
        Use $...$ for inline math mode.
        After solving, kindly validate the correctness of your solution.
        Problem: 
        ```{text}```
        """
        # instructions = fr"""
        # You are tasked with helping a student with their math homework in the text delimited by triple backticks. Please provide a comprehensive, step-by-step, and accurate solution to the problem below, using appropriate mathematical principles and techniques. Use LaTeX for formatting, employing the `\begin{{align*}}…\end{{align*}}` environment for equations and $...$ for inline math. 
        # Validate the correctness of your solution.
        # Problem:
        # ```{text}```
        # """
        prompt = f"""{instructions}\n```{text}```"""
        return self.get_completion(prompt)
import g4f

class PromptGenerator:
    def __init__(self, provider=g4f.Provider.DeepAi, model="gpt-3.5-turbo"):
        self.model = model
        self.provider = provider
    def get_completion(self, prompt):
        response = g4f.ChatCompletion.create(
            provider=self.provider,
            model=self.model,
            messages=[{"role": "user", "content": prompt}],
            temperature=0, # this is the degree of randomness of the model's output
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
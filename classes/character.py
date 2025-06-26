import functions.LLM as fct

class Character:
    def __init__(self, name: str, description: str,model = "llama2:7b"):
        self.name = name
        self.model = model
        self.description = description
        self.list_story = []
        self.list_actions = []
        self.list_thoughts = []
    
    def summarize_with_ia(self):
        """
        Function to summarize the character's thoughts and actions using the IA.
        """
        
        for i in range(len(self.list_story)):
            prompt_thought = f"""
            As the character {self.name}, my original thought was: {self.list_thoughts[i]}. I summarize what I thought in one sentence.
            """
            response_thought = fct.send_prompt(prompt_thought, model=self.model)
            prompt_action = f"""
            As the character {self.name}, my original action was: {self.list_actions[i]}. I summarize what I did in one sentence.
            """
            response_action = fct.send_prompt(prompt_action, model=self.model)
            print(f"Summarized thought: {response_thought}")
            print(f"Summarized action: {response_action}")
            self.list_thoughts[i] = response_thought
            self.list_actions[i] = response_action
    def make_prompt_thought(self, story):
        """
        Function to make a thought for the character.
        
        :param story: The story context to use for generating the thought.
        :return: The generated thought.
        """

        prompt = f"""
        You are {self.description}, previously \n
        """
        for i in range(len(self.list_story)):
            prompt += f"""
            In the context {self.list_story[i]}, I thought {self.list_thoughts[i]}, and I did {self.list_actions[i]} \n.
            """
        prompt += f"Now in the context {story}, what do I think really personnaly as an emotionnal human being about it ?"
        return prompt
    def make_prompt_action(self, story):
        """
        Function to make an action for the character.
        
        :param story: The story context to use for generating the action.
        :return: The generated action.
        """
        prompt = f"""
        You are {self.description}, previously
        """
        for i in range(len(self.list_story)):
            prompt += f"""
            In the context {self.list_story[i]}, I thought {self.list_thoughts[i]}, and I did {self.list_actions[i]}.
            """
        prompt += f"Now in the context {story}, what do I do really personnaly as an emotionnal human being about it?"
        return prompt
    def make_thought(self, story: str):
        """
        Function to generate a thought for the character based on the story context.
        
        :param story: The story context to use for generating the thought.
        :return: The generated thought.
        """
        prompt_thought = self.make_prompt_thought(story)
        thought = fct.send_prompt(prompt_thought, model=self.model)
        self.list_thoughts.append(thought)
        return thought

    def make_action(self, story: str):
        """
        Function to generate an action for the character based on the story context.
        
        :param story: The story context to use for generating the action.
        :return: The generated action.
        """
        prompt_action = self.make_prompt_action(story)
        action = fct.send_prompt(prompt_action, model=self.model)
        self.list_actions.append(action)
        return action

    def react_story(self, story: str):
        """
        Function to react to a story by generating a thought and an action.
        
        :param story: The story context to react to.
        :return: A tuple containing the thought and action generated.
        """
        thought = self.make_thought(story)
        action = self.make_action(story)
        self.list_story.append(story)
        return thought, action
    def __str__(self):
        """
        Display the character's information.
        """
        return f"Name: {self.name}\n Description: {self.description}\n "
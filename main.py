import os
from textwrap import dedent

from crewai import Crew, Task

from agents import editor, idea_analyst, writer
from tasks import CreateTasks


class ContentWritingrew():
    def __init__(self, idea):
        self.idea = idea
    def __call__(self):
        tasks = self._create_tasks()
        crew = Crew(
            tasks=tasks,
            agents=[idea_analyst, writer, editor],
            verbose=True
            )
        result = crew.kickoff()
        return result

    def _create_tasks(self):
        idea = CreateTasks.expand_idea().format(idea=self.idea)
        expand_idea_task = Task(
            description=idea,
            agent = idea_analyst
        )
        write_task =  Task(
            description=CreateTasks.write(),
            agent=writer
        )
        edit_task = Task(
            description=CreateTasks.edit(),
            agent=editor
        )
        return [expand_idea_task, write_task, edit_task]

if __name__ == "__main__":
    dir = "./lore"
    if not os.path.exists(dir):
        os.mkdir(dir)
    idea = input("idea: ")
    my_crew = ContentWritingrew(idea=idea)
    result = my_crew()
    print(dedent(result))
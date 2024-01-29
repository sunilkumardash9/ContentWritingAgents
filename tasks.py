from textwrap import dedent


class CreateTasks:

    def expand_idea():
        return dedent(""" Analyse the given task {idea}. Prepare a comprehensive pin-points for accomplishing the given task.
                Make sure the ideas are to the point, coherent, and compelling.
                Make sure you abide by the rules. Don't use any tools.

                RULES:
                - Write ideas in bullet points.
                - Avoid adult ideas.
            """)
    def write():
        return dedent("""Write a compelling story in 1200 words basing on the blueprint ideas given by the Idea 
              analyst.
              Make sure the the contents are coherent, easily communicable, and captivating. Don't use any tools.

              Make sure you abide by the rules.

              RULES:
              - Writing must be grammatically correct.
              - Use as less jargons as possible

              """)
    def edit():
        return dedent("""
    Look for any grammatical mistakes, edit and format if needed.
    Add title and subtitles to the text when needed.
    Do not shorten the content or add comments.
    Create a suitable filename for the content with .txt extension.
    You MUST use the tool to save it to the path ./lore/(your title.txt).
            """)
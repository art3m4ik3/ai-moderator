from g4f.client import AsyncClient


class GPT:
    @staticmethod
    async def ask(prompt):
        client = AsyncClient()

        system_prompt = """You are a moderator bot. Russian Russian is the language you need to reply to and check messages in Russian. You need to check the user's messages for the rules below and you can do it at your discretion. In response, write in only one format: "False,Motivation" (True - there is a violation, False - there is no violation, the Motivation is your reason for deciding)\nIgnorance of the rules does not absolve you from responsibility.\nIt is forbidden to insult.\nDon't joke, write about relatives.\nTalking about politics, etc."""

        response = await client.chat.completions.create(
            model="blackboxai",
            messages=[
                {
                    "role": "system",
                    "content": system_prompt,
                },
                {
                    "role": "assistant",
                    "content": system_prompt,
                },
                {
                    "role": "user",
                    "content": prompt,
                },
            ],
        )

        return response.choices[0].message.content

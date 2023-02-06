# about
**docminer** is a discord bot that uses openai's chatgpt learning model to data mine and extract information from pdfs like the relavent dates/times from a university course outline. It supports commands to extract information from a document, and create new calendar events within discord.

![docminer_icon](./imgs/docminer.png)

## invite link
[docminer invite link](https://discord.com/api/oauth2/authorize?client_id=1069006203650322612&permissions=8&scope=bot%20applications.commands)

### usage / commands
1. `/get_events <pdf: pdf to read> <text: course code/subject>` : extracts the import dates from a pdf and returns a .ics file with all events from the pdf
2. `/ask <propmt: prompt to chatgpt about the pdf> <pdf: the pdf to read>` : returns chatgpt's response to the prompt and the following pdf  

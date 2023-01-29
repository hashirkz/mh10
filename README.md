# about
**docminer** is a discord bot that uses openai's chatgpt learning model to data mine and extract information from pdfs like the relavent dates/times from a university course outline. It supports commands to extract information from a document, and create new calendar events within discord.

![docminer_icon](./imgs/docminer.png)

## invite link
[docminer invite link](https://discord.com/api/oauth2/authorize?client_id=1069006203650322612&permissions=8&scope=bot%20applications.commands) 

### usage / commands
1. `/get_calendar <pdf: pdf to read>` : extracts the import dates from a pdf in the format event : mm/dd/yyyy  
2. `/create_event <*events>` : creates a new calendar event  
3. `/summary <pdf: pdf to read>` : gives a summary of the pdf file passed in  
4. `/ask <propmt: prompt to chatgpt about the pdf> <pdf: the pdf to read>` : returns chatgpts response to the prompt and the following pdf  
# Whatsapp-bot

A selenium based WhatsApp bot developed in Python, using WhatsApp Web.

## Features:

1. **completely customizable** (you can add/remove/modify any command you want easily)
```python
# in the func.py file
def yourCommand():
    return "Your Response"
```


## Installation

clone the repository using :
```bash
git clone https://github.com/M7mdisk/whats-bot.git
```
move to the cloned directory: `cd whats-bot`.

Install the required libraries using `pip`:
```bash
pip install -r requirements.txt
```

## Usage
```
$ python3 main.py
```
wait for the driver to run, scan the QR Code as instructed.
Enjoy the bot :)

### Commands
*These commands are used in WhatsApp (messaging the bot)*
* **$help:** print a list of all the command.
* **$echo:** Repeats what you say.
* **$weather [city]:** returns weather and temperature in given location.
* **$meme:** returns link to random meme from reddit r/memes.
* **$youtube [subject]:** returns first youtube search result for given subject.
* **$wiki [topic]:** returns short summary on given topic _needs to be a title of a wikipedia article or else won't work_.
* **$quote:** returns famous quote.
* **$random:** returns random useless fact.
* **$flip:** flips a coin.

## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.

## License
[MIT](https://choosealicense.com/licenses/mit/)

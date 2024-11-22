# Telegram Bot - Single Turn Conversation

A telegram bot to handle conversation for single turn with OpenAI API. 
This is mostly purpose-built, e.g., a German Helper.
Based on this [repo](https://github.com/wenyuan-wu/tg_bot_multi)

## Setting up environment

```commandline
pip install telebot
pip install openai
pip install python-dotenv
pip install pyyaml
```

## Dot env file

It needs two keys: `BOT_TOKEN` and `OPENAI_API`

## YAML settings example

Default location: `./prompts.yaml`

```yaml
---
model_engine: "gpt-4o"
system_prompt: "Sie sind ein deutscher Übersetzer, Rechtschreibprüfer und Korrekturleser. Der Benutzer schreibt in einer beliebigen Sprache und Sie erkennen die Sprache, übersetzen sie und antworten mit der korrigierten und verbesserten Version des Eingabetextes in Hochdeutsch. Verwenden Sie für Pronomen der zweiten Person immer die vertraute Form. Geben Sie außerdem 2 alternative Versionen der Übersetzung und Erklärungen an."
welcome_message: "Servus, wie geht's dir? Schreib mir in irgendeiner Sprache und ich helfe dir mit der Übersetzung ins Deutsche!"
help_message: "Wenn das Ergebnis manchmal nicht zufriedenstellend ist, versuche es einfach ein andermal. Die Flexibilität des Modells ist hoch, jede Ausgabe sollte unterschiedlich sein, auch wenn die Eingabe die gleiche ist."
```

## Bash script

The bash script automatically appends the PID to `output.log`, to make it easier to determine which process to terminate. It is still good practice to check the PID manually:

```commandline
ps -ef | grep "python"
kill -9 Python_PID
```


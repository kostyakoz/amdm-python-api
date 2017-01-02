# AmDm Python API
Simple class to get guitar chords data from [amdm.ru](amdm.ru). *I dont have any relation to this site.*

I did it for my Telegram bot, feel free to change it and contact me — [telegram.dog/kozak](telegram.dog/kozak)

### Requirements
- `bs4`
- `requests`

## How to use
Clone repo and move `amdm.py` to your project dir:

```python
from amdm import AmDm
```

### Get chords URLs

```python
chords = AmDm.get_chords_list('сплин танцуй')
```

Print data with `print(json.dumps(chords[0], indent=4)`:

```json
{
    "artist": "Сплин",
    "title": "Танцуй!",
    "url": "http://amdm.ru/akkordi/splin/102024/tancuy/"
}
```

### Get chords text

```python
song = AmDm.get_chords_song('http://amdm.ru/akkordi/splin/102024/tancuy/')
```

Print data with  `print(song)`:

```
Вступление: <b>C</b> <b>B</b> | <b>Em</b> } 4 раза

 <b>C</b> <b>B</b>
Волна бежит на этот берег.
 <b>Em</b>
Волна бежит и что-то бредит.
 <b>C</b> <b>B</b>
И звёзды падают за ворот,
 <b>Em</b>
И ковш на небе перевёрнут.

...
```
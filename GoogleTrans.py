# meta developer: @minimaxno
# meta pic: https://img.icons8.com/color/344/input-latin-letters-emoji.png
# requires: deep-translator


import logging
import deep_translator
from telethon.tl.types import Message
from .. import loader, utils, translations

translator = deep_translator.GoogleTranslator()
available_languages = translator.get_supported_languages(as_dict=True)
logger = logging.getLogger(__name__)


def get_key(dictionary: dict, needle: str) -> str:
    return next((key for key, value in dictionary.items() if value == needle), None)
def get_num(list: list, needle: str) -> int:
    for i in range(0, len(list)):
        if list[i] == needle:
            return i


@loader.tds
class GoogleTranslateMod(loader.Module):
    """Advanced Google Translate module!"""

    strings = {
        "name": "Google Translate",
        "load": "🔄 <b>Translating…</b>",
        "load2": "🔎 <b>Searching… Please, wait.</b>",
        "se-re": "📘 <b>Search result:</b>\n",
        "cll": "🔄 <b>Configuring language list…</b>",
        "args": "🚫 <b>No arguments, no reply…</b>",
        "args2": "🚫 <b>No arguments…</b>",
        "no_lang": "📕 <b>No such language!</b>",
        "setted": "🔤 <b>Your main language is updated!</b>",
        "silent": "🔇 <b>OK, I won't dispay translation message!</b>",
        "unsilent": "🔊 <b>OK, I will dispay translation message!</b>",
        "mark": "🔇 <b>OK, I won't dispay «translated» mark!</b>",
        "unmark": "🔊 <b>OK, I will dispay «translated» mark!</b>",
        "tr-ed": "<b>Translated:</b>",
        "added": "➕ <b>Chat added to autotranslate list!</b>",
        "changed": "〰️ <b>Autotranslate configuration changed!</b>",
        "deled": "➖ <b>Chat deleted from autotranslate list!</b>",
        "alheader": "📃 <b>Chats, in which autotranslate is activated:</b>",
        "subscribe": "🖋️ <b>Now I'll keep original text while autotranslating.</b>",
        "unsubscribe": (
            "🖋️ <b>Now I won't keep original text while autotranslating.</b>"
        ),
        'onboard-h': 'ℹ️ <b>Some useful info about syntax</b>\n\n•  .deflang {two-digit lang code} sets your language to defined.\n• .markmode, .subsmode, .silentmode, .atlist takes no arguments.\n• .autotranslate {start;finish} takes argument only in such format. You may skip start language to define it automatically. Also you may skip finish language to define it from your default language.\n• .translate ({start;finish}) [text/reply] have same rules while defining languages, as previous command. You may skip block in brackets to translate text from autodefined language to your default language.\n• .searchlang {two-digit language code/russion or english language name} returns following language.\n\n In manual [s-t] being used for unnecessary text block. {s-t} — for necessary.',
        'tt': 'tt',
        'lapi': '📥 <b>Language names packet for <code>{}</code> succesfully installed!</b>',
        'lapd': '📤 <b>Language names packet for <code>{}</code> succesfully deleted!</b>'
    }

    strings_ru = {
        "name": "Google Translate",
        "load": "🔄 <b>Перевожу…</b>",
        "load2": "🔎 <b>Ищу… Ожидайте.</b>",
        "se-re": "📘 <b>Найдено:</b>\n",
        "cll": "🔄 <b>Конфигурирую список языков…</b>",
        "args": "🚫 <b>Ни аргумента, ни ответа…</b>",
        "args2": "🚫 <b>Нет аргумента…</b>",
        "no_lang": "📕 <b>Я не знаю такого языка!</b>",
        "setted": "🔤 <b>Ваш основной язык обновлён!</b>",
        "silent": "🔇 <b>Хорошо, теперь не отображаю сообщение о переводе!</b>",
        "unsilent": "🔊 <b>Хорошо, теперь отображаю сообщение о переводе!</b>",
        "mark": "🔇 <b>Хорошо, теперь не отображаю пометку «переведено»!</b>",
        "unmark": "🔊 <b>Хорошо, теперь отображаю пометку «переведено»!</b>",
        "tr-ed": "<b>Переведено:</b>",
        "added": "➕ <b>Чат добавлен в список автоперевода!</b>",
        "changed": "〰️ <b>Конфигурация автоперевода изменена!</b>",
        "deled": "➖ <b>Чат убран из списка автоперевода!</b>",
        "alheader": "📃 <b>Список чатов, в которых активен автоперевод:</b>",
        "subscribe": "🖋️ <b>Теперь я сохраняю оригинальный текст при автопереводе.</b>",
        "unsubscribe": (
            "🖋️ <b>Теперь я не сохраняю оригинальный текст при автопереводе.</b>"
        ),
        'onboard-h': 'ℹ️ <b>Руководство по синтаксису</b>\n\n•  .deflang {двузначный языковой код} установит ваш язык по умолчанию на введённый.\n• .markmode, .subsmode, .silentmode, .atlist не принимают аргументов.\n• .autotranslate {старт;финал} принимает аргументы только в таком формате. При пропуске начального языка, он будет определяться автоматически каждый раз. Финальный язык при пропуске его будет взят из языка по умолчанию.\n• .translate [({старт;финал})] {текст/ответ} имеет те же правила по обозначению языков, что и прошлая команда. Можно пропустить блок в круглых скобках чтобы перевести с автопереведённого языка на язык по умолчанию.\n• .searchlang {двузначный языковой код/название языка на русском или английском} выдаёт язык, соотвтетствующий названию или коду.\n\nВ руководстве [что-то] обозначает необязательный текстовый блок. {что-то} — обязательный.',
        'tt': 'тф',
        'lapi': "📥 <b>Языковой пакет для языка <code>{}</code> успешно установлен!</b>",
        'lapd': '📤 <b>Языковой пакет для языка <code>{}</code> успешно удалён!</b>'
    }

    async def client_ready(self, client, db):
        self._client = client
        self._db = db
        if not self.get("deflang", False):
            self.set("deflang", "en")

        if not self.get("silence", False):
            self.set("silence", False)

        if not self.get("mark", False):
            self.set("mark", True)

        if not self.get("s-script", False):
            self.set("s-script", False)

        if not self.get("tr_cha", False):
            self.set("tr_cha", {})
            
        if not self.get("addla", False):
            self.set("addla", [])

    async def setdeflangcmd(self, message: Message):
        """Use language code with this command to switch basic translation language."""
        lang = utils.get_args_raw(message)
        if lang not in available_languages.values:
            await utils.answer(message, self.strings("nolang"))
        else:
            self.set("deflang", lang)
            await utils.answer(message, self.strings("setted"))

    async def autotranslatecmd(self, message: Message):
        """Use language code with this command to add this chat to autotranslate list."""
        lang = utils.get_args_raw(message)
        if (str(utils.get_chat_id(message)) in self.get("tr_cha")) and not lang:
            tr_cha = self.get("tr_cha")
            del tr_cha[str(utils.get_chat_id(message))]
            self.set("tr_cha", tr_cha)
            await utils.answer(message, self.strings("deled"))
            return

        if ";" not in lang:
            stla = "auto"
            fila = self.get("deflang")
        else:
            stla, fila = lang.split(";", 1)
            if not stla:
                stla = "auto"

            if not fila:
                fila = self.get("deflang")

        if fila not in available_languages.values():
            await utils.answer(message, self.strings("no_lang"))
            return

        if (stla != "auto") and (stla not in available_languages.values()):
            await utils.answer(message, self.strings("no_lang"))
            return

        lang = f"{stla};{fila}"
        tr_cha = tco = self.get("tr_cha")
        tr_cha.update({str(utils.get_chat_id(message)): lang})
        self.set("tr_cha", tr_cha)
        if str(utils.get_chat_id(message)) not in tco.keys():
            await utils.answer(message, self.strings("added"))
        else:
            await utils.answer(message, self.strings("changed"))

    async def onboardhcmd(self, m: Message):
        """Syntax manual."""
        await utils.answer(m, self.strings('onboard-h'))

    async def dllapcmd(self, m: Message):
        """Downloads languages name pack for entered language. Allows to search languages through .searchlang on your own language."""
        lang = utils.get_args_raw(m)
        if lang == '':
            return await utils.answer(m, self.strings('args2'))
        if lang not in available_languages.values():
            await utils.answer(m, self.strings("nolang"))
        if not self.get(f'{lang}langdb', False):
            await utils.answer(m, self.strings('cll'))
            rld = {}
            langword = deep_translator.GoogleTranslator('en', lang).translate('a language').casefold()
            if ' ' in langword:
                langword = deep_translator.GoogleTranslator('en', lang).translate('language').casefold()
            for z in available_languages:
                ru_n = z + ' language'
                ru_n = deep_translator.GoogleTranslator('en', lang).translate(ru_n).casefold().replace(langword, '')
                if ru_n[-1] == ' ':
                    ru_n = ru_n[:-1]
                if ru_n[0] == ' ':
                    ru_n = ru_n.replace(' ', '', 1)
                rld.update({ru_n: available_languages[z]})
            self.set(f'{lang}langdb', rld)
            addla = self.get("addla")
            addla.append(lang)
            addla = self.set("addla", addla)
        return await utils.answer(m, self.strings('lapi').format(lang))

    async def dellapcmd(self, m: Message):
        """Deletes custom language pack."""
        lang = utils.get_args_raw(m)
        if lang == '':
            return await utils.answer(m, self.strings('args2'))
        if lang not in self.get('addla'):
            await utils.answer(m, self.strings("nolang"))
        del self._db[self.__class__.__name__][f'{lang}langdb']
        addla = self.get("addla")
        del addla[get_num(addla, lang)]
        addla = self.set("addla", addla)
        return await utils.answer(m, self.strings('lapd').format(lang))

    async def deflangcmd(self, message: Message):
        """Use language code with this command to switch basic translation language."""
        lang = utils.get_args_raw(message)
        if lang not in available_languages.values():
            await utils.answer(message, self.strings("nolang"))
        else:
            self.set("deflang", lang)
            await utils.answer(message, self.strings("setted"))

    async def searchlangcmd(self, m: Message):
        """Searching language by code or name (RU and EN names avaliable; first usage takes some time to configure database)."""
        query = utils.get_args_raw(m)
        if query == '':
            return await utils.answer(m, self.strings('args2'))
        if not self.get('rulangdb', False):
            await utils.answer(m, self.strings('cll'))
            rld = {}
            for z in available_languages:
                ru_n = z + ' language'
                ru_n = deep_translator.GoogleTranslator('en', 'ru').translate(ru_n).replace('язык', '').replace(' ', '')
                rld.update({ru_n: available_languages[z]})
            self.set('rulangdb', rld)
        rld = self.get('rulangdb')
        for x in range(len(self.get('addla'))):
            try:
                res = self.get(f'{self.get("addla")[x]}langdb')[query]
                return await utils.answer(m, f'{self.strings("se-re")}<code>{query}</code> -> <code>{res}</code>')
            except:
                continue
        try:
            res = available_languages[query]
        except:
            try:
                res = rld[query]
            except:
                if self.strings('tt') == 'тф':
                    res = get_key(rld, query)
                    if res is None:
                        return await utils.answer(m, self.strings('no_lang'))
                else:
                    res = getkey(available_languages, query)
                    if res is None:
                        return await utils.answer(m, self.strings('no_lang'))
        return await utils.answer(m, f'{self.strings("se-re")}<code>{query}</code> -> <code>{res}</code>')
                

    async def silentmodecmd(self, message):
        """Use this command to switch between silent/unsilent mode."""
        if self.get("silence"):
            self.set("silence", False)
            await utils.answer(message, self.strings("unsilent"))
        else:
            self.set("silence", True)
            await utils.answer(message, self.strings("silent"))

    async def subsmodecmd(self, message):
        """Use this command to switch autotranslate subscription mode."""
        if self.get("s-script"):
            self.set("s-script", False)
            await utils.answer(message, self.strings("unsubscribe"))
        else:
            self.set("s-script", True)
            await utils.answer(message, self.strings("subscribe"))

    async def markmodecmd(self, message):
        """Use this command to switch between showing/unshowing «translated» mark."""
        if self.get("mark"):
            self.set("mark", False)
            await utils.answer(message, self.strings("mark"))
        else:
            self.set("mark", True)
            await utils.answer(message, self.strings("unmark"))

    async def atlistcmd(self, message: Message):
        """Sends a list of chats, in which autotranslate is turned on."""
        laco = self._db.get(translations.__name__, "lang", "en")
        autotranslate = self.get("tr_cha")
        alist = self.strings("alheader") + "\n"
        avlad = deep_translator.GoogleTranslator().get_supported_languages(as_dict=True)
        for i in autotranslate.keys():
            st_la, fi_la = autotranslate[i].split(";")
            if st_la == "auto":
                if laco == "ru":
                    st_la = "авто"
            elif laco == "ru":
                st_la = f"{get_key(avlad, st_la)} language"
                st_la = (
                    deep_translator.GoogleTranslator("en", "ru")
                    .translate(st_la)
                    .replace("язык", "")
                )
            else:
                st_la = get_key(avlad, st_la)
            if laco == "ru":
                fi_la = f"{get_key(avlad, fi_la)} language"
                fi_la = (
                    deep_translator.GoogleTranslator("en", "ru")
                    .translate(fi_la)
                    .replace("язык", "")
                )
            else:
                fi_la = get_key(avlad, fi_la)

            type_ = (
                "user"
                if getattr(await self._client.get_entity(int(i)), "first_name", False)
                else "chat"
            )

            alist += (
                f'<a href="tg://openmessage?{type_}_id={i.replace("-100", "")}">id{i.replace("-100", "")}</a>:'
                f" {st_la} » {fi_la}" + "\n"
            )

        await utils.answer(message, alist)

    async def translatecmd(self, message: Message):
        """In fact, it translates. Use (start;final) to mark the start and end language of the translation.
        Leave the start language blank to define it automatically."""
        reply = await message.get_reply_message()
        prompt = utils.get_args_raw(message)
        if not prompt and reply is None:
            await utils.answer(message, self.strings("args"))

        if prompt and prompt.startswith("("):
            lafo, prompt = prompt.split(")", 1)
            if ";" not in lafo:
                prompt = f"({lafo}){prompt}"
                stal = "auto"
                finl = self.get("deflang")
            else:
                lafo = lafo.replace("(", "", 1)
                stal, finl = lafo.split(";", 1)
                if not stal:
                    stal = "auto"

                if not finl:
                    finl = self.get("deflang")

                if (
                    (stal or finl) not in available_languages.values()
                    and (stal != "auto")
                    and (finl not in available_languages.values())
                ):
                    await utils.answer(
                        message,
                        self.strings("no_lang") + "\n" + stal + " " + finl,
                    )
                    return
        else:
            stal = "auto"
            finl = self.get("deflang")

        if not self.get("silence"):
            await utils.answer(message, self.strings("load"))

        if not prompt:
            if reply is None:
                await utils.answer(message, self.strings("args"))
                return
            else:
                prompt = reply.raw_text

        translator = deep_translator.GoogleTranslator(stal, finl)
        translated = translator.translate(prompt)

        if self.get("mark"):
            translated = f'{self.strings("tr-ed")}\n{translated}'

        await utils.answer(message, translated)

    async def watcher(self, message: Message):
        if (
            not getattr(message, "raw_text", False)
            or not message.out
            or str(utils.get_chat_id(message)) not in self.get("tr_cha").keys()
            or message.raw_text.split(maxsplit=1)[0].lower() in self.allmodules.commands
            or (message.text[0] == "/")
            or (message.text == "")
        ):
            return

        stla, fila = self.get("tr_cha")[str(utils.get_chat_id(message))].split(";")

        tren = deep_translator.GoogleTranslator(stla, fila)
        translated = "".join(
            [
                await utils.run_sync(lambda: tren.translate(chunk))
                for chunk in utils.chunks(message.raw_text, 512)
            ]
        )

        if self.get("s-script"):
            translated = (
                message.raw_text + "\n\n" + self.strings("tr-ed") + "\n\n" + translated
            )

        try:
            await utils.answer(message, translated)
        except:
            return
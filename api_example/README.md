# ZenQuotes API
Использую API [ZenQuotes](https://zenquotes.io/) для получения случайной цитаты.

1. Отправляет GET-запрос к API `https://zenquotes.io/api/random`
2. Получает случайную цитату в формате JSON
3. Преобразует данные в таблицу **Pandas DataFrame**
4. Выводит цитату и автора в терминал

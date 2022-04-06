# Environment Variables

PyStark needs some special keys as environment variables to run your bot. This section will explain how to get them and configure them.

!!! important

    Never disclose `API_ID`, `API_HASH` and specially `BOT_TOKEN` to anyone!

- `API_ID`
- `API_HASH`
- `BOT_TOKEN`
- `OWNER_ID`

---

## API Keys

API Keys are one of the most important needed keys to work with any MTProto Framework. They include a `API_ID` and `API_HASH`.

You can get these from [my.telegram.org](https://my.telegram.org)

---

## Bot Token

Bot Token is a specific token for every telegram bot. You will get it when you create a new bot using [BotFather](https://t.me/BotFather)

It should be filled as `BOT_TOKEN`

---

## Owner ID

Your Telegram ID (or Username). Get it using [Identity Bot](https://t.me/TheIdentityBot) or [Rose](https://t.me/MissRose_bot)

It should be filled as `OWNER_ID`.

---

## Filling the Variables

- **For Local Deploy** - fill them in `.env` file.

- **For Heroku Deploy** - fill them after you tap on `Deploy to Heroku` button on your repository.

---

## Non-mandatory Variables

- `SUDO_USERS` - User IDs (or Usernames) of users that can use `sudo_only` commands, buttons, inline searches. Specify multiple users by adding spaces.

---

## Other Variables

Necessity of these variables depends on particular use case. For example, you need `DATABASE_URL` only if you use sql database. You need `REDIS_URL` only if you use redis as your database.

- `DATABASE_URL` - needed only for PostgreSQL database
- `REDIS_URL` - needed only for Redis database (public endpoint)
- `REDIS_PASSWORD` - needed only for Redis database
- `DB_SESSION` - needed only for using Telegram as a database.
- `DB_CHAT_ID`- needed only for using Telegram as a database (ID of a new channel).

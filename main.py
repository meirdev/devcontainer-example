import asyncio

import asyncpg


async def main():
    conn = await asyncpg.connect("postgresql://postgres:postgres@db/postgres")
    row = await conn.fetchrow("SELECT 'works';")
    print(row)
    await conn.close()


asyncio.run(main())

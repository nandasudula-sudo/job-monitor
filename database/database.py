import sqlite3


DATABASE = "storage/jobs.db"


def connect():
    return sqlite3.connect(DATABASE)


def initialize_database():
    connection = connect()

    cursor = connection.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS jobs (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            company TEXT,
            title TEXT,
            location TEXT,
            source TEXT,
            url TEXT UNIQUE,
            discovered_at TEXT
        )
    """)

    connection.commit()
    connection.close()


def insert_job(job):
    connection = connect()

    cursor = connection.cursor()

    try:
        cursor.execute(
            """
            INSERT INTO jobs (
                company,
                title,
                location,
                source,
                url,
                discovered_at
            )
            VALUES (?, ?, ?, ?, ?, ?)
            """,
            (
                job["company"],
                job["title"],
                job["location"],
                job["source"],
                job["url"],
                job["discovered_at"],
            ),
        )

        connection.commit()

    except sqlite3.IntegrityError:
        pass

    connection.close()


def job_exists(url):
    connection = connect()

    cursor = connection.cursor()

    cursor.execute(
        "SELECT id FROM jobs WHERE url = ?",
        (url,),
    )

    result = cursor.fetchone()

    connection.close()

    return result is not None
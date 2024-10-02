import psycopg2


class Database:
    def __init__(self, database: str, host: str, user: str, password: str):
        self.conn = psycopg2.connect(
            database=database, user=user, password=password, host=host
        )
        self.cur = self.conn.cursor()

    def __del__(self):
        self.conn.close()

    def close(self):
        self.conn.close()

    def execute_query(self, query: str) -> list[tuple]:
        self.cur.execute(query)
        return self.cur.fetchall()

    def insert_album(
        self, name: str, date: str, location: str, cover: str, note: str
    ) -> int:
        sql = "INSERT INTO album(name, date, location, cover, note) VALUES(%s, %s, %s, %s, %s) RETURNING album_id"

        album_id = -1

        try:
            self.cur.execute(sql, (name, date, location, cover, note))
            self.conn.commit()

            rows = self.cur.fetchone()
            if rows:
                album_id = rows[0]
        except (Exception, psycopg2.DatabaseError) as error:
            print(error)
        finally:
            return album_id

    def insert_images(self, images_list: list[tuple[int, str, str, str]]):
        sql = (
            "INSERT INTO images(album_id, filepath, note, exif) VALUES(%s, %s, %s, %s)"
        )

        try:
            self.cur.executemany(sql, images_list)
            self.conn.commit()
        except (Exception, psycopg2.DatabaseError) as error:
            print(error)

    def create_tag(self, tag_name: str):
        sql = "INSERT INTO tags(name) VALUES(%s)"

        try:
            self.cur.executemany(sql, (tag_name,))
            self.conn.commit()
        except (Exception, psycopg2.DatabaseError) as error:
            print(error)

    def tag_image(self, image_id: int, tag_name: str):
        insert = "INSERT INTO tag_instances(tag_id, item_id) VALUES(%s, %s)"
        select = "SELECT tag_id FROM tags WHERE tag = %s"
        tag_id = -1
        try:
            self.cur.execute(select, (tag_name,))

            rows = self.cur.fetchone()
            if rows:
                tag_id = rows[0]

        except (Exception, psycopg2.DatabaseError) as error:
            print(error)

        try:
            self.cur.execute(insert, (tag_id, image_id))
            self.conn.commit()
        except (Exception, psycopg2.DatabaseError) as error:
            print(error)

    def get_image_tags(self, image_id: int) -> list[str]:
        select = "SELECT tags.tag_name FROM \
                ((images \
                JOIN tag_instances ON images.image_id = tag_instances.image_id)\
                JOIN tags ON tags.tag_id = tag_instances.tag_id)"
        tags = []
        try:
            self.cur.execute(select, (image_id,))
            rows = self.cur.fetchall()
            if rows:
                tags = [tag[0] for tag in rows]
        except (Exception, psycopg2.DatabaseError) as error:
            print(error)
        finally:
            return tags

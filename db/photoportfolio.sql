-- Adminer 4.8.1 PostgreSQL 17.0 (Debian 17.0-1.pgdg120+1) dump

\connect "photoportfolio";

DROP TABLE IF EXISTS "album";
DROP SEQUENCE IF EXISTS album_album_id_seq;
CREATE SEQUENCE album_album_id_seq INCREMENT 1 MINVALUE 1 MAXVALUE 2147483647 CACHE 1;

CREATE TABLE "public"."album" (
    "album_id" integer DEFAULT nextval('album_album_id_seq') NOT NULL,
    "name" text NOT NULL,
    "date" date NOT NULL,
    "location" text NOT NULL,
    "cover" text NOT NULL,
    "note" text NOT NULL,
    CONSTRAINT "album_pkey" PRIMARY KEY ("album_id")
) WITH (oids = false);


DROP TABLE IF EXISTS "images";
DROP SEQUENCE IF EXISTS images_image_id_seq;
CREATE SEQUENCE images_image_id_seq INCREMENT 1 MINVALUE 1 MAXVALUE 2147483647 CACHE 1;

CREATE TABLE "public"."images" (
    "image_id" integer DEFAULT nextval('images_image_id_seq') NOT NULL,
    "album_id" integer NOT NULL,
    "filepath" text NOT NULL,
    "note" text NOT NULL,
    "exif" jsonb NOT NULL,
    CONSTRAINT "images_pkey" PRIMARY KEY ("image_id")
) WITH (oids = false);


DROP TABLE IF EXISTS "tag_instances";
CREATE TABLE "public"."tag_instances" (
    "tag_id" integer NOT NULL,
    "image_id" integer NOT NULL,
    CONSTRAINT "tag_instances_tag_id_image_id" PRIMARY KEY ("tag_id", "image_id")
) WITH (oids = false);


DROP TABLE IF EXISTS "tags";
DROP SEQUENCE IF EXISTS tags_tag_id_seq;
CREATE SEQUENCE tags_tag_id_seq INCREMENT 1 MINVALUE 1 MAXVALUE 2147483647 CACHE 1;

CREATE TABLE "public"."tags" (
    "tag_id" integer DEFAULT nextval('tags_tag_id_seq') NOT NULL,
    "name" text NOT NULL,
    CONSTRAINT "tags_pkey" PRIMARY KEY ("tag_id")
) WITH (oids = false);


ALTER TABLE ONLY "public"."images" ADD CONSTRAINT "images_album_id_fkey" FOREIGN KEY (album_id) REFERENCES album(album_id) NOT DEFERRABLE;

-- 2024-09-30 13:28:42.991947+00

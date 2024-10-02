import { QueryResultRow } from "pg";

interface ImageResult extends QueryResultRow {
  image_id: number;
  album_id: number;
  filepath: string;
  note: string;
  exif: string;
}

export type { ImageResult };
